#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines module review """


class Review(BaseModel):
    """ Defines a class for user reviews """
    place_id = ''
    user_id = ''
    text = ''
