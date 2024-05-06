#!/usr/bin/python3
"""Unittests for BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Define test cases for BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def test_attributes(self):
        """Test BaseModel attributes."""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_str(self):
        """Test __str__ method."""
        string = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), string)

    def test_save(self):
        """Test save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        self.assertEqual(type(self.model.to_dict()), dict)
        self.assertTrue('__class__' in self.model.to_dict())
        self.assertTrue('created_at' in self.model.to_dict())
        self.assertTrue('updated_at' in self.model.to_dict())

    def test_to_dict_values(self):
        """Test values in to_dict method."""
        self.assertEqual(self.model.to_dict()['__class__'], 'BaseModel')
        self.assertEqual(self.model.to_dict()['created_at'], self.model.created_at.isoformat())
        self.assertEqual(self.model.to_dict()['updated_at'], self.model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()

