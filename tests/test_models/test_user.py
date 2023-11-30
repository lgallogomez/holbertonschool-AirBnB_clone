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
        new_user.email = "juanito@gmail.com"
        new_user_no_email = User()
        new_user_no_email.email = None
        self.assertNotEqual(new_user.email, new_user_no_email.email)
