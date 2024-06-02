#!/usr/bin/python3
"""Module for testing the Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class."""

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Amenity.name))

    def test_name_default(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
