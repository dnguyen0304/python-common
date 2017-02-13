# -*- coding: utf-8 -*-

from nose.tools import assert_in

from common.logging import formatters
from common.logging.tests import test_loggers


def test_format_extra_as_json():

    extra = {'foo': 'bar'}
    log_record = test_loggers.TestUnstructuredDataLogger.get_log_record(extra=extra)
    log_record.message = ''
    formatter = formatters.JsonFormatter()

    output = formatter.formatMessage(record=log_record)

    assert_in("'foo': 'bar'", output)

