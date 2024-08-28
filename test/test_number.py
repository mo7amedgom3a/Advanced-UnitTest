import unittest
from parameterized import parameterized
from src.check_number import * 

class TestNumber(unittest.TestCase):
    def test_is_even(self):
        """test_is_even"""
        for number in [2, 4, 6, 8, 10]:
            with self.subTest(number=number):
                self.assertIsInstance(number, int)
                self.assertTrue(is_even(number))
        self.assertFalse(is_even(1))
        with self.assertRaises(TypeError):
            is_even("1")
    
    @parameterized.expand([
        (2, True),
        (4, True),
        (6, True),
        (8, True),
        (10, True),
        (1, False),
        (3, False),
        (5, False),
        (7, False),
        (9, False),
    ])
    def test_is_even_parameterized(self, number, expected):
        """test_is_even_parameterized"""
        self.assertEqual(is_even(number), expected)
    
    """
    @parameterized.parameterized.expand([])
    this equivalent to calling the function without any arguments 10 times
    """
    
    def test_invalid_input(self):
        """test_invalid_input"""

        with self.assertRaises(ValueError):
            is_even(0)

    @parameterized.expand([
        (1, True),
        (3, True),
        (5, True),
        (7, True),
        (9, True),
        (2, False),
        (4, False),
        (6, False),
        (8, False),
        (10, False),
    ])
    def test_is_odd_parameterized(self, number, expected):
        """test_is_odd_parameterized"""
        self.assertEqual(is_odd(number), expected)

    def test_is_odd(self):
        """test_is_odd"""
        for number in [1, 3, 5, 7, 9]:
            with self.subTest(number=number):
                self.assertTrue(is_odd(number))


if __name__ == '__main__':
    unittest.main(verbosity=2)