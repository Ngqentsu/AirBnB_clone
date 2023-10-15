#!/usr/bin/python3
"""Declaring a Place class that inherits from BaseModel."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a Place.

       Attributes:
                 city_id (str): City id
                 user_id (str): User id
                 name (str): Name of the place
                 description (str): Description of the place
                 number_rooms (int): Number of rooms in the place
                 number_bathrooms (int): Number of bathrooms in the place
                 max_guest (int): Max number of guests to acommodate
                 price_by_night (int): Price to pay per night
                 latitude (float): The latitude of the place
                 longitude (float): The longitude of the place
                 amenity_ids (list): A list of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
