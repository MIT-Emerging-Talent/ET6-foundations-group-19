"""
This module contains unit tests for the calculate_square_area function.

The tests cover normal cases, boundary cases, and defensive assertions.

Created on : 15 Jan 2025
Author :Ahmed khalifa
"""

import unittest
from ..calculate_square_area import calculate_square_area


class TestCalculateSquareArea(unittest.TestCase):
    """
    A collection of unit tests for the calculate_square_area function.
    """

    def test_positive_integer_side(self):
        """
        Test the function with a positive integer side length.
        """
        self.assertEqual(calculate_square_area(5), 25.0)

    def test_positive_float_side(self):
        """
        Test the function with a positive float side length.
        """
        self.assertEqual(calculate_square_area(2.5), 6.25)

    def test_very_small_float_side(self):
        """
        Test the function with a very small float side length.
        """
        self.assertEqual(calculate_square_area(0.00000005), 0.0000000000000025)
    
    def test_large_side(self):
        """
        Test the function with a very large side length.
        """
        self.assertEqual(calculate_square_area(10000000), 10000000000000000)

    def test_zero_side(self):
        """
        Test the function with a side length of zero.
        This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            calculate_square_area(0)

    def test_negative_side(self):
        """
        Test the function with a negative side length.
        This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

    def test_non_numeric_side(self):
        """
        Test the function with a non-numeric side length.
        This should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            calculate_square_area("invalid")
