#!/usr/bin/python3
"""Declaring the BaseModel class that defines all common attributes/methods
   for other classes."""

from uuid import uuid4
from datetime import datetime
import models import storage


class BaseModel:
    """Represent the BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel.

        Args:
            *args (any): Unused
            **kwargs (dict): Attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'
                        )
                    else:
                        self.__dict__[key] = value
                else:
                    self.id = str(uuid4())
                    self.created_at = datetime.today()

        if not kwargs or "__class__" not in kwargs:
            storage.new(self)

    def __str__(self):
        """Prints in stdout string representation of the BaseModel"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates public instance attribute updated_at
           with current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Returns dictionary containing all keys/values of
           __dict__ of the instance"""
        final_dict = self.__dict__.copy()
        final_dict["__class__"] = self.__class__.__name__
        final_dict["created_at"] = self.created_at.isoformat()
        final_dict["updated_at"] = self.updated_at.isoformat()
        return final_dict
