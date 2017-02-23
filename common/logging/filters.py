# -*- coding: utf-8 -*-

import logging
import uuid


class ContextFilter(logging.Filter):

    def __init__(self, application_name):

        """
        Parameters
        ----------
        application_name : str
            Application name.
        """

        super().__init__()
        self._application_name = application_name

    def filter(self, log_record):

        """
        Impart the logging call with additional context.

        This processing adds the process's name and an event ID.
        Assuming the log repository stores data across many
        applications, services, etc., namespaces for differentiation
        are mandatory.

        Parameters
        ----------
        log_record : logging.LogRecord
            Log record.

        Returns
        -------
        bool
            This method always returns True. Rather than filtering
            LogRecords, they are updated in-place.
        """

        log_record.event_id = str(uuid.uuid4())
        log_record.process_name = self._application_name
        return True

