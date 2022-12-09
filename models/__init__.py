#!/usr/bin/python3
<<<<<<< HEAD
"""Create a unique storage instance for your application"""

from os import environ
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""check envirn var to determine storage method"""
if environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    """file storage selected"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
=======
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
>>>>>>> 4d7c2a3c7c21a1669bc53b99b54169c35bc3e731
