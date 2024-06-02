#!/usr/bin/python3
"""Module for testing the Review class."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing the Review class."""

    def test_place_id_is_public_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_str(self):
        self.assertEqual(str, type(Review.text))

    def test_place_id_default(self):
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id_default(self):
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_text_default(self):
        review = Review()
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
