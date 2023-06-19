#!/usr/bin/python3

"""
Unit tests for the max_integer function.

This module contains test cases for the max_integer function
from the '6-max_integer' module. It tests various scenarios
to ensure the correct behavior of the max_integer function.
"""

import unittest
from importlib import import_module

max_integer = import_module('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """
    Test case class for testing the max_integer function.
    """

    def test_empty_list(self):
        """
        Test the max_integer function with an empty list.
        The expected result is None.
        """

        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """
        Test the max_integer function with a list containing a single element.
        The expected result is the same single element.
        """

        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """
        Test the max_integer function with a list of positive numbers.
        The expected result is the maximum number from the list.
        """

        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """
        Test the max_integer function with a list of negative numbers.
        The expected result is the maximum number from the list.
        """

        result = max_integer([-5, -4, -3, -2, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """
        Test the max_integer function with a list of mixed positive
        and negative numbers.
        The expected result is the maximum number from the list.
        """

        result = max_integer([-5, 0, 5, -10, 10])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        """
        Test the max_integer function with a list of duplicate numbers.
        The expected result is the same duplicate number.
        """

        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_max_in_the_middle(self):
        """Test the max_integer function with a list of where the max
        number in the middle of the list
        The expected result is the middle number which is the max"""
        result = max_integer([1, 2, 5, 3, 4])
        self.assertEqual(result, 5)

    def test_large_list(self):
        """
        Test the max_integer function with a large list of numbers.
        The expected result is the maximum number from the list.
        """

        result = max_integer(list(range(1000000, 0, -1)))
        self.assertEqual(result, 1000000)


if __name__ == '__main__':
    unittest.main()
