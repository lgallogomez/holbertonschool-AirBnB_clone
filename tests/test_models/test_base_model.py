#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    def test_save(self):
        new_object = BaseModel()
        new_object.save()
        self.assertNotEqual(new_object.updated_at, new_object.created_at)

if __name__ == "__main__":
    unittest.main()