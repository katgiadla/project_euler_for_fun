import unittest
from Multiply_Problem import *

class MyTestCase(unittest.TestCase):
    def test_create_multiply_loop_not_to_max_value(self):
        self.assertEqual(Multiply_Problem.create_multiply(2, 7), {2, 4, 6})

    def test_create_multiply_loop_to_max_value(self):
        self.assertEqual(Multiply_Problem.create_multiply(2, 8), {2, 4, 6, 8})

    def test_create_multiply_zero_factor(self):
        self.assertRaises(ValueError, Multiply_Problem.create_multiply, 0, 7)

    def test_create_multiply_zero_max_value(self):
        self.assertRaises(ValueError, Multiply_Problem.create_multiply, 1, 0)

    def test_create_multiply_equal_factor_max_value(self):
        self.assertEqual(Multiply_Problem.create_multiply(1, 1), {1})

if __name__ == '__main__':
    unittest.main()