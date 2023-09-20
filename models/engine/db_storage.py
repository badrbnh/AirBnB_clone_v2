#!/usr/bin/python3

"""this module represts the DB stroage engine for AirBnB clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """this class handles storage of hbnb models in DB"""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage constructor"""
        # create engine
        self.__engine = create_engine('sql+mysql://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        # drop all tables if the environment variable HBNB_ENV is equal to test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        # create a dictionary of objects from a given class name
        classes = {'State': State, 'City': City, 'User': User,
                   'Place': Place, 'Review': Review, 'Amenity': Amenity}
        objs = {}
        if cls is not None:
            query = self.__session.query(classes[cls]).all()
            for obj in query:
                key = obj.__class__.__name__ + '.' + obj.id
                objs[key] = obj
        else:
            for key, value in classes.items():
                query = self.__session.query(value).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs[key] = obj
        return objs

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """save all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload the data"""
        # create all tables in the database (feature of SQLAlchemy)
        Base.metadata.create_all(self.__engine)
        # create a session
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        session = scoped_session(session_maker)
