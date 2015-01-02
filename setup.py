#!/usr/bin/python
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab


from setuptools import setup

NAME = "pycopia3-testcases"
VERSION = "1.0"


setup(name=NAME, version=VERSION,
      namespace_packages=["testcases"],
      packages="testcases",
      description="Base namespace package for all test cases.",
      long_description=open("README.md").read(),
      license="LGPL",
      author="Keith Dart",
      author_email="keith@darworks.biz",
      keywords="automated tests",
      url="http://www.pycopia.org/",
      classifiers=["Operating System :: POSIX",
                   "Topic :: Software Development :: Libraries :: Python Modules",  # noqa
                   "Intended Audience :: Developers"],
      )
