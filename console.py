#!/usr/bin/python3

"""
This program contains the entry point of the command interpreter
"""

import cmd, sys
from models.base_model import BaseModel
from models import engine

class HBNBCommand(cmd.Cmd):
    """
    class that inherits all cmd's methods
    """
    prompt = "(hbnb)"

    def do_create(self, model):
        if model:
            model = BaseModel()
            model.save()
            print(model.id)
        else:
            print("** class name missing **")
    def emptyline(self):
        pass
    
    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self):
        True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
