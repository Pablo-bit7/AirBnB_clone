#!/usr/bin/python3
"""
Module for testing the User class.
"""
import unittest
from datetime import datetime
from models.user import User
from models import storage


class TestUserInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the User class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_different_created_at(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        user1 = User()
        user1.id = "777777"
        user1.created_at = user1.updated_at = my_date
        user_str = str(user1)
        self.assertIn("[User] (777777)", user_str)
        self.assertIn("'id': '777777'", user_str)
        self.assertIn("'created_at': {}".format(repr(my_date)), user_str)
        self.assertIn("'updated_at': {}".format(repr(my_date)), user_str)

    def test_args_unused(self):
        user1 = User(None)
        self.assertNotIn(None, user1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        user1 = User(id="777", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(user1.id, "777")
        self.assertEqual(user1.created_at, my_date)
        self.assertEqual(user1.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    def test_save(self):
        user = User()
        user.save()
        user_id = "User." + user.id
        self.assertIn(user_id, storage.all())

    def test_save_updates_updated_at(self):
        user = User()
        first_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(first_updated_at, user.updated_at)


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)


if __name__ == "__main__":
    unittest.main()
