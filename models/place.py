#!/usr/bin/python3

"""
module initializes a state class that inherits attributes from BaseModel
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    class creates an Place
    """
    city_id = str()
    user_id = str()
    name = str()
    description = str()
    number_rooms = 0
    number_bathrooms = 0
    max_guest = float(0.0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = list()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
