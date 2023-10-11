#!/usr/bin/python3
"""Tests for the Base class."""

from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    """Tests for the Base class."""
    
    def test_base_constructor_with_id(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

if __name__ == "__main__":
    unittest.main()
