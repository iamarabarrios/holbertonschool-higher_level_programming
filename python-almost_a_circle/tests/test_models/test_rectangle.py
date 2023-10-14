#!/usr/bin/python3
"""Tests for the Rectangle class."""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_rectangle_constructor(self):
        """Try the constructor of class rectangle."""
        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 20)

    def test_invalid_rectangle_width_type(self):
        """Try if work the TypeError."""
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle("invalid", 20)

    def test_invalid_rectangle_width_value(self):
        """Try if work the ValueError."""
        with self.assertRaises(ValueError):
            rectangle_instance = Rectangle(-5, 20)

    def test_invalid_rectangle_x_type(self):
        """Try if work the TypeError."""
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(10, 20, "invalid_x")

    def test_invalid_rectangle_x_value(self):
        """Try if work the ValueError."""
        with self.assertRaises(ValueError):
            rectangle_instance = Rectangle(10, 20, -5)

    def test_area(self):
        """Try the method area."""
        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(rectangle_instance.area(), 200)

    if __name__ == "__main__":
        unittest.main()

    def test_display(self):
        """Try methd display."""
        rectangle_instance = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rectangle_instance.display()

        output = mock_stdout.getvalue()

        self.assertEqual(output, expected_output)

    def test_str(self):
        """Try str method."""
        rectangle_instance = Rectangle(4, 3, 1, 2, 5)
        expected_str = "[Rectangle] (5) 1/2 - 4/3"
        self.assertEqual(str(rectangle_instance), expected_str)

    def test_to_dictionary_method(self):
        """Test dictionary."""
        rectangle = Rectangle(4, 3, 1, 2, 5)
        rectangle_dict = rectangle.to_dictionary()
        expected_dict = {"id": 5, "width": 4, "height": 3, "x": 1, "y": 2}
        self.assertEqual(rectangle_dict, expected_dict)
