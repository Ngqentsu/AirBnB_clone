#!/usr/bin/python3
"""Declaring Review class that inherits from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review.

       Attributes:
                 place_id (str): Place id
                 user_id (str): User id
                 text (str): Text in the review
    """
    place_id = ""
    user_id = ""
    text = ""
