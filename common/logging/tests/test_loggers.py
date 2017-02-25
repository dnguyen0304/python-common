# -*- coding: utf-8 -*-

from nose.tools import assert_true

from common.logging import loggers


class TestUnstructuredDataLogger:

    def test_can_identify_extra(self):
        log_record = TestUnstructuredDataLogger.get_log_record()
        assert_true(hasattr(log_record, '_extra'))

    @staticmethod
    def get_log_record(extra=None):
        logger = loggers.UnstructuredDataLogger(name='')
        log_record = logger.makeRecord(name='',
                                       level='',
                                       fn='',
                                       lno='',
                                       msg='',
                                       args='',
                                       exc_info='',
                                       extra=extra)
        return log_record

