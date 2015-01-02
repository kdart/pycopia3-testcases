#!/usr/bin/python
# vim:ts=4:sw=4:softtabstop=0:smarttab

"""
Eat
---

Example test case. Your overview documentation goes here.
"""

from pycopia.QA import core


class EatTheApple(core.Test):
    """
    Purpose
    -------

    Demonstrate eating an apple.

    Pass Criteria
    -------------

    The apple is eaten.

    Start Condition
    ---------------

    empty stomach.

    End Condition
    -------------

    Stomach full of apple.

    Reference
    ---------

    Gray's Anatomy.

    Procedure
    +++++++++

    - Open mouth
    - Place apple to mouth
    - Bite with teeth
    - Chew
    - swallow
    - repeat steps 2 through 5 until apple is gone.
    """

    def execute(self):
        return self.manual()


class EatUseCase(core.UseCase):
    """Eating the apple use case.

    A use case typically constructs a TestSuite containing a set of tests for
    this particular use case. The ``get_suite`` method takes a config and
    environment that it can use to adjust the set of test.
    """

    @staticmethod
    def get_suite(config, environment, ui):
        suite = core.TestSuite(config, environment, ui, name="EatingSuite")
        suite.add_test(EatTheApple)
        return suite
