"""
Unit tests for the `extract_integers` function.

This module contains a set of unittests for the `extract_integers` function,
which extracts integers from a given input string.

Classes:
    TestExtractIntegers: Contains unittests for the `extract_integers` function.

Methods:
    test_positive_integer_in_string: Checks if the function works with
    strings containing positive integers.
    test_negative_integer_in_string: Checks if the function works with
    strings containing negative integers.
    test_string_with_no_spaces: Checks if the function works with a string that contains no spaces in between.
    test_defensive_check_if_input_argument_is_string: Ensures the function raises an error if the input argument is not a string.

Usage:
    Run this module with a Python test runner to execute the unittests.
"""

import unittest
from ..extract_integers import extract_integers


class TestExtractIntegers(unittest.TestCase):
    """
    Unit tests that check different scenarios to make sure the
    code is implemented correctly and matches the expectations of its
    behavior.
    """

    def test_positive_integer_in_string(self):
        """
        Checks if the function works with strings containing positive integers.
        """
        self.assertEqual(extract_integers("I have 3 apples"), [3])
        self.assertEqual(extract_integers("I have 3 apples and 5 bananas"), [3, 5])

    def test_negative_integer_in_string(self):
        """
        Checks if the function works with strings containing negative integers.
        """
        self.assertEqual(extract_integers("The temp is -300"), [-300])
        self.assertEqual(
            extract_integers("The table is inclined -5 degrees and the temp is -300"),
            [-5, -300],
        )

    def test_string_with_no_spaces(self):
        """
        Checks if the function works with a string that contains no spaces in between.
        """
        self.assertEqual(extract_integers("Ihave3apples"), [3])

    def test_string_with_no_integers(self):
        """
        Checks if the function works with a string that contains no spaces in between.
        """
        self.assertEqual(extract_integers("I like apples"), [])

    def test_defensive_check_if_input_argument_is_string(self):
        """
        Ensures the function raises an error if the input argument is not a string.
        """
        with self.assertRaises(AssertionError):
            extract_integers(123)
