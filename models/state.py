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

    def __init__(self, *args, **kwargs):
        """init method for State class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
