#!/usr/bin/python

from datetime import datetime
from models import storage
import uuid

class BaseModel:
    '''
    class defines common methods for other classes
    '''

    
    def __init__(self, *args, **kwargs):
        '''
        if intance args receives a dict, makes dict an obj
        if not, creates object & stores in dict of objects using storage.new
        '''
        
        
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4()) 
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    def __str__(self):
        return(f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dicti = {}
        for key, value in vars(self).items():    
           dicti[key] = value

        dicti["__class__"] = self.__class__.__name__
        dicti["created_at"] = self.created_at.isoformat()
        dicti["updated_at"] = self.updated_at.isoformat()  
        return dicti
