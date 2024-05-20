#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.reload()

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all method of FileStorage."""
        all_objs = self.storage.all()
        self.assertEqual(type(all_objs), dict)
        self.assertEqual(len(all_objs), 0)

    def test_new(self):
        """Test new method of FileStorage."""
        my_model = BaseModel()
        self.storage.new(my_model)
        all_objs = self.storage.all()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], my_model)

    def test_save(self):
        """Test save method of FileStorage."""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test reload method of FileStorage."""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].id, my_model.id)

if __name__ == "__main__":
    unittest.main()
