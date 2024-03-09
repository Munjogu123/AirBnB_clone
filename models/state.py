#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines module state """


class State(BaseModel):
    """ Defines a class for the state the user is in """
    name = ''

    def __str__(self):
        """ overwrites the str function to print some elements of the class """
        return f'[State] ({self.id}) {self.__dict__}'
