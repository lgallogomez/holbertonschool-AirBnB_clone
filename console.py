#!/usr/bin/python3

"""
This program contains the entry point of the command interpreter
"""

import cmd, sys
from models.base_model import BaseModel
from models import storage

list_of_models = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    """
    class that inherits all cmd's methods
    """
    prompt = "(hbnb)"

    def do_create(self, model):
        '''
        creates a model & prints id
        '''
        if model != "BaseModel" and model != "":
            print("** class doesn't exist **")
        elif (model == "BaseModel"):
            model = BaseModel()
            model.save()
            print(model.id)
        elif not model:
            print("** class name missing **")

    def do_show(self, line):

        if not line:
            print("** class name missing **")
            return

        model, model_id, *other_args = (line.split(), None, None)

        if not model_id:
            return print("** instance id missing **")

        if not model:
            return print("** class name missing **")

        if model not in list_of_models:
            return print("** class doesn't exist **")

        object_key = f"{model}.{model_id}"

        if object_key not in storage.all():
            return print("** no instance found **")
            
        print(storage.all()[object_key])

    def emptyline(self):
        pass
    
    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self):
        True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
