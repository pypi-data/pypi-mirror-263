from calculatormp.calculator import Calculator
import unittest

class Test(unittest.TestCase):
    # Reset tests
    def test_reset1(self):
        result = Calculator.add(5)
        Calculator.reset()
        result = Calculator.add(6)
        self.assertEqual(result, 6)
    def test_reset2(self):
        result = Calculator.add(-15, 5)
        Calculator.reset()
        result = Calculator.add(42)
        self.assertEqual(result, 42)
        
if __name__ == '__main__':
    unittest.main()