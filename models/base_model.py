#!/usr/bin/python

from datetime import datetime
import uuid

class Base_Model:

    def __init__(self):
        self.id = uuid.uuid4() 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return(f"{__class__.__name__} ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = self.updated_at.now()

    def to_dict(self):
        obj_dict = {
            "__class__": self.__dict__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
        return(obj_dict)

mi_clase = Base_Model()
mi_clase.name = "My first model"
mi_clase.mynumber = 89

mi_clase.save()
print(mi_clase)
mi_clase.save()
print("-----")
print(mi_clase)

