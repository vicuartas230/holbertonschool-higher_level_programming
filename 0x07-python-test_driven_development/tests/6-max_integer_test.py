#!/usr/bin/python3
""" This program is used to test all
    posible special cases for the function
    max_integer """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class to test the function max_integer
        with the module unittest """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        with self.assertRaises(TypeError):
            max_integer([0, 'a', 5])
        self.assertEqual(max_integer([5, 5, 5]), 5)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([2.36, 2.361, 2.362]), 2.362)
        self.assertEqual(max_integer([-1, -900, -3,]), -1)
        self.assertEqual(max_integer([1000, 5e4, -3000, 5000]), 5e4)
        self.assertEqual(max_integer([]), None)

if __name__ == '__name__':
    unittest.main()
