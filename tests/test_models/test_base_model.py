#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    def test_save(self):
        new_object = BaseModel()
        new_object.save()
        before_save = new_object.created_at
        after_save = new_object.updated_at
        self.assertNotEqual(before_save, after_save)

   
if __name__ == "__main__":
    unittest.main()