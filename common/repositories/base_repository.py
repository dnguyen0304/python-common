# -*- coding: utf-8 -*-

import abc
import collections


class EntityConflict(Exception):
    pass


class MultipleResultsFound(Exception):
    pass


class NoResultsFound(Exception):
    pass


class BaseQuery:

    __metaclass = abc.ABCMeta

    def __init__(self, db_context):
        self._db_context = db_context

    def filter(self, **kwargs):
        return self

    def execute(self):
        self._db_context.commit()


# persistence framework
class BaseDBContext:

    __metaclass = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        self._queries = collections.deque()

    def commit(self):
        # commit the transaction ( collection of events)
        results = list()
        for query in self._queries:
            result = self._do_commit(query=query, context=self._context)
            results.append(result)
        return results

    def rollback(self):
        pass

    def dispose(self):
        pass

    @staticmethod
    def _do_commit(self, query, context):
        pass

    @staticmethod
    def _do_rollback(self, query, context):
        pass

    @staticmethod
    def _do_dispose(self, query, context):
        pass


# query logic
class BaseRepository:

    __metaclass = abc.ABCMeta

    def __init__(self, db_context):
        self._db_context = db_context

    @abc.abstractmethod
    def get(self, entity_id):
        self._db_context.queries.append(query)
        return query

    @abc.abstractmethod
    def add(self, entity, by=None):

        """
        Add the entity to the repository.

        Parameters
        ----------
        entity : models.Base subclass
            Domain model to be added.
        by : models.Base subclass, optional.
            Domain model performing the operation. Defaults to None.
        """

        self._db_context.queries.append(query)

    # delete
    @abc.abstractmethod
    def remove(self, entity):
        self._db_context.queries.append(query)

    @abc.abstractmethod
    def _search(self, predicate):
        # string
        return query
