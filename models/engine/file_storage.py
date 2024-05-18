#!/usr/bin/python3
"""
convert the dictionary representation to a JSON string.
JSON is a standard representation of a data structure.
With this format, humans can read and all programming languages
have a JSON reader and writer.
"""
import json 
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    serializes instances to a JSON file 
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        class_name_of_obj = obj.__class__.__name__
        key_name = "{}.{}".format(class_name_of_obj, obj.id)
        FileStorage.__objects[key_name] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        objs = FileStorage.__objects
        dict_obj = {}

        for obj in objs.keys():
            dict_obj[obj] = objs[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(dict_obj, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) 
        exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised))
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                try:
                    dict_obj = json.load(f)

                    for key, value in dict_obj.items():
                        class_name, obj_id = key.split('.')
                        class_type = eval(class_name)
                        instance = class_type(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

