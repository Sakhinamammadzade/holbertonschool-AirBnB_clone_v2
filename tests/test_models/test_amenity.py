#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.amenity1 = Amenity(name="Wi-fi")

    def test_name2(self):
        """ """
        self.assertEqual(type(self.amenity1.name), str)
