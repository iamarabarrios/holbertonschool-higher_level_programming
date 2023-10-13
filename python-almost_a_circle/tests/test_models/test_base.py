#!/usr/bin/python3
"""Tests for the Base class."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def testBaseConstructorWithId(self):
        """Test constructor."""
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)


if __name__ == "__main__":
    unittest.main()

    def testToJSONString(self):
        """test to json string."""
        data = [{"id": 1, "name": "Object1"}, {"id": 2, "name": "Object2"}]
        json_str = Base.to_json_string(data)
        expected_json = (
            '[{"id": 1, "name": "Object1"}, {"id": 2, "name": "Object2"}]'
        )
        self.assertEqual(json_str, expected_json)
