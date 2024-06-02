#!/usr/bin/python3
"""Module for testing the State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unittest for testing the State class"""
    
    def test_name_is_public_str(self):
        self.assertEqual(str, type(State.name))

    def test_name_default(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
