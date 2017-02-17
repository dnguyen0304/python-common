# -*- coding: utf-8 -*-

import json
import logging
import re


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

        replacement_field_keys = self._parse_format(self._style._fmt)
        format = [(key, '%(' + key + ')s') for key in replacement_field_keys]

        try:
            for item in record._extra.items():
                setattr(record, *item)
                format.append((item[0], '%(' + item[0] + ')s'))
        except AttributeError:
            pass

        return json.dumps(dict(format)) % record.__dict__

    @staticmethod
    def _parse_format(format):

        """
        Extract all replacement field keys.

        Only the percent style is supported.

        Parameters
        ----------
        format : str
            Percent-style format string.

        Returns
        -------
        list
            List of strings of the replacement field keys.
        """

        pattern = '%\((\w+)\)'
        matches = re.findall(pattern=pattern, string=format)
        return matches or list()

