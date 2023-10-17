#!/usr/bin/python3
"""Class HBNBCommand(cmd.Cmd) that has entry point of command interpreter."""

import cmd
import json
import re
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def character(arg):
    curly_brackets = re.search(r"\{(.*?)\}", arg)
    square_brackets = re.search(r"\[(.*?)\]", arg)
    round_brackets = re.search(r"\((.*?)\)", arg)
    if curly_brackets is None:
        if square_brackets is None:
            if round_brackets is None:
                return [char.strip(",") for char in split(arg)]
            else:
                char_tok = split(arg[:round_brackets.span()[0]])
                com_tok = [c.strip(",") for c in char_tok]
                com_tok.append(round_brackets.group())
                return com_tok
        else:
            char_tok = split(arg[:square_brackets.span()[0]])
            com_tok = [c.strip(",") for c in char_tok]
            com_tok.append(square_brackets.group())
            return com_tok
    else:
        char_tok = split(arg[:curly_brackets.span()[0]])
        com_tok = [c.strip(",") for c in char_tok]
        com_tok.append(curly_brackets.group())
        return com_tok


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command interpreter."""

    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

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

    def default(self, arg):
        """Handle specified commands and invalid input."""
        arg_dict = {
            "show": self.do_show,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "update": self.do_update,
            "count": self.do_count
        }
        valid = re.search(r"\.", arg)
        if valid is not None:
            arg_tok = [arg[:valid.span()[0]], arg[valid.span()[1]:]]
            valid = re.search(r"\((.*?)\)", arg_tok[1])
            if valid is not None:
                cmd = [arg_tok[0], valid.group()[1:-1]]
                if cmd[0] in arg_dict.keys():
                    call = "{} {}".format(arg_tok[0], cmd[1])
                    return arg_dict[cmd[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
           (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            print(new_instance.id)
            storage.new(new_instance)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
           based on the class name and id.
        """
        arg_list = character(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(arg_list[0], arg_list[1])
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[instance_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
           (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(arg.split()[0], arg.split()[1])
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[instance_key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
           or not on the class name.
        """
        obj_list = []
        arg_list = character(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                class_name, instance_id = key.split('.')
                if len(arg_list) > 0 and arg_list[0] == class_name:
                    obj_list.append(str(value))
                elif len(arg_list) == 0:
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
           adding or updating attribute (save the change into the JSON file).

           Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[obj_key]
            attribute_name = args[2]
            attribute_value = args[3]

            if attribute_name in obj.__dict__:
                attribute_type = type(obj.__dict__[attribute_name])
                obj.__dict__[attribute_name] = attribute_type(attribute_value)
            else:
                print("** attribute name missing **")
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
