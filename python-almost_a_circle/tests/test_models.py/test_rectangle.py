#!/usr/bin/python3
"""Tests for the Rectangle class."""

import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_rectangle_constructor(self):
        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 20)

    def test_invalid_rectangle_width_type(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle("invalid", 20)

    def test_invalid_rectangle_width_value(self):
        with self.assertRaises(ValueError):
            rectangle_instance = Rectangle(-5, 20)

    def test_invalid_rectangle_x_type(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(10, 20, "invalid_x")

    def test_invalid_rectangle_x_value(self):
        with self.assertRaises(ValueError):
            rectangle_instance = Rectangle(10, 20, -5)

    def test_area(self):
        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(rectangle_instance.area(), 200)

    if __name__ == "__main__":
        unittest.main()

    def test_display(self):
        rectangle_instance = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rectangle_instance.display()

        output = mock_stdout.getvalue()

        self.assertEqual(output, expected_output)
