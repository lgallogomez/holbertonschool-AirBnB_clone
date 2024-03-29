#!/usr/bin/python3

"""
module creates a class City
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    class inherits methods & attributes of basemodel & initializes it's own
    """
    state_id = str()
    name = str()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
