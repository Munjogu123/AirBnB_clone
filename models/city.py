#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines module city """


class City(BaseModel):
    """ Defines a class for the city a user is in """
    state_id = ''
    name = ''
