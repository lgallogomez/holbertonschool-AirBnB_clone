#!/usr/bin/python3

"""
class tests Review class attributes
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime

class test_review_attributes(unittest.TestCase):
    """
    class test Review class attributes
    """
    def test_Review(self):
        new_review = Review()
        self.assertTrue(hasattr(new_review.place_id))
        self.assertTrue(hasattr(new_review.user_id))
        self.assertTrue(hasattr(new_review.text))
