#!/usr/bin/python3
"""
this script is used to define attributes and methods
for an amenity
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class
    Attributes:
        name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method for State class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
