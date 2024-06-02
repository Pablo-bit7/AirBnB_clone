#!/usr/bin/python3
"""Module for testing the City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""

    def test_state_id_is_public_str(self):
        self.assertEqual(str, type(City.state_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(City.name))

    def test_state_id_default(self):
        city = City()
        self.assertEqual(city.state_id, "")

    def test_name_default(self):
        city = City()
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
