#!/usr/bin/python3
"""" Contains tests for state module """


import unittest
from models.state import State
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Tests the state module """
    def test_is_subClass(self):
        """ tests if state is a subclass of BaseModel """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, 'name'))

    def test_str(self):
        """ tests the __str__ function """
        state = State()

        self.assertTrue(str(state).startswith('[State]'))
        self.assertIn(state.id, str(state))
        self.assertIn(str(state.__dict__), str(state))
