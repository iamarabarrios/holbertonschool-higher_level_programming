#!/usr/bin/python3
"""Tests."""


from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    """Tests base."""
    def test_base_constructor_with_id(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

class TestRectangle(unittest.TestCase):
    """Test rectangle."""
    def test_rectangle_constructor(self):
        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 20)

