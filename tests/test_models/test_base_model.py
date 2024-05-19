#!/usr/bin/python3
""" tests for BASEMODEl class """
import unittest
from datetime import datetime
from models.base_model import BaseModel
import models
from unittest.mock import patch
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up the test environment"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up the test environment"""
        del self.model

    def test_init(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        data = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "name": "Test"
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, data["id"])
        self.assertEqual(model.created_at.isoformat(), data["created_at"])
        self.assertEqual(model.updated_at.isoformat(), data["updated_at"])
        self.assertEqual(model.name, data["name"])

    def test_str(self):
        """Test string representation"""
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    @patch('models.storage.save')
    def test_save(self, mock_save):
        """Test save method"""
        old_updated_at = self.model.updated_at
        # Adding a small delay to ensure the time difference
        from time import sleep
        sleep(0.1)
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(new_updated_at, old_updated_at)
        self.assertTrue(mock_save.called)

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
