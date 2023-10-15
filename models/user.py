#!/usr/bin/python3
"""Declaring the User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User:
    """Represent a User.

       Attributes:
                 email (str): User email
                 password (str): User password
                 first_name (str): User name
                 last_name: User surname
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
