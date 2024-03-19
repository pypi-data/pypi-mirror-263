from calculatormp.calculator import Calculator
import unittest

class Test(unittest.TestCase):
    # Root tests
    def test_root1(self):
        result = Calculator.root(16, 2)
        self.assertEqual(result, 4.0)
    def test_root2(self):
        result = Calculator.root(81, 4)
        self.assertEqual(result, 3.0)
    def test_root3(self):
        result = Calculator.root(100, 5)
        self.assertEqual(result, 2.51188643150958)
    def test_root4(self):
        Calculator.reset()
        with self.assertRaises(ValueError):
            Calculator.root(0)
    def test_root5(self):
        Calculator.reset()
        with self.assertRaises(ValueError):
            Calculator.root(16, 0)
    def test_root6(self):
        Calculator.reset()
        with self.assertRaises(ValueError):
            Calculator.root(-16, 2)
    def test_root7(self):
        Calculator.reset()
        result = Calculator.root(81, 2)
        result = Calculator.root(2)
        self.assertEqual(result, 3)
        
if __name__ == '__main__':
    unittest.main()