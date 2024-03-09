#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines module place """


class Place(BaseModel):
    """ Defines the place the AirBnB is located """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __str__(self):
        """ overwrites the str function to print some elements of the class """
        return f'[Place] ({self.id}) {self.__dict__}'
