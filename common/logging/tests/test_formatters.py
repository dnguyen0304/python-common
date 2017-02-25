# -*- coding: utf-8 -*-

import json
import logging

from nose.tools import assert_false, assert_in, assert_true

from common.logging import formatters


class TestJsonFormatter:

    def __init__(self):
        self.formatter = None
        self.log_record = None

    def setup(self):
        fmt = json.dumps({'timestamp': '%(asctime)s',
                          'level_name': '%(levelname)s',
                          'message': '%(message)s'})
        self.formatter = formatters.JsonFormatter(fmt=fmt)
        self.log_record = logging.makeLogRecord(dict())

        self.log_record.levelname = 'level_name'
        # Set the msg attribute because the message attribute is
        # overwritten in format() by getMessage().
        self.log_record.msg = 'message'

    def test_to_json(self):
        log_message = self.formatter.format(record=self.log_record)

        assert_true(log_message.startswith('{'))
        assert_true(log_message.endswith('}'))
        assert_in('"timestamp"', log_message)
        assert_in('"level_name": "level_name"', log_message)
        assert_in('"message": "message"', log_message)

    def test_to_json_does_not_raise_attribute_error(self):
        raised_error = False
        try:
            self.formatter.format(record=self.log_record)
        except AttributeError:
            raised_error = True
        assert_false(raised_error)

    def test_to_json_includes_extra_data_as_string_literals(self):
        self.log_record._extra = {'foo': '%(foo)s'}
        log_message = self.formatter.format(record=self.log_record)
        assert_in('"foo": "%(foo)s"', log_message)

