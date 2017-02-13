# -*- coding: utf-8 -*-

import logging

from nose.tools import (assert_false,
                        assert_in,
                        assert_list_equal,
                        assert_true)

from common.logging import formatters


class TestJsonFormatter:

    def setup(self):
        class LogRecord:
            pass

        self.formatter = formatters.JsonFormatter(fmt=logging.BASIC_FORMAT)
        self.log_record = LogRecord()

        self.log_record.levelname = 'levelname'
        self.log_record.name = 'name'
        self.log_record.message = 'message'

    def test_to_json(self):
        output = self.formatter.formatMessage(record=self.log_record)

        assert_true(output.startswith('{'))
        assert_true(output.endswith('}'))
        assert_in("'levelname': 'levelname'", output)
        assert_in("'name': 'name'", output)
        assert_in("'message': 'message'", output)

    def test_to_json_does_not_raise_attribute_error(self):
        raised_error = False
        try:
            self.formatter.formatMessage(record=self.log_record)
        except AttributeError:
            raised_error = True
        assert_false(raised_error)

    def test_parse_format(self):
        expected = ['levelname', 'name', 'message']
        output = self.formatter._parse_format(logging.BASIC_FORMAT)
        assert_list_equal(output, expected)

    def test_parse_format_no_replacement_fields(self):
        expected = list()
        output = self.formatter._parse_format('')
        assert_list_equal(output, expected)

