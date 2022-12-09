#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
<<<<<<< HEAD


class Amenity(BaseModel, Base):
    """This is the class for Amenity Attributes"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # place_amenities = relationship('Place', secondary='place_amenity')
=======
import models


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary='place_amenity')
>>>>>>> 4d7c2a3c7c21a1669bc53b99b54169c35bc3e731
