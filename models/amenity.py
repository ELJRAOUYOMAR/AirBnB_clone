#!/usr/bin/python3
"""Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class.
    Attributes:
        name (str): The name of the amenity.
    """
    name = ""