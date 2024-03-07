#!/usr/bin/python3
"""

"""

import json
from models.base_model import BaseModel

class FileStorage():
    """   """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump({k: v.to_dict() if hasattr(v, 'to_dict') else v for k, v in self.__objects.items()}, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                dict = json.load(file)
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
