#!/usr/bin/python3
"""
defines file storage class
"""
import json


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances
    Arguments:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
        <class name>.id (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        k = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        data = {k: obj.to_dict() for k, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path) as f:
                data = f.read()
                if not data:
                    return
                dict_obj = json.loads(data)
                for v in dict_obj.values():
                    class_name = v['__class__']
                    self.new(eval(class_name)(**v))
        except FileNotFoundError:
            return
