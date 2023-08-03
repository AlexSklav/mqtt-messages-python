#!/usr/bin/env python
from setuptools import setup

import versioneer

with open('README.md', 'r', encoding='utf-8') as f:
    description = f.read().strip()

setup(name='mqtt-messages',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description=description,
      author='Lucas Zeer',
      author_email='lucas.zeer@gmail.com',
      url='https://github.com/Lucaszw/mqtt-messages-python',
      install_requires=['onoff'],
      packages=['mqtt_messages'])
