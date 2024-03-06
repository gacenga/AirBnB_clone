#!/usr/bin/python3
'''
Class BaseModel

'''

import uuid
from datetime import datetime

class BaseModel():
    '''
    class BaseModel
    '''
    def __init__(self, *args, **kwargs):
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, DATE_TIME_FORMAT)
                elif key[0] == 'id':
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            from models import storage
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
            storage.new(self)
    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        class_name = self.__class__.__name__
        return {'__class__':class_name, **instance_dict}
