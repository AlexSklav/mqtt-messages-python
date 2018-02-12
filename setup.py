#!/usr/bin/env python
from setuptools import setup

import versioneer


setup(name='mqtt-messages',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description=open('README.md', 'rb').read(),
      author='Lucas Zeer',
      author_email='lucas.zeer@gmail.com',
      url='https://github.com/Lucaszw/mqtt-messages-python',
      install_requires=['onoff'],
      packages=['mqtt_messages'])
