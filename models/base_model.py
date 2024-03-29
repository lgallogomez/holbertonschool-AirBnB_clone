#!/usr/bin/python


"""
this module defines a class that defines methods and
attributes for other classes
"""


from datetime import datetime
from models import storage
import uuid


iso_formated_time = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """
    class defines common methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        if intance args receives a dict, makes dict an obj
        if not, creates object & stores in dict of objects using storage.new
        """
        if kwargs:
            self.from_kwargs(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        defines and returns the format to print
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates object attribute updated_at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        takes an basemodel object and transforms into dictionary
        """
        dicti = {}
        for key, value in vars(self).items():
            dicti[key] = value
        dicti["__class__"] = type(self).__name__
        dicti["created_at"] = self.created_at.isoformat()
        dicti["updated_at"] = self.updated_at.isoformat()
        return dicti

    def from_kwargs(self, **kwargs):
        """
        creates an instance from a dictionary
        """
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
        self.created_at = datetime.strptime(kwargs['created_at'], iso_formated_time)
        self.updated_at = datetime.strptime(kwargs['updated_at'], iso_formated_time)
