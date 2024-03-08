#!/usr/bin/python3
"""

class HBNBCommmand

"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """

    contains the entry point of the command interpreter

    Attributes:
        prompt
        classes:classes in module

    Methods:
        do_quit:exit
        do_EOF:exit
        do_help:show documented and undocumented commands
        do_create:create instance
        do_show:show instance based on name and id
        do_destroy:delete instance based on name and id
        do_all:print string representation of all instances
        do_update:updates an instance based on name and id

    """

    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
        }

    def do_quit(self, _):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, _):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split(" ")
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance """
        args = line.split(" ")
        b = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            if not args[1]:
                print("** instance id missing **")
            else:
                if "{}.{}".format(args[0], args[1]) not in b:
                    print("** no instance found **")
                else:
                    key = args[0] + '.' + args[1]
                    print(b[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split(" ")
        b = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            if not args[1]:
                print("** instance id missing **")
            else:
                if "{}.{}".format(args[0], args[1]) not in b:
                    print("** no instance found **")
                else:
                    key = args[0] + '.' + args[1]
                    del b[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances """
        if not line:
            b = storage.all()
            print([b[k].__str__() for k in b])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError
            b = storage.all(eval(args[0]))
            print([b[k].__str__() for k in b])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split(" ")
        b = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in b:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        c = b["{}.{}".format(args[0], args[1])]
        value = (args[3]).strip('"')        
        if hasattr(c, args[2]):
            attribute_type = type(getattr(c, args[2]))
            casted_value = attribute_type(value)
            setattr(c, args[2], casted_value)
        else:
            setattr(c, args[2], value)
        c.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
