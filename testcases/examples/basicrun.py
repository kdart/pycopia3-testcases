#!/usr/bin/python
# vim:ts=4:sw=4:softtabstop=0:smarttab

"""
Test module with top-level run function and no core functionality.
------------------

If module has a callable name "run", it can be run directly, but can't do much.
However it can be useful for quick-and-dirty test cases, for those times when
you're really in a hurry.

"""

from pycopia.QA.constants import TestResult


# This example just runs and returns a result. NO report is generated.
def run(config, environment, ui):
    print("Running from a plain run function.")
    return TestResult.PASSED

