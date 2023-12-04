#!/usr/bin/python3


"""
this module tests the class user methods
"""


import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class Test_User_Model_outputs(unittest.TestCase):
    '''
    tests methods in User class
    '''

    def test_email(self):
        new_user = User()
        new_user.email = ""
        self.assertTrue(hasattr(User, "email"))
    
    def test_password(self):
        new_user = User()
        new_user.password = ""
        self.assertTrue(hasattr(User, "password"))
    
    def test_first_name(self):
        new_user = User()
        new_user.first_name = ""
        self.assertTrue(hasattr(User, "first_name"))
        
    def test_last_name(self):
        new_user = User()
        new_user.last_name = ""    
        self.assertTrue(hasattr(User, "last_name"))
