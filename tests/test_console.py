import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User

class TestHBNBCommand(unittest.TestCase):
    
    def setUp(self):
        """Sets up the test environment."""
        storage.reset()  # Assuming you have a method to clear storage

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            output = f.getvalue()
            self.assertEqual(output, "")

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            output = f.getvalue()
            self.assertEqual(output, "")

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            output = f.getvalue()
            self.assertEqual(output, "")

    def test_create_missing_class(self):
        """Test create command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create command with valid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertTrue(user_id in storage.all().keys())

    def test_show_missing_class(self):
        """Test show command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing id."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show command with invalid id."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_valid(self):
        """Test show command with valid class name and id."""
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user.id}")
            self.assertIn(user.id, f.getvalue().strip())

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing id."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid id."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_valid(self):
        """Test destroy command with valid class name and id."""
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user.id}")
            self.assertNotIn(user.id, storage.all().keys())

    def test_all_invalid_class(self):
        """Test all command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_all_valid_class(self):
        """Test all command with valid class name."""
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertIn(user.id, f.getvalue().strip())