from calculatormp.calculator import Calculator
import unittest

class Test(unittest.TestCase):
    # Subtraction tests
    def test_subtract1(self):
        result = Calculator.subtract(5, 3)
        self.assertEqual(result, 2)
    def test_substract2(self):
        result = Calculator.subtract(-15, 5)
        self.assertEqual(result, -20)
    def test_substract3(self):
        result = Calculator.subtract(6.66, 17.8975)
        self.assertEqual(result, -11.2375)
    def test_substract4(self):
        Calculator.reset()
        result = Calculator.subtract(100)
        self.assertEqual(result, -100)
    def test_substract5(self):
        Calculator.reset()
        result = Calculator.subtract(100)
        result = Calculator.subtract(500)
        self.assertEqual(result, -600)
        
if __name__ == '__main__':
    unittest.main()