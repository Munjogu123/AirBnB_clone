#!/usr/bin/python3
import unittest
import datetime
from models.base_model import BaseModel
""" contains module test_base_model """


class TestBaseModel(unittest.TestCase):
    """ creates test for all methods in BaseModel """
    def test_init(self):
        """ tests initialization of BaseModel class """
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertIsNotNone(bm1.id)
        self.assertIsNotNone(bm1.created_at)
        self.assertIsNotNone(bm1.updated_at)

        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm2, BaseModel)
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)

        self.assertIsInstance(bm1.created_at, datetime.datetime)
        self.assertIsInstance(bm2.created_at, datetime.datetime)

        self.assertIsInstance(bm1.updated_at, datetime.datetime)
        self.assertIsInstance(bm2.updated_at, datetime.datetime)

    def test_str(self):
        """ tests the __str__ function """
        bm1 = BaseModel()

        self.assertTrue(str(bm1).startswith('[BaseModel]'))
        self.assertIn(bm1.id, str(bm1))
        self.assertIn(str(bm1.__dict__), str(bm1))

    def test_save(self):
        """ checks if updated at changes when save function is called """
        bm1 = BaseModel()
        bm1.save()

        self.assertNotEqual(bm1.created_at, bm1.updated_at)

    def test_to_dict(self):
        """ tests the to_dict function """
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()

        self.assertIsInstance(bm1_dict, dict)
        self.assertEqual(bm1_dict['__class__'], 'BaseModel')
        self.assertEqual(bm1_dict['id'], bm1.id)
        self.assertEqual(bm1_dict['created_at'], bm1.created_at.isoformat())
        self.assertEqual(bm1_dict['updated_at'], bm1.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
