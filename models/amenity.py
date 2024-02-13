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
