#!/usr/bin/python3
"""
this script is used to define attributes and methods
for a place
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    Attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list: it will be the
        list of Amenity.id later
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """init method for State class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)