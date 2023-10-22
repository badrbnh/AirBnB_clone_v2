#!/usr/bin/python3
"""New engine DBStorage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base


class DBStorage:
    """ class definition """

    __engine = None
    __session = None

    def __init__(self):
        """public isnatnce method"""
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        db_url = f"mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}"
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all classes or specific one"""
        allClasses = [User, State, City, Place, Amenity, Review]
        result = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                ClassName = obj.__class__.__name__
                keyName = ClassName + "." + obj.id
                result[keyName] = obj
            else:
                for clss in allClasses:
                    for obj in self.__session.query(clss).all():
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + obj.id
                        result[keyName] = obj
            return result

    def new(self, obj):
        """add new obj"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload data """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """call the remove function"""
        self.__session.close()
