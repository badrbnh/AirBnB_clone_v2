#!/usr/bin/python3
"""Defines the DBStorage engine."""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError, OperationalError
from os import getenv
from models.base_model import Base


class DBStorage:
    """database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """queries current database session for all objects of a given class
        If cls is None, queries all types of objects
        returns:
            dictionary of queried classes, format: <class name>.<obj id> = obj
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """adds object to the database session"""
        self.__session.add(obj)

    def save(self):
        """saves all the changes to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes object from the database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all the tables in database and initializes a new session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """calls remove() method on the private session attribute"""
        self.__session.close()
