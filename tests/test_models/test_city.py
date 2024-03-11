#!/usr/bin/python3
"""" Contains tests for city module """


import unittest
from models.city import City
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Tests the city module """
    def test_is_subClass(self):
        """ tests if city is a subclass of BaseModel """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_str(self):
        """ tests the __str__ function """
        city = City()

        self.assertTrue(str(city).startswith('[City]'))
        self.assertIn(city.id, str(city))
        self.assertIn(str(city.__dict__), str(city))
