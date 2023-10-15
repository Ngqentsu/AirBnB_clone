#!/usr/bin/python3
"""Declaring State class that inherit from BaseModel."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent a State

       Attributes:
                 name (str): State name.
    """
    name = ""
