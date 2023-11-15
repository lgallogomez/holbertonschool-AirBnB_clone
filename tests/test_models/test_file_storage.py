#!/usr/bin/python3

"""
this module test filestorage class methods
"""


import unittest

from models.engine import file_storage
from models.engine.file_storage import FileStorage

class test_file_storage(unittest.TestCase):
    """
    this class test file storage methods
    """

    def test_file_path(self):
        """
        tests if file path is created after creating
        a file storage object
        """
        new_storage = FileStorage()
        self.assertNotEqual(new_storage.__file_path, None)