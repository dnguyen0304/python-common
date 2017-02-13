# -*- coding: utf-8 -*-

from nose.tools import assert_equal, assert_not_in, assert_raises, assert_true

from common.logging import filters


class TestContextFilter:

    def setup(self):
        class LogRecord:
            pass

        self.context_filter = filters.ContextFilter(application_name='foo')
        self.log_record = LogRecord()

    def test_has_event_id(self):
        with assert_raises(AttributeError):
            self.log_record.event_id
        self.context_filter.filter(log_record=self.log_record)

        assert_true(self.log_record.event_id)

    def test_event_id_does_not_include_hyphens(self):
        self.context_filter.filter(log_record=self.log_record)
        assert_not_in('-', self.log_record.event_id)

    def test_has_process_name(self):
        with assert_raises(AttributeError):
            self.log_record.process_name
        self.context_filter.filter(log_record=self.log_record)

        assert_equal(self.log_record.process_name, 'foo')

