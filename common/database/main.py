# -*- coding: utf-8 -*-

import datetime

import sqlalchemy
from sqlalchemy import orm


class DBContext:

    def __init__(self, session):

        """
        Decorator class that manages persistence operations for
        ORM-mapped objects.

        Parameters
        ----------
        session : sqlalchemy.orm.session.Session
            Session instance.

        See Also
        --------
        sqlalchemy.orm.session.Session
        """

        # Composition must be used instead of inheritance because
        # SQLAlchemy Sessions are always accessed through a factory.
        self._session = session

    def add(self, entity, by=None):

        """
        Decorator method.

        Extends the SQLAlchemy Session's `add()` to require specifying
        the created or updated `by` information given the respective
        condition. The appropriate `created_at` or `updated_at` field
        is set to the current UTC date and time.

        Parameters
        ----------
        entity : models.Base subclass
            Domain model instance.
        by : int
            Unique identifier for the user who created or updated the
            entity.
        """

        entity_state = sqlalchemy.inspect(entity)
        self._validate_metadata(entity=entity,
                                entity_state=entity_state,
                                by=by)

        if not entity_state.persistent or entity in self._session.dirty:
            self._session.add(entity)

    @staticmethod
    def _validate_metadata(entity, entity_state, by):

        message = 'add() missing 1 required positional argument: "by"'

        if entity_state.transient:
            if by is None:
                raise TypeError(message)
            else:
                entity.created_at = datetime.datetime.utcnow()
                entity.created_by = by
        elif entity_state.persistent:
            if by is None:
                raise TypeError(message)
            else:
                entity.updated_at = datetime.datetime.utcnow()
                entity.updated_by = by

    def __getattr__(self, name):
        return getattr(self._session, name)


class DBContextFactory:

    def __init__(self, connection_string):

        """
        Factory class for producing DBContexts.

        Parameters
        ----------
        connection_string : str
            Formatted string containing host and authentication
            information.
        """

        engine = sqlalchemy.create_engine(connection_string)
        SessionFactory = orm.sessionmaker()
        SessionFactory.configure(bind=engine)

        self._SessionFactory = orm.scoped_session(SessionFactory)

    def create(self):

        """
        Produce an object configured as specified.

        See the Stack Overflow answer for more details [1].

        Returns
        -------
        database.DBContext

        References
        ----------
        .. [1] zzzeek, "SQLAlchemy: Creating vs. Reusing a Session",
           http://stackoverflow.com/a/12223711.
        """

        # Should this dispose the engine, close the connection, and / or
        # close the session?
        session = self._SessionFactory()
        return DBContext(session=session)

