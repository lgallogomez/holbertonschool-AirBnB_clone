#!/usr/bin/python3

"""
module creates a class Review
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    class inherits methods & attributes of basemodel & initializes it's own
    """
    place_id = str()
    user_id = str()
    text = str()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
