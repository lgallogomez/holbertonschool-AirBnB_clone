#!/usr/bin/python3

"""
module test State class
"""

import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime

class test_State_Model_outputs(unittest.TestCase):
    """
    test methods in State class
    """
    def test_state(self):
        new_state = State()
        self.assertTrue(hasattr(new_state.name))