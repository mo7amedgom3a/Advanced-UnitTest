import unittest
from src.calculator import *

class TestCalculator(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skip(self):
        """test skip"""
        self.assertTrue(False)
    
    @unittest.skipIf(1 == 1, "skip if")
    def test_skip_if(self):
        """test skip if"""
        self.assertTrue(False)

    @unittest.skipUnless(1 == 1, "skip unless")
    def test_skip_unless(self):
        """test skip unless"""
        self.assertTrue(True)
    
    def test_add(self):
        """test add"""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 1), 1)

    def test_subtract(self):
        """test subtract"""
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(0, 1), -1)
    
    def test_multiply(self):
        """test multiply"""
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(0, 1), 0)
    
    def test_divide(self):
        """test divide"""
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(0, 1), 0)
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)