#!/usr/bin/python3

"""
module initializes a state class that inherits attributes from BaseModel
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    class creates an state
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
