#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods
for other classes s
"""    
import uuid
from datetime import datetime
import models

class BaseModel():
    """
    define all common attributes/methods for other classes
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
            
    def save(self) -> None:
        """
        updates the public instance attribute updated_at 
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        return a dictionary containing all keys/values
        of __dict__ of the instance:
        """

        """instance_to_dict = dict(self.__dict__)"""
        instance_to_dict = self.__dict__.copy()
        instance_to_dict["__class__"] = self.__class__.__name__
        if not isinstance(instance_to_dict["created_at"], str):
            instance_to_dict["created_at"] = instance_to_dict["created_at"].isoformat()
        if not isinstance(instance_to_dict["updated_at"], str):
            instance_to_dict["updated_at"] = instance_to_dict["updated_at"].isoformat()
        return instance_to_dict
    
    
