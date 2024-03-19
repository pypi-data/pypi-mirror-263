from calculatormp.calculator import Calculator
import unittest

class Test(unittest.TestCase):
    # Division tests
    def test_divide1(self):
        result = Calculator.divide(5, 3)
        self.assertEqual(result, 1.6666666666666667)
    def test_divide2(self):
        result = Calculator.divide(-15, 5)
        self.assertEqual(result, -3.0)
    def test_divide3(self):
        result = Calculator.divide(6.66, 17.8975)
        self.assertEqual(result, 0.37211901103506073)
    def test_divide4(self):
        Calculator.reset()
        result = Calculator.divide(100)
        self.assertEqual(result, 0)
    def test_divide5(self):
        Calculator.reset()
        with self.assertRaises(ValueError):
            Calculator.divide(0)
    def test_divide6(self):
        Calculator.reset()
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)
    def test_divide7(self):
        Calculator.reset()
        result = Calculator.divide(500, 100)
        result = Calculator.divide(5)
        self.assertEqual(result, 1)
        
if __name__ == '__main__':
    unittest.main()