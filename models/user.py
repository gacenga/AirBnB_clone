#!/usr/bin/python3
"""

class User:inherits from class BaseModel

"""

from models.base_model import BaseModel
import json

class User(BaseModel):
    """

    class User

    Attributes:
        email:empty string
        password:empty string
        first_name:empty string
        last_name:empty string

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
