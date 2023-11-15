#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    '''
    tests methods in BaseModel class
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
        '''
        test checks if dictionary is created from 
        instance and if is not a n empty dictionary 
        '''
        new_object = BaseModel()
        new_dict = new_object.to_dict()
        empty_dict = {}
        self.assertIs(type(new_dict), dict)
        self.assertIsNot(new_dict, new_object)
        self.assertNotEqual(new_dict, empty_dict)
        
    def test_str(self):
        '''
        test checks if str prints what its designed to
        and not a random text
        '''
        new_object = BaseModel()
        printed_obj = f'{new_object}'
        sec_obj = BaseModel()
        second_obj = f'{sec_obj}'
        self.assertIs(type(printed_obj), str)
        self.assertIs(len(printed_obj), len(second_obj))
        self.assertNotEqual(printed_obj, "Fake")

        
if __name__ == "__main__":
    unittest.main()