#!/usr/bin/python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_attribute_type(self):
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

if __name__ == '__main__':
    unittest.main()
