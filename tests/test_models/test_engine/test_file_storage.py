#!/usr/bin/python3
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
""" contains module test_fileStorage """


class TestFileStorage(unittest.TestCase):
    """ tests all methods of FileStorage """
    def setUp(self):
        """ creates a temporary file for tests """
        self.file = 'test_file.json'

    def tearDown(self):
        """ deletes temporary file after running tests """
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_all(self):
        """ tests the all function """
        self.assertEqual(type(models.storage.all()), dict)

    def test_new(self):
        """ tests the new function """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn(f'BaseModel.{obj.id}', models.storage.all())

    def test_save_reload(self):
        """ tests the save and reload """
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        models.storage.new(obj_1)
        models.storage.new(obj_2)
        models.storage.save()

        f_storage = FileStorage()
        f_storage.reload()

        self.assertTrue(
            f_storage.all().get(f'BaseModel.{obj_1.id}') is not None)
        self.assertTrue(
            f_storage.all().get(f'BaseModel.{obj_2.id}') is not None)

    def test_save_file(self):
        """ tests if file is created and contents saved """
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()
