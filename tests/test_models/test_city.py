#!/usr/bin/python3

"""
module tests City class
"""

import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime

class test_City_Model_outputs(unittest.TestCase):
    """
    class test if City class has name & state_id attributes
    """
    def test_city(self):
        new_city = City()
        self.assertTrue(hasattr(new_city.state_id))
        self.assertTrue(hasattr(new_city.name))
