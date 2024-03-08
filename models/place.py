#!/usr/bin/python3
"""

class Place:inherits from class BaseModel

"""

from models.base_model import BaseModel
import json

class Place(BaseModel):
    """

    class Place

    Attributes:
        city_id:empty string
        user_id:empty string
        name:empty string
        description:empty string
        number_rooms:initialized to 0
        number_bathrooms:initialized to 0
        max_guest:initialized to 0
        price_by_night::initialized to 0
        latitude::initialized to 0
        longitude::initialized to 0
        amenity_ids:empty list

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
