import unittest
from main import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.plus(15,4), 19)

    def test_subtract(self):
        self.assertEqual(self.calculator.minus(17,3), 14)

    def test_multiply(self):
        self.assertEqual(self.calculator.mltpl(15,5), 75)

    def test_divide(self):
        self.assertEqual(self.calculator.div(32,4), 8)

if __name__ == "__main__":
    unittest.main()
