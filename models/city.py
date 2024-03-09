#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines module city """


class City(BaseModel):
    """ Defines a class for the city a user is in """
    state_id = ''
    name = ''

    def __str__(self):
        """ overwrites the str function to print some elements of the class """
        return f'[City] ({self.id}) {self.__dict__}'
