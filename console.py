#!/usr/bin/python3

"""
This program contains the entry point of the command interpreter
"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

dict_of_models = {
    "BaseModel": BaseModel, 
    "User": User, 
    "Place": Place,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """
    class that inherits all cmd's methods
    """
    prompt = "(hbnb)"

    def do_create(self, model):
        '''
        creates a model & prints id
        '''
        if model not in dict_of_models and model != "":
            print("** class doesn't exist **")

        if not model:
            print("** class name missing **")

        if model in dict_of_models:
            model_instance = dict_of_models[model]()
            model_instance.save()
            return print(model_instance.id)

    def do_show(self, line):

        if not line:
            return print("** class name missing **")

        model, model_id, *args = (*line.split(), None, None)

        if not model_id:
            return print("** instance id missing **")

        if not model:
            return print("** class name missing **")

        if model not in dict_of_models:
            return print("** class doesn't exist **")

        object_key = f"{model}.{model_id}"

        if object_key not in storage.all():
            return print("** no instance found **")
        
        objects = storage.all()
        object_to_return = objects.get(object_key)
        return print(object_to_return)

    def do_destroy(self, line):
        if not line:
            return print("** class name missing **")
        
        model, model_id, *args = (*line.split(), None, None)

        if not model_id:
            return print("** instance id missing **")

        if model not in dict_of_models:
            return print("** class doesn't exist **")

        object_key = f"{model}.{model_id}"

        if object_key not in storage.all():
            return print("** no instance found **")

        objects = storage.all()
        objects.pop(object_key)
        objects = storage.save()

    def do_update(self, line):
        if not line:
            return print("** class name missing **")
        
        model, model_id, attr_name, attr_value, *args = (*line.split(), None, None, None, None)

        if model not in dict_of_models:
            return print ("** class doesn't exist **")

        if not model_id:
            return print("** instance id missing **")
        
        if not attr_name:
            return print("** attribute name missing **")
        
        if not attr_value:
            return print("** value missing **")

        object_key = f"{model}.{model_id}"

        if object_key not in storage.all():
            return print("** no instance found **")
        
        dict_of_objs = storage.all()
        instance_retrieved = dict_of_objs.get(object_key)
        instance_retrieved.__setattr__(attr_name, attr_value)  #im trying to update the value of an attribute. 
        instance_retrieved.save()
        

    def do_all(self, line):

        if not line:
            objects = storage.all()
            return print(f"{objects}")

        model_to_print, *args = (*line.split(), None)

        if model_to_print not in dict_of_models:
            return print("** class doesn't exist **")

        objects = storage.all()
        return print(f"{objects}")

    def emptyline(self):
        pass
    
    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self):
        True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
