#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011-2024 Mitar <mitar.trac@tnode.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import setup

VERSION = '0.1.6'
PACKAGE = 'mathjax'

setup(
    name='MathJaxPlugin',
    version=VERSION,
    description="Renders mathematical equations using MathJax library.",
    author='Mitar',
    author_email='mitar.trac@tnode.com',
    url='https://trac-hacks.org/wiki/TracMathJaxPlugin',
    keywords='trac plugin',
    license="AGPLv3",
    packages=[PACKAGE],
    include_package_data=True,
    package_data={
        PACKAGE: ['htdocs/*.js'],
    },
    install_requires=[],
    zip_safe=False,
    entry_points={
        'trac.plugins': '%s = %s' % (PACKAGE, PACKAGE),
    },
)
