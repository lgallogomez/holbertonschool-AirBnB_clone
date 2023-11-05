#!/usr/bin/python

from datetime import datetime
import uuid

class Base_Model:

    def __init__(self):
        self.id = str(uuid.uuid4()) 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return(f"{__class__.__name__} ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = self.updated_at.now()

    def to_dict(self):
        dicti = {}
        for key, value in vars(self).items():    
           dicti[key] = value
        dicti["__class__"]: __class__.__name__
        dicti["created_at"]: self.created_at.isoformat()
        dicti["updated_at"]: self.updated_at.isoformat()  
        return dicti
