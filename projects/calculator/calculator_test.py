import unittest
from projects.calculator.calculator import Calculator

class TestOK(unittest.TestCase):
    def test_sum(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 1), 2)

class TestNotOK(unittest.TestCase):
    def test_sum(self):
        calculator = Calculator()
        self.assertNotEqual(calculator.add(1, 1), 3)


if __name__ == '__main__':
    unittest.main()