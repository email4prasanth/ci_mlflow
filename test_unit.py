import unittest
from example import add

class TestMathFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10,20),30)
        self.assertEqual(add(1,2),3)

if __name__ == "__main__":
    unittest.main()