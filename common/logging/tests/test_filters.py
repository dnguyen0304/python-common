# -*- coding: utf-8 -*-

from nose.tools import assert_equal, assert_raises, assert_true

from common.logging import filters


class TestContextFilter:

    def setup(self):
        class LogRecord:
            pass

        self.context_filter = filters.ContextFilter(application_name='foo')
        self.log_record = LogRecord()

    def test_has_events_id(self):
        with assert_raises(AttributeError):
            self.log_record.events_id
        self.context_filter.filter(log_record=self.log_record)

        assert_true(self.log_record.events_id)

    def test_has_process_name(self):
        with assert_raises(AttributeError):
            self.log_record.process_name
        self.context_filter.filter(log_record=self.log_record)

        assert_equal(self.log_record.process_name, 'foo')

