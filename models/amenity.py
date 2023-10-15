#!/usr/bin/python3
"""Amenity class that inherit from BaseModel."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent Anemity.

       Attributes:
                 name(str) = anemity name
    """
    name = ""
