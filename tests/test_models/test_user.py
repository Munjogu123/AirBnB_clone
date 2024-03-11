#!/usr/bin/python3
"""" Contains tests for user module """


import unittest
from models.user import User
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Tests the user module """
    def test_is_subClass(self):
        """ tests if user is a subclass of BaseModel """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_str(self):
        """ tests the __str__ function """
        user = User()

        self.assertTrue(str(user).startswith('[User]'))
        self.assertIn(user.id, str(user))
        self.assertIn(str(user.__dict__), str(user))
