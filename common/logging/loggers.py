# -*- coding: utf-8 -*-

import logging


class UnstructuredDataLogger(logging.Logger):

    def makeRecord(self,
                   name,
                   level,
                   fn,
                   lno,
                   msg,
                   args,
                   exc_info,
                   func=None,
                   extra=None,
                   sinfo=None):

        """
        Create a new LogRecord.

        This extends the factory method so "extra" key-value pairs can
        be identified later.

        Returns
        -------
        logging.LogRecord
        """

        log_record = super().makeRecord(name=name,
                                        level=level,
                                        fn=fn,
                                        lno=lno,
                                        msg=msg,
                                        args=args,
                                        exc_info=exc_info,
                                        func=func,
                                        extra=extra,
                                        sinfo=sinfo)
        log_record._extra = extra
        return log_record

