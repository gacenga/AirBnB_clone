#!/usr/bin/python3
"""

class Review:inherits from class BaseModel

"""

from models.base_model import BaseModel
import json

class Review(BaseModel):
    """

    class Review

    Attributes:
        place_id:empty string
        user_id:empty string
        text:empty string

    """
    place_id = ""
    user_id = ""
    text = ""
