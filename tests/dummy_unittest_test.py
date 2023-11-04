# The file name should always have _test.py for it to be automatically picked up by pytest
from unittest import TestCase

class DummyTestClass(TestCase):
    # test case in pytest should always start with test_
    def test_dummy(self):
        print("This is dummy Test Case...")
        self.assertTrue(True)
