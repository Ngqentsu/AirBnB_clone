#!/usr/bin/python3
"""Class HBNBCommand(cmd.Cmd) that has entry point of command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """An empty line does not execute anything"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
