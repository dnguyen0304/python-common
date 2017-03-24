# -*- coding: utf-8 -*-

import io

from nose.tools import assert_equal, assert_raises_regexp, raises

from common import utilities


def test_get_configuration():

    _configuration_file = io.StringIO('{ "foo": "bar" }')

    configuration = utilities.get_configuration(
        application_name='foo',
        _configuration_file=_configuration_file)

    assert_equal(configuration['foo'], 'bar')


def test_get_configuration_standardize_application_name():

    with assert_raises_regexp(EnvironmentError, 'FOOBAR'):
        utilities.get_configuration(application_name='foo_bar')


@raises(EnvironmentError)
def test_get_configuration_missing_configuration_file_path():

    utilities.get_configuration(application_name='foo')
