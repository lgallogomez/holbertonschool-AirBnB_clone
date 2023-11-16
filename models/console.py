#!/usr/bin/python3

"""
This program contains the entry point of the command interpreter
"""

import cmd, sys

class HBNBCommand(cmd.Cmd):
    """
    class that inherits all cmd's methods
    """
    
    prompt = "(hbnb) "
    
    def emptyline(self):
        pass
    
    def do_quit(self):
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
