#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
>>>>>>> 4d7c2a3c7c21a1669bc53b99b54169c35bc3e731
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
<<<<<<< HEAD
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', cascade='all, delete', backref='cities')
=======
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    # One2many relationship to places
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
>>>>>>> 4d7c2a3c7c21a1669bc53b99b54169c35bc3e731
