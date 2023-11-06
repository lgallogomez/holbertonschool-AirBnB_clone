#!/usr/bin/python

Storage = __import__('')
from datetime import datetime
import uuid


iso_formated_time = '%Y-%m-%dT%H:%M:%S.%f'
class BaseModel:

    def __init__(self, **kwargs):
        if kwargs:
            self.from_kwargs(**kwargs)
        else:
            self.id = str(uuid.uuid4()) 
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return(f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dicti = {}
        for key, value in vars(self).items():    
           dicti[key] = value

        dicti["__class__"] = self.__class__.__name__
        dicti["created_at"] = self.created_at.isoformat()
        dicti["updated_at"] = self.updated_at.isoformat()  
        return dicti
    
    def from_kwargs(self, **kwargs):
        for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        self.created_at = datetime.strptime(kwargs['created_at'], iso_formated_time)
        self.updated_at = datetime.strptime(kwargs['updated_at'], iso_formated_time)
