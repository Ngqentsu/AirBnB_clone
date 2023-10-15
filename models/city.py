#!/usr/bin/python3
"""City class that inherit from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City.

       Attributes:
                 state_id (str): State id
                 name (str): Name of the city
    """
    state_id = ""
    name = ""
