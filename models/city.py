#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Base.sqlalchemy.Column(Base.sqlalchemy.String(60),
                                      Base.sqlalchemy.ForeignKey('states.id'),
                                      nullable=False)
    name = Base.sqlalchemy.Column(Base.sqlalchemy.String(128), nullable=False)
