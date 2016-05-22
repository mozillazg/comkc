#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding='utf-8') as history_file:
    history = history_file.read()

requirements = [
]

setup(
    name='comkc',
    version='0.1.0',
    description="a server for comic.",
    long_description=readme + '\n\n' + history,
    author="mozillazg",
    author_email='mozillazg101@gmail.com',
    url='https://github.com/mozillazg/comkc',
    packages=[
        'comkc',
    ],
    package_dir={'comkc':
                 'comkc'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='comkc',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
