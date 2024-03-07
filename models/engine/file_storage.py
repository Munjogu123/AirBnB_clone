#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
""" creates a module file_storage """


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key """
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        new_obj = {}

        for key in self.__objects:
            new_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(new_obj, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)

            for key, value in data.items():
                class_name = key.split('.')[0]
                cls = eval(class_name)
                self.__objects[key] = cls(**value)
