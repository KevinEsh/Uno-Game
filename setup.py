#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from src import __version__

requirements = [
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO: put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

desc = "UNO Game on a web server project"
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='UnoGame',
    version=__version__,
    description=desc,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Kevin Esh",
    author_email='kevin@valiot.io',
    url='https://172.17.0.2:8080',
    packages=find_packages(include=['src']),
    # entry_points={
    #     'console_scripts': [
    #         'heinekenWorker = src.__main__:main',
    #         'pycmd = src.cmd.__main__:main'
    #     ]
    # },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='webUnoGame',
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)