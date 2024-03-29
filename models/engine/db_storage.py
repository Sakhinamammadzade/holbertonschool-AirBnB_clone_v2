#!/usr/bin/python3
"""doc"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os


env = os.environ.get('HBNB_ENV')
usr = os.environ.get('HBNB_MYSQL_USER')
pwd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, db),  pool_pre_ping=True)
       
        if env == "test":
            metadata = MetaData()
            metadata.bind = self.__engine
            metadata.drop_all()

    def all(self, cls=None):
        """doc"""
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        objects = {}
        classes = {"City": City, "State": State,
                     "User": User, "Place": Place,
                     "Review": Review, "Amenity": Amenity}
        if cls:
            if isinstance(cls, str):
                cls = classes[cls]
            for ins in self.__session.query(cls).all():
                objects["{}.{}".format(ins.__class__.__name__, ins.id)] = ins
        else:
            for classs in classes:
                for ins in self.__session.query(classes[classs]).all():                
                    objects[f"{obj.__class__.__name__}.{ins.id}"] = ins
        return objects


    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_scop = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_scop)
        self.__session = Session()




            
