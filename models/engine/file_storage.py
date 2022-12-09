#!/usr/bin/python3v
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """Returns a dictionary of models currently in storage"""
        if cls:
            """filter the objects by class"""
            return {k: v for k, v in self.__objects.items() if
                    isinstance(v, cls)}
        return self.__objects
=======
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        d = {}

        if not cls:
            return self.__objects

        d = {key: value for key, value in self.__objects.items()
             if type(value) == cls}

        return d
>>>>>>> 4d7c2a3c7c21a1669bc53b99b54169c35bc3e731

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
<<<<<<< HEAD
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__,obj.id)
            if key in self.__objects:
                del self.__objects[key]
=======
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)
>>>>>>> 4d7c2a3c7c21a1669bc53b99b54169c35bc3e731

    def reload(self):
        """ deserialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """ specific storage """
        self.reload()

    def delete(self, obj=None):
        """ Delete obj if its inside """
        if not obj:
            return

        k = "{}.{}".format(type(obj).__name__, obj.id)

        if k in self.__objects:
            del self.__objects[k]
            self.save()
