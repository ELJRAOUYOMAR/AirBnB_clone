#!/usr/bin/python3
""" City tests"""


import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up the test environment"""
        self.city = City()

    def tearDown(self):
        """Clean up the test environment"""
        del self.city

    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test the attributes of City"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_to_dict(self):
        """Test the to_dict method of City"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        self.assertEqual(city_dict["created_at"], self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], self.city.updated_at.isoformat())

    def test_str(self):
        """Test the string representation of City"""
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_save(self):
        """Test the save method of City"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)


if __name__ == '__main__':
    unittest.main()
