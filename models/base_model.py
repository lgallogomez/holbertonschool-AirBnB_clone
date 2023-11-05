#!/usr/bin/python

from datetime import datetime
import uuid

class BaseModel:

    def __init__(self, **kwargs):
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


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model_json = my_model.to_dict()
print(my_model_json)
print("----")
new_model = BaseModel(**my_model_json)
print(new_model)
print(new_model.id)
print(new_model)
print(type(new_model.created_at))

print("--")
print(my_model is new_model)