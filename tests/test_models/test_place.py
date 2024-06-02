#!/usr/bin/python3
"""Module for testing the Place class."""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing the Place class."""

    def test_city_id_is_public_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Place.user_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Place.name))

    def test_description_is_public_str(self):
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_is_public_int(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_is_public_int(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_is_public_int(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_is_public_int(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_is_public_float(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_is_public_float(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_is_public_list(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_city_id_default(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_user_id_default(self):
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_name_default(self):
        place = Place()
        self.assertEqual(place.name, "")

    def test_description_default(self):
        place = Place()
        self.assertEqual(place.description, "")

    def test_number_rooms_default(self):
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_default(self):
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_default(self):
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_default(self):
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_default(self):
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_longitude_default(self):
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids_default(self):
        place = Place()
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
