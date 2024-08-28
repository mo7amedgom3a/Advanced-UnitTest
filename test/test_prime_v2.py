import unittest

def is_prime(n):
    if type(n) != int:
        raise TypeError("Input must be an integer")
    if n <= 1:
        raise ValueError("Input must be greater than 1")
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(17))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(10))

    def test_invalid_type_float(self):
        with self.assertRaises(TypeError):
            is_prime(4.5)

    def test_invalid_type_str(self):
        with self.assertRaises(TypeError):
            is_prime("5")

    def test_zero_and_one(self):
        with self.assertRaises(ValueError):
            is_prime(0)
        with self.assertRaises(ValueError):
            is_prime(1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            is_prime(-1)

if __name__ == "__main__":
    unittest.main(verbosity=2)