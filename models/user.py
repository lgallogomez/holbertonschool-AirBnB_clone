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
    email = str()
    password = str()
    first_name = str()
    last_name = str()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
