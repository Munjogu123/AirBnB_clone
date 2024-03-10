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
