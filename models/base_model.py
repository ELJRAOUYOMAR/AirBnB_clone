#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods
for other classes
"""    
from uuid import uuid4


class BaseModel():
    """
    define all common attributes/methods for other classes
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
