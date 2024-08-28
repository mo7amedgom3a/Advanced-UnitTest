import unittest

class TestCollections(unittest.TestCase):
    def test_list_identity(self):
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3, 4, 5]
        ## assertListEqual() and assertEqual() are equivalent
        self.assertListEqual(a, b)
        self.assertEqual(a, b)

    def test_sequence(self):
        a = ("H", "e", "l", "l", "o")
        b = "Hello"
        self.assertSequenceEqual(a, b)
        ## assertEqual() will fail
        ## self.assertEqual(a, b)

    def test_set(self):
        a = {1, 2, 3, 4, 5}
        b = {5, 4, 3, 2, 1}
        self.assertSetEqual(a, b)
    def test_dict(self):
        a = {"name": "Alice", "age": 25}
        b = {"age": 25, "name": "Alice"}
        self.assertDictEqual(a, b)

    def test_tuple(self):
        a = (1, 2, 3, 4, 5)
        b = (1, 2, 3, 4, 5)
        self.assertTupleEqual(a, b)
        self.assertEqual(a, b)

    def tets_string(self):
        a = "Hello"
        b = "Hello"
        self.assertMultiLineEqual(a, b)
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main(verbosity=2)
