#!/usr/bin/python3

"""
module initializes a state class that inherits attributes from BaseModel
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    class creates an Place
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = str()
        self.user_id = str()
        self.name = ""
        self.description = str()
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = float(0.0)
        self.latitude = float(0.0)
        self.longitude = float(0.0)
        self.amenity_ids = list()

