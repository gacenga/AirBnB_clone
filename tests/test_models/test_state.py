#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_attributes(self):
        state  = State()
        self.assertTrue(hasattr(state, "name"))

    def test_attribute_type(self):
        state = State()
        self.assertIsInstance(state.name, str)

if __name__ == '__main__':
    unittest.main()
