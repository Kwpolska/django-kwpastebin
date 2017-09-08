#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup

setup(name='django-kwpastebin',
      version='0.1.0',
      description='A simple, yet stylish, pastebin',
      keywords='django,pastebin',
      author='Chris Warrick',
      author_email='chris@chriswarrick.com',
      url='https://github.com/Kwpolska/django-kwpastebin',
      license='3-clause BSD',
      long_description=io.open('./README.rst', 'r', encoding='utf-8').read(),
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 2 - Alpha',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3'],
      packages=['kwpastebin'],
      install_requires=['Django', 'hashids', 'django-hashid-field'],
      )
