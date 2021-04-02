import unittest
import Arithmetic

class ArithmeticTest(unittest.TestCase):
    def setUp(self):
        self.arithmetic = Arithmetic.Arithmetic(10, 5)

    def test_addition(self):
        self.assertEqual(self.arithmetic.addition(), 15)

    def test_subtraction(self):
        self.assertEqual(self.arithmetic.subtraction(), 5)

    def test_multiplication(self):
        self.assertEqual(self.arithmetic.multiplication(), 50)

    def test_divisionTest(self):
        self.assertEqual(self.arithmetic.division(), 2)

if __name__ == '__main__':
    unittest.main()
