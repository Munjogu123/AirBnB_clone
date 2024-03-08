#!/usr/bin/python3
from models.base_model import BaseModel
""" Contains module user """


class User(BaseModel):
    """ Defines class for user information """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __str__(self):
        """ overwrites the str function to print some elements of the class """
        return f'[User] ({self.id}) {self.__dict__}'
