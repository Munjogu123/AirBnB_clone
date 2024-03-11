#!/usr/bin/python3
"""" Contains tests for review module """


import unittest
from models.review import Review
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Tests the review module """
    def test_is_subClass(self):
        """ tests if review is a subclass of BaseModel """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_str(self):
        """ tests the __str__ function """
        review = Review()

        self.assertTrue(str(review).startswith('[Review]'))
        self.assertIn(review.id, str(review))
        self.assertIn(str(review.__dict__), str(review))
