#!/usr/bin/python
# vim:ts=4:sw=4:softtabstop=0:smarttab

"""
Test module with top-level run function.
------------------

If module has a callable name "run", it can be run directly.

"""

from pycopia.QA import core


class SimpleExample(core.TestCase):
    """Example to be added with a basic run test.
    """
    def execute(self):
        return self.passed("You ran me.")


# This example constructs a core.TestSuite, and runs it itself.
def run(config, environment, ui):
    suite = core.TestSuite(config, environment, ui, name="SimpleSuite")
    suite.add_test(SimpleExample)
    return suite.run()

