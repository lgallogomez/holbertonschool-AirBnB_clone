#!/usr/bin/python3

"""
Module defines user class. Inherits 
BaseModel attributes and methods
"""

from models.base_model import BaseModel
class User(BaseModel):
    """
    Class inherits from BaseModel 
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
