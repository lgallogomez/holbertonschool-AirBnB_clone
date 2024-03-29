#!/usr/bin/python3

"""
this module test filestorage class methods
"""


import unittest

from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class test_file_storage(unittest.TestCase):
    """
    this class test file storage methods
    """

    def test_all(self):
        """
        tests if method returns a dict of objects
        """
        new_storage = storage.all()
        self.assertNotEqual(new_storage, {})
    
    def test_objects(self):
        new_obj = BaseModel()
        new_storage = FileStorage()
        self.assertNotEquals(new_storage, [])