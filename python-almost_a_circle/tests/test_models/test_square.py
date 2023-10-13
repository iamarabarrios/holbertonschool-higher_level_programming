import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    def test_inheritance(self):
        square = Square(5)
        self.assertIsInstance(square, Square)
        self.assertIsInstance(square, Rectangle)

    def test_initialization(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            square = Square("invalid")
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_update(self):
        square = Square(3, 1, 2)
        square.update(4, 5, 6, 7)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_to_dictionary(self):
        square = Square(3, 1, 2, 4)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {"id": 4, "size": 3, "x": 1, "y": 2})

    def test_size_property(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 7
        self.assertEqual(square.size, 7)


if __name__ == "__main__":
    unittest.main()
