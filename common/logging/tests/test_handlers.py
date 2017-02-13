# -*- coding: utf-8 -*-

from nose import SkipTest
from nose.tools import assert_equal, assert_false, assert_true

from common.logging import handlers


class MockProducer:

    def __init__(self, *args, **kwargs):
        pass


class TestKafkaHandler:

    def setup(self):
        self.handler = handlers.KafkaHandler(hostname='',
                                             port=0,
                                             topic_name='',
                                             _producer_class=MockProducer)

    def test_accepts_port_of_type_numeric(self):
        raised_error = False

        try:
            handlers.KafkaHandler(hostname='foo',
                                  port=0,
                                  topic_name='',
                                  _producer_class=MockProducer)
        except TypeError:
            raised_error = True

        assert_false(raised_error)

    def test_producer_has_isend_method(self):
        assert_true(hasattr(self.handler._producer, 'isend'))

    # A proper teardown for the following test would require deleting
    # Topics. As noted below, the Kafka server does not expose an API
    # for deleting Topics [1]. Implementing this feature is
    # "non-trivial" [2].
    #
    # References
    # ----------
    # .. [1] "Topics are not deleted but lingered."
    #    https://github.com/dpkp/kafka-python/issues/363
    # .. [2] "Feature: Delete topics"
    #    https://github.com/dpkp/kafka-python/issues/433
    def test_producer_isend_only_requires_value_parameter(self):
        raise SkipTest

    def test_serialize_value(self):
        expected = b'foo'
        output = self.handler._serialize_value('foo')
        assert_equal(output, expected)

