# -*- coding: utf-8 -*-

import functools
import logging

import kafka


class KafkaHandler(logging.Handler):

    def __init__(self,
                 hostname,
                 port,
                 topic_name,
                 level=logging.NOTSET,
                 _producer_class=None):

        """
        Handler for logging to Kafka.

        Parameters
        ----------
        hostname : str
            Hostname.
        port : int
            Port.
        topic_name : str
            Topic name.
        level : int
            Numeric value of the severity level.
        _producer_class : object, optional
            Used for testing. Defaults to None.
        """

        super().__init__(level=level)

        if _producer_class is None:
            _producer_class = kafka.KafkaProducer

        class KafkaProducer(_producer_class):
            isend = functools.partialmethod(func=kafka.KafkaProducer.send,
                                            topic=topic_name)

        self._producer = KafkaProducer(
            bootstrap_servers=[hostname + ':' + str(port)],
            value_serializer=self._serialize_value)

    @staticmethod
    def _serialize_value(value):
        return str(value).encode('utf-8')

    def emit(self, record):
        try:
            message = self.format(record=record)
            self._producer.isend(value=message)
        except Exception:
            self.handleError(record=record)

