#!/usr/bin/python3
"""

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
