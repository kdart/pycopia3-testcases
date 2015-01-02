#!/usr/bin/python
# vim:ts=4:sw=4:softtabstop=0:smarttab

"""
Run a module, like a script.
----------------------------

You may also write a simple test case as top-level code in a module. TestCase
methods are magically inserted into the modules scope.
"""


def execute():
    print("You got me")
    info("same place")
    assertTrue(True)
    assertFalse(False)
    passed("Test passed")
