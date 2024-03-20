#!/usr/bin/env python3
from distutils.core import setup

setup(name='dbrepo',
      version='1.4.2',
      description='A library for communicating with DBRepo',
      author='Martin Weise',
      author_email='martin.weise@tuwien.ac.at',
      packages=['client'],
      requires=['requests']
      )
