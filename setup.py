#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'semver>=2.0'
    # TODO: put package requirements here
]

setup_requirements = [
]

test_requirements = [
]

setup(
    name='semvercli',
    version='0.1.4',
    description="basic CLI for python-semver",
    long_description=readme + '\n\n' + history,
    author="matthew davidson",
    author_email='matthew.davidson@ingrooves.com',
    url='https://github.com/matchdav/semvercli',
    packages=find_packages(include=['semvercli']),
    entry_points={
        'console_scripts': [
            'semvercli=semvercli.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='semvercli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
