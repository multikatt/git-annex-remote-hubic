#!/usr/bin/env python2

# Copyright (c) 2014 Thomas Jost
#
# This file is part of git-annex-remote-hubic.
#
# git-annex-remote-hubic is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# git-annex-remote-hubic is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# git-annex-remote-hubic. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(name="git-annex-remote-hubic",
      version="0.1",
      description="A git-annex special remote for hubiC",
      long_description=open("README.md", "r").read(),
      author="Thomas Jost",
      author_email="schnouki@schnouki.net",
      url="https://github.com/Schnouki/git-annex-remote-hubic",
      packages=find_packages(),
      install_requires=[
          "python-dateutil",
          "python-swiftclient",
          "rauth>=0.6",
      ],
      entry_points={
          "console_scripts": [
              "git-annex-remote-hubic = hubic_remote.main:main",
          ],
      },
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Plugins",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Programming Language :: Python :: 2",
          "Topic :: System :: Archiving",
      ],
)
