#!/usr/bin/python3

"""
class creates an amenity
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    class inherits methods & attributes from BaseModel
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = str()
