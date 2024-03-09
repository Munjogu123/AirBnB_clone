#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines module amenity """


class Amenity(BaseModel):
    """ Defines a class for amenities """
    name = ''

    def __str__(self):
        """ overwrites the str function to print some elements of the class """
        return f'[Amenity] ({self.id}) {self.__dict__}'
