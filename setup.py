#!/usr/bin/env python

import sys
from setuptools import setup

import version

sys.path.insert(0, '.')


setup(name='mqtt-messages',
      version=version.getVersion(),
      description=open('README.md', 'rb').read(),
      author='Lucas Zeer',
      author_email='lucas.zeer@gmail.com',
      url='https://github.com/Lucaszw/mqtt-messages-python',
      install_requires=['onoff'],
      packages=['mqtt_messages'])
