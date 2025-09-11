#!/usr/bin/python3
"""
Unit tests for the max_integer function.
"""
import unittest
from os import path
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test the max_integer function.
    """

    def test_positive_numbers(self):
        """
        Test a list of positive integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
        self.assertEqual(max_integer([10, 50, 20]), 50)

    def test_negative_numbers(self):
        """
        Test a list of negative integers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -50, -20]), -10)

    def test_mixed_numbers(self):
        """
        Test a list of mixed positive and negative numbers.
        """
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)
        self.assertEqual(max_integer([10, -5, 0, 3]), 10)

    def test_single_element(self):
        """
        Test a list with a single element.
        """
        self.assertEqual(max_integer([99]), 99)

    def test_empty_list(self):
        """
        Test an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_duplicate_max(self):
        """
        Test a list where the max is repeated.
        """
        self.assertEqual(max_integer([10, 5, 10, 2]), 10)

    def test_floats(self):
        """
        Test a list of floats.
        """
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)
        self.assertEqual(max_integer([1.5, 2, 0.5]), 2)
        self.assertEqual(max_integer([-1.5, -2, -0.5]), -0.5)

    def test_invalid_type(self):
        """
        Test a list with an invalid element type (string).
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, "hello"])

    def test_no_args(self):
        """
        Test calling the function with no arguments.
        """
        with self.assertRaises(TypeError):
            max_integer()
