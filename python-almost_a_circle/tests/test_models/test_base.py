#!/usr/bin/python3
"""Tests for the Base class."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def testBaseConstructorWithId(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)


if __name__ == "__main__":
    unittest.main()
