from calculatormp.calculator import Calculator
import unittest

class Test(unittest.TestCase):
    # Addition tests
    def test_add1(self):
        result = Calculator.add(5, 3)
        self.assertEqual(result, 8)
    def test_add2(self):
        result = Calculator.add(-15, 5)
        self.assertEqual(result, -10)
    def test_add3(self):
        result = Calculator.add(6.66, 17.8975)
        self.assertEqual(result, 24.5575)
    def test_add4(self):
        Calculator.reset()
        result = Calculator.add(100)
        self.assertEqual(result, 100)
    def test_add5(self):
        Calculator.reset()
        result = Calculator.add(100)
        result = Calculator.add(500)
        self.assertEqual(result, 600)
        
if __name__ == '__main__':
    unittest.main()