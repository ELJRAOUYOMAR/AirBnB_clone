#!/usr/bin/python3
"""
convert the dictionary representation to a JSON string.
JSON is a standard representation of a data structure.
With this format, humans can read and all programming languages
have a JSON reader and writer.
"""
import json 
import os

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
        id = obj.to_dict()["id"]
        class_name = obj.__class__.__name
        key_name = f"{class_name}.{id}"
        FileStorage.__objects[key_name] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) 
        exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        file_path = FileStorage.__file_path
        if os.path.exists(file_path):
            try:
                with open(file_path, encoding="utf-8") as f:
                    date = json.load(f)
            except:
                pass

