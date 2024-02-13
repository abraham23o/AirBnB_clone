#!/usr/bin/python3
"""
this script is used to define attributes and methods
for a city
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    City class
    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
