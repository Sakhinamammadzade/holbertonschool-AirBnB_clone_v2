#!/usr/bin/python3
""" Test for DB storage """
from os import getenv
import unittest
from models.base_model import BaseModel
from models import storage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "DBStorage")
class TestDBStorage(unittest.TestCase):
    """ Test DBStorage class """

    def test_all(self):
        """ test all method """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

