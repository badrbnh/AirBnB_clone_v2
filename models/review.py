#!/usr/bin/python3
"""'Review' class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel, Base):
    """represents a review class for a MySQL database
    inherits from the SQLAlchemy 'Base' and links to the MySQL table reviews
    """
    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(Text(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
