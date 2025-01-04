#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A test for module calculate_factorial.

Test categories:
    - Standard cases: small positive numbers 
    - Edge cases: 0, 1, large positive numbers
    - Defensive tests: assertions, wrong input types

Created on 4 1 2025

@author: Ahmed Hussein
"""

import unittest

from ..calculate_factorial import calculate_factorial


class TestCalculateFactorial(unittest.TestCase):
    """Test the calculate_factorial function"""

    def test_zero_factorial(self):
        """Test the factorial of 0 is 1"""
        self.assertEqual(calculate_factorial(0), 1)

    def test_one_factorial(self):
        """Test the factorial of 1 is 1"""
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_small_positive_number(self):
        """Test the factorial of 1 is 1"""
        self.assertEqual(calculate_factorial(2), 2)

    def test_test_positive_number(self):
        """Test the factorial of 5 is 120"""
        self.assertEqual(calculate_factorial(5), 120)
    
    def test_two_digits_number(self):
        """Test the factorial of 10 is 3628800"""
        self.assertEqual(calculate_factorial(10), 3628800)
    
    def test_two_digits_number2(self):
        """Test the factorial of 42 is 1405006117752879898543142606244511569936384000000000"""
        self.assertEqual(calculate_factorial(42), 1405006117752879898543142606244511569936384000000000)

    def test_three_digits_number(self):
        """Test the factorial of 112 is 197450685722107402353682037275992488341277868034975337796656295094902858969771811440894224355027779366597957338237853638272334919686385621811850780464277094400000000000000000000000000"""
        self.assertEqual(calculate_factorial(112), 197450685722107402353682037275992488341277868034975337796656295094902858969771811440894224355027779366597957338237853638272334919686385621811850780464277094400000000000000000000000000)

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            calculate_factorial(None)

    def test_non_integer_input(self):
        """It should raise AssertionError for non-integer input"""
        with self.assertRaises(AssertionError):
            calculate_factorial("FaCtOrIaL")

    def test_ngative_number(self):
        """It should raise ValueError for negative integer"""
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
