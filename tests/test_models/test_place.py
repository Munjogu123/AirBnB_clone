#!/usr/bin/python3
"""" Contains tests for place module """


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Tests the place module """
    def test_is_subClass(self):
        """ tests if place is a subclass of BaseModel """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_str(self):
        """ tests the __str__ function """
        place = Place()

        self.assertTrue(str(place).startswith('[Place]'))
        self.assertIn(place.id, str(place))
        self.assertIn(str(place.__dict__), str(place))
