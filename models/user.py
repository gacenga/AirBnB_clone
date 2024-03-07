#!/usr/bin/python3
"""

"""

from models.base_model import BaseModel
import json

class User(BaseModel):
    """ """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
