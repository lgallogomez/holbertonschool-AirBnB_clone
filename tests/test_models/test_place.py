#!/usr/bin/python3

"""
class tests Place class attributes
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime

class test_place_attributes(unittest.TestCase):
    """
    class test Place class attributes
    """
    def test_Place(self):
        new_place = Place()
        self.assertTrue(hasattr(new_place.name))
