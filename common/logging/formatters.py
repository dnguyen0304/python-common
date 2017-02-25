# -*- coding: utf-8 -*-

import json
import logging


class JsonFormatter(logging.Formatter):

    def formatMessage(self, record):

        """
        Generate the JSON representation of the log record.

        When configured alongside the UnstructuredDataLogger, arbitrary
        data passed within the "extra" parameter is dynamically
        unpacked and added to the log record.

        Parameters
        ----------
        record : logging.LogRecord
            LogRecord.

        Returns
        -------
        str
            Text representation of the log record formatted as JSON.

        See Also
        --------
        utilities.UnstructuredDataLogger
        """

        log_record = json.loads(self._style._fmt % record.__dict__,
                                encoding='utf-8')
        try:
            log_record.update(record._extra)
        except AttributeError:
            pass
        except TypeError:
            pass
        return json.dumps(log_record)

