import unittest
import calcs

class TestCalcs(unittest.TestCase):
#has to start with test_ !, otherwise it wont test method
#tests dont run in order
    def test_add(self):
        self.assertEqual(calcs.add(10, 5), 15)
        self.assertEqual(calcs.add(-1, 1), 0)
        self.assertEqual(calcs.add(-1, -1), -2)


    def test_subtract(self):
        self.assertEqual(calcs.subtract(10, 5), 5)
        self.assertEqual(calcs.subtract(-1, 1), -2)
        self.assertEqual(calcs.subtract(-1, -1), 0)


    def test_multiply(self):
        self.assertEqual(calcs.multiply(10, 5), 50)
        self.assertEqual(calcs.multiply(-1, 1), -1)
        self.assertEqual(calcs.multiply(-1, -1), 1)


    def test_divide(self):
        self.assertEqual(calcs.divide(10, 5), 2)
        self.assertEqual(calcs.divide(-1, 1), -1)
        self.assertEqual(calcs.divide(-1, -1), 1)
        self.assertEqual(calcs.divide(5, 2), 2.5)
        #testing exceptions
        with self.assertRaises(ValueError):
            calcs.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
