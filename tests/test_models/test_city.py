#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.city1 = City(state_id="d80e0345-67eb-434a-b1e0-07783522124e",
                          name="Albuquerque")

    def test_state_id(self):
        """ """
        self.assertEqual(type(self.city1.state_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.city1.name), str)
