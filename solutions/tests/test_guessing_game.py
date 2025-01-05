"""
Unit tests for the `guessing_game` function.

a module contains a set of unittests for the `guessing_game` function,
which compares the user's input integer to a randomly generated integer
within specified lower and upper bounds.

Classes:
    TestGuessingGame: Contains unittests for the `guessing_game` function.

Methods:
    test_input_types: Tests if the function raises
                    an AssertionError for non-integer inputs.
    test_correct_guess: Tests if the function prints "You Won!"
                    when the user's guess matches the random number.
    test_incorrect_guess: Tests if the function prints "Try Again"
                        when the user's guess does not match the random number.
    test_boundary_condition: Tests if the function works correctly for the boundary condition
                            where the lower and upper bounds are the same.

Usage:
    Run this module with a Python test runner to execute the unittests.
"""

import unittest
from unittest.mock import patch
from ..guessing_game import guessing_game


class TestGuessingGame(unittest.TestCase):
    """
    unittest used to test the function with different approaches to make sure
    the expected behavior is met


    """

    def test_input_types(self):
        """checks if the function raises an AssertionError for non-integer inputs"""
        with self.assertRaises(AssertionError):
            guessing_game("a", 5)
        with self.assertRaises(AssertionError):
            guessing_game(2, "b")

    @patch("builtins.input", side_effect=[3])
    @patch("random.randint", return_value=3)
    def test_correct_guess(self, mock_randint, mock_input):
        """checks if the function prints "You Won!"
        when the user's guess matches the random number."""
        with patch("builtins.print") as mocked_print:
            guessing_game(1, 5)
            mocked_print.assert_called_with("You Won!")

    @patch("builtins.input", side_effect=[-3])
    @patch("random.randint", return_value=-3)
    def test_negative_boundary(self, mock_randint, mock_input):
        """checks if the function prints "You Won!"
        when the user's guess matches the random number of negative boundary."""
        with patch("builtins.print") as mocked_print:
            guessing_game(-5, 5)
            mocked_print.assert_called_with("You Won!")

    @patch("builtins.input", side_effect=[2])
    @patch("random.randint", return_value=3)
    def test_incorrect_guess(self, mock_randint, mock_input):
        """checks if the function prints "Try Again"
        when the user's guess does not match the random number"""
        with patch("builtins.print") as mocked_print:
            guessing_game(1, 5)
            mocked_print.assert_called_with("Try Again")

    @patch("builtins.input", side_effect=[1])
    @patch("random.randint", return_value=1)
    def test_boundary_condition(self, mock_randint, mock_input):
        """checks if the function works correctly for the boundary
        condition where the lower and upper bounds are the same."""
        with patch("builtins.print") as mocked_print:
            guessing_game(1, 1)
            mocked_print.assert_called_with("You Won!")
