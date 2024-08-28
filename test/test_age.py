import unittest
from src.age import catgorize_age

class TestAge(unittest.TestCase):
    def test_child(self):
        """test child"""
        self.assertEqual(catgorize_age(0), 'child')
        self.assertEqual(catgorize_age(17), 'child')
    def test_adult(self):
        """test adult"""
        self.assertEqual(catgorize_age(18), 'adult')
        self.assertEqual(catgorize_age(64), 'adult')
    def test_senior(self):
        """test senior"""
        self.assertEqual(catgorize_age(70), 'senior')
        self.assertEqual(catgorize_age(100), 'senior')

if __name__ == '__main__':
    unittest.main(verbosity=2)