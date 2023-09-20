#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Base.sqlalchemy.Column(Base.sqlalchemy.String(128), nullable=False)
    cities = Base.sqlalchemy.relationship("City", cascade="all, delete",
                                          backref="state")
    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances"""
        from models import storage
        from models.city import City
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
