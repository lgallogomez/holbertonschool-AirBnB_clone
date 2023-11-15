#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    '''
    tests method in BaseModel class
    '''
    
    def test_save(self):
        '''
        tests the save method in BaseModel class, where updated_at attribute
        updates itself everytime the object/instance is saved
        '''
        new_object = BaseModel()
        new_object.save()
        first_save = new_object.updated_at
        new_object.save()
        second_save = new_object.updated_at
        self.assertNotEqual(first_save, second_save)
   
    def test_to_dict(self):
        new_object = BaseModel()
        new_dict = new_object.to_dict()
        self.assertIs(type(new_dict), dict)
        self.assertIsNot(new_dict, new_object)
        
    def test_str(self):
        new_object = BaseModel()
        printed_obj = f'{new_object}'
        sec_obj = BaseModel()
        second_obj = f'{sec_obj}'
        self.assertIs(type(printed_obj), str)
        self.assertIs(len(printed_obj), len(second_obj) )

        
if __name__ == "__main__":
    unittest.main()