#!/usr/bin/python3
"""Declaring class FileStorage that serializes instances 
   to a JSON file and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Represent a FileStorage.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of objects.
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__
        self.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as file:
            obj_dict = {
                "{}.{}".format(obj.__class__.__name__, obj.id): obj.to_dict()
                for obj in self.__objects.values()
            }
            json.dump(obj_dict, file, default=str)

    def reload(self):
        """Deserializes the JSON file to __objects 
           (only if the JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path) as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
