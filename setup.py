#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

if __name__ == '__main__':
    package_name = 'common'

    description = 'Shared Python libraries.'

    with open('./README.md', 'r') as file:
        long_description = file.read()

    install_requires = ['kafka-python==1.3.3',
                        'SQLAlchemy==1.1.6']

    setuptools.setup(name=package_name,
                     version='0.4.3',
                     description=description,
                     long_description=long_description,
                     url='https://github.com/dnguyen0304/python-common.git',
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     license='MIT',
                     packages=[package_name,
                               package_name + '.database',
                               package_name + '.logging',
                               package_name + '.utilities'],
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)
