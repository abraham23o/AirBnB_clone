#!/usr/bin/python3
"""
this script is used to define attributes and methods
for a state
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    State class
    Attributes:
        name: string - empty string
    """
    name = ''
