#!/usr/bin/python3
"""
this script is used to define attributes and methods
for a user
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    a class User that inherits from BaseModel
    Attributes:
        email (str): Public class attribute for User's email
        password (str): Public class attribute for User's password
        first_name (str): Public class attribute for User's first name
        last_name (str): Public class attribute for User's last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
