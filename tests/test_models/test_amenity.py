#!/usr/bin/python3
"""" Contains tests for amenity module """


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Tests the amenity module """
    def test_is_subClass(self):
        """ tests if amenity is a subclass of BaseModel """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'name'))

    def test_str(self):
        """ tests the __str__ function """
        amenity = Amenity()

        self.assertTrue(str(amenity).startswith('[Amenity]'))
        self.assertIn(amenity.id, str(amenity))
        self.assertIn(str(amenity.__dict__), str(amenity))
