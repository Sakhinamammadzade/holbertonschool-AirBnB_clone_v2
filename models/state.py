#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete", passive_deletes=True)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Getter instance method """
            all_cities = storage.all(City)
            city_list = []

            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list