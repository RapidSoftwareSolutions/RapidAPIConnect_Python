#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
        name='RapidConnect',
        version='0.0.2',
        author='Andrey Bukati',
        author_email='andrey@rapidapi.com',
        description='Official Python client for RapidAPI Connect',
        url='https://github.com/RapidSoftwareSolutions/RapidAPIConnect_Python',
        keywords=['rapidapi', 'api', 'python'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
        ],
        package_dir={'': '.'},
        packages=find_packages('.'),
        install_requires=[
            'requests>=2.8.1',
            'six>=1.10.0',
        ],
)
