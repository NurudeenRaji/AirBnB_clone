#!/usr/bin/python3
""" Place test for State class """
from models.place import Place
import unittest
import os
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ Place class unit tests """

    def setUp(self):
        """ Creating an object of the class """
        self.my_model = Place()

    def tearDown(self):
        """ Method to clean up """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type(self):
        """ Testing the tye of attribute """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.name, str)
        self.assertIsInstance(self.my_model.city_id, str)
        self.assertIsInstance(self.my_model.user_id, str)
        self.assertIsInstance(self.my_model.description, str)
        self.assertIsInstance(self.my_model.number_rooms, int)
        self.assertIsInstance(self.my_model.number_bathrooms, int)
        self.assertIsInstance(self.my_model.max_guest, int)
        self.assertIsInstance(self.my_model.price_by_night, int)
        self.assertIsInstance(self.my_model.latitude, float)
        self.assertIsInstance(self.my_model.longitude, float)
        self.assertIsInstance(self.my_model.amenity_ids, list)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
