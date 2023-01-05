# Author: Konn <hello@konn.ink>
# Copyright (c) 2022 Konn

from setuptools import setup
import YayAPI

DESCRIPTION = 'Unofficial api library for yay.space'
NAME = 'YayAPI'
AUTHOR = 'Konn'
AUTHOR_EMAIL = 'hello@konn.ink'
URL = 'https://github.com/konn-konn/YayAPI'
DOWNLOAD_URL = 'https://github.com/konn-konn/YayAPI'
VERSION = YayAPI.__version__

INSTALL_REQUIRES = [
    'requests>=2.25.1'
]
PACKAGES = [
    'YayAPI'
]

with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
long_description = readme

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      )
