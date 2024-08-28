import unittest

from src.shape import Shape
from src.circle import Circle
from src.square import Square

class TestShape(unittest.TestCase):
    def test_circle(self):
        """test circle"""
        circle = Circle(5)
        self.assertIsInstance(circle, Shape)
        self.assertEqual(circle.name, "Circle")
        self.assertEqual(int(circle.area()), 78)

    def test_square(self):
        """test square"""
        square = Square(5)
        self.assertIsInstance(square, Shape)
        self.assertEqual(square.name, "Square")
        self.assertEqual(square.area(), 25)

if __name__ == "__main__":
    unittest.main(verbosity=2)
