#!/usr/bin/python3
"""Unittests for BaseModel class with dictionary representation."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    """Define test cases for BaseModel with dictionary representation."""

    def test_init_kwargs(self):
        """Test __init__ method with kwargs."""
        kwargs = {
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            'updated_at': '2017-09-28T21:03:54.052302',
            'my_number': 89,
            'name': 'My_First_Model'
        }
        my_model = BaseModel(**kwargs)
        self.assertEqual(my_model.id, kwargs['id'])
        self.assertEqual(my_model.created_at.isoformat(), kwargs['created_at'])
        self.assertEqual(my_model.updated_at.isoformat(), kwargs['updated_at'])
        self.assertEqual(my_model.my_number, kwargs['my_number'])
        self.assertEqual(my_model.name, kwargs['name'])

    def test_init_empty_kwargs(self):
        """Test __init__ method with empty kwargs."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_init_extra_kwargs(self):
        """Test __init__ method with extra kwargs."""
        kwargs = {
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            'updated_at': '2017-09-28T21:03:54.052302',
            'my_number': 89,
            'name': 'My_First_Model',
            'extra_attr': 'Extra Attribute'
        }
        my_model = BaseModel(**kwargs)
        print(dir(my_model))
        self.assertFalse(hasattr(my_model, 'extra_attr'))


if __name__ == "__main__":
    unittest.main()
