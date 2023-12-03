#!/usr/bin/python3

"""
class tests Amenity class attributes
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime

class test_amenity_attributes(unittest.TestCase):
    """
    class test Amenity class attributes
    """
    def test_Amenity(self):
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, "name"))
