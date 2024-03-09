#!/usr/bin/python3
"""

Class FileStorage

"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """

    serializes instances to a JSON file and
     deserializes JSON file to instances

    Attributes:
        file_path: path to the JSON file
        objects:dictionary - empty but will store all objects

    Methods:
        all(self, cls=None):
            returns the dictionary __objects
        new(self, obj):
            sets in __objects the obj with key <obj class name>.id
        save(self):
            serializes __objects to the JSON file (path: __file_path)
        reload(self):
            deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Parameters:
            cls:class instance
        returns the dictionary __objects
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """

        sets in __objects the obj with key <obj class name>.id

        Parameters:
            obj:value
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """

        serializes __objects to the JSON file

        """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(
                {
                    k: v.to_dict() if hasattr(v, 'to_dict') else v
                    for k, v in self.__objects.items()
                },
                file
            )

    def reload(self):
        """

        deserializes the JSON file to __objects

        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                dict = json.load(file)
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
