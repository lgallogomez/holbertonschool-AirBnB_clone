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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = str()
        self.password = str()
        self.first_name = str()
        self.last_name = str()