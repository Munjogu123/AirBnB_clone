#!/usr/bin/python3
from models.base_model import BaseModel
""" Contains module user """


class User(BaseModel):
    """ Defines class for user information """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
