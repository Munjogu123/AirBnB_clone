#!/usr/bin/python3
import uuid
from datetime import datetime
import models
""" contains module base_model """


class BaseModel:
    """ Superclass for all other classes """
    def __init__(self, *args, **kwargs):
        """ Initialization of BaseModel """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                if key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ overwrites the str function to print some elements of the class """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__

        for key, value in new_dict.items():
            if key == 'created_at':
                new_dict[key] = new_dict[key].isoformat()
            if key == 'updated_at':
                new_dict[key] = new_dict[key].isoformat()

        return new_dict
