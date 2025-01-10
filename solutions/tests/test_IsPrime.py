#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A test for module is_prime.

Test categories:
    - Standard cases: small prime numbers, small non-prime numbers
    - Edge cases: 0, 1, and negative numbers
    - Defensive tests: assertions, wrong input types

Created on 10-Jan-2025

@author: Mahmoud Alnouri
"""

import unittest

from ..is_prime import is_prime


class TestIsPrime(unittest.TestCase):
    """Test the is_prime function"""

    def test_zero(self):
        """Test that 0 is not a prime number"""
        self.assertFalse(is_prime(0))

    def test_one(self):
        """Test that 1 is not a prime number"""
        self.assertFalse(is_prime(1))

    def test_two(self):
        """Test that 2 is a prime number"""
        self.assertTrue(is_prime(2))

    def test_small_prime(self):
        """Test that 7 is a prime number"""
        self.assertTrue(is_prime(7))

    def test_small_non_prime(self):
        """Test that 9 is not a prime number"""
        self.assertFalse(is_prime(9))

    def test_large_prime(self):
        """Test that 7919 is a prime number"""
        self.assertTrue(is_prime(7919))

    def test_large_non_prime(self):
        """Test that 7920 is not a prime number"""
        self.assertFalse(is_prime(7920))

    def test_negative_number(self):
        """Test that negative numbers are not prime"""
        self.assertFalse(is_prime(-7))

    def test_non_integer_input(self):
        """It should raise AssertionError for non-integer input"""
        with self.assertRaises(AssertionError):
            is_prime("PrimeTest")

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            is_prime(None)


if __name__ == "__main__":
    unittest.main()
