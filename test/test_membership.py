import unittest 

class TestMembership(unittest.TestCase):
    def test_in(self):
        """test_in"""
        a = ["Python", "unittest"]
        self.assertIn("Python", a)
        self.assertNotIn("Java", a)

    def test_is(self):
        """test_is"""
        a = ["Python", "unittest"]
        b = a
        self.assertIs(a, b)
        self.assertIsNot(a, ["Python", "unittest"])
    
    def test_is_not(self):
        """test_is_not"""
        a = ["Python", "unittest"]
        b = ["Python", "unittest"]
        self.assertIsNot(a, b)

if __name__ == "__main__":
    unittest.main(verbosity=2)
