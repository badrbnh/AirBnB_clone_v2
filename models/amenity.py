#!/usr/bin/python3
"""'Amenity' class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """represents an Amenity for a MySQL database
    inherits from the SQLAlchemy Base and links to the MySQL table amenities
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity',
                                       back_populates="amenities")
    else:
        name = ""
