from calculatormp.calculator import Calculator
import unittest

class Test(unittest.TestCase):
    # Multiplication tests
    def test_multiply1(self):
        result = Calculator.multiply(5, 3)
        self.assertEqual(result, 15)
    def test_multiply2(self):
        result = Calculator.multiply(-15, 5)
        self.assertEqual(result, -75)
    def test_multiply3(self):
        result = Calculator.multiply(6.66, 17.8975)
        self.assertEqual(result, 119.19735000000001)
    def test_multiply4(self):
        Calculator.reset()
        result = Calculator.multiply(100)
        self.assertEqual(result, 0)
    def test_multiply5(self):
        Calculator.reset()
        result = Calculator.multiply(5, 3)
        result = Calculator.multiply(100)
        self.assertEqual(result, 1500)
        
if __name__ == '__main__':
    unittest.main()