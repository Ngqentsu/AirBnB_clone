#!/usr/bin/python3
"""Class HBNBCommand(cmd.Cmd) that has entry point of command interpreter."""

import cmd
import json
from models.base_model import BaseModel
from models import storage
from shlex import split


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
           (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.__classes[arg]()
            models.storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
           based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(arg.split()[0], arg.split()[1])
            if instance_key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[instance_key])

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
            if instance_key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[instance_key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
           or not on the class name.
        """
        obj_list = []
        if arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                class_name, instance_id = key.split('.')
                if not arg or arg == class_name or \
                        arg == value.__class__.__name__:
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
        elif "{}.{}".format(args[0], args[1]) not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            obj = models.storage.all()[obj_key]
            attribute_name = args[2]
            attribute_value = args[3]

            if attribute_name in obj.__class__.__dict__:
                attribute_type = type(obj.__class__.__dict__[attribute_name])
                obj.__dict__[attribute_name] = attribute_type(attribute_value)
            else:
                print("** attribute doesn't exist **")
            models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
