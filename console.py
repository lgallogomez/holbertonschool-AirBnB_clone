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
            return("** class name missing **")

        model, model_id, *args = (*line.split(), None, None)

        if not model_id:
            return("** instance id missing **")

        if not model:
            return("** class name missing **")

        if model not in list_of_models:
            return("** class doesn't exist **")

        object_key = f"{model}.{model_id}"

        if object_key not in storage.all():
            return print("** no instance found **")

    def emptyline(self):
        pass
    
    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self):
        True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
