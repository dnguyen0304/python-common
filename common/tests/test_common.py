# -*- coding: utf-8 -*-

import os
from nose.tools import assert_in

import common


def test_package_initialization():

    package_directory = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

    def get_subpackages():
        for entry in os.listdir(package_directory):
            entry_path = os.path.join(package_directory, entry)

            if not os.path.isdir(entry_path):
                continue
            if entry.startswith('_'):
                continue
            if entry == 'tests':
                continue

            yield entry

    # Using `subpackage in dir(common)` or `hasattr(common, subpackage)`
    # introduces false negatives presumably because the nose framework
    # has a runtime akin to that of `python setup.py develop`; nose can
    # always "see" all subpackages.
    #
    # Using `all()` instead of iterating one by one produces obfuscated
    # unit test results.
    for subpackage in get_subpackages():
        assert_in(subpackage, common.__all__)

