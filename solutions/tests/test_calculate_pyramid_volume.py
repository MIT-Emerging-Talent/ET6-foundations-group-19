#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the calculate_pyramid_volume function.

Test categories:
    - Standard cases: small positive numbers
    - Edge cases: 0, 1, large positive numbers
    - Defensive tests: assertions, wrong input types

Created on 12-Jan-2025
@author: Mahmoud Alnouri
"""

import unittest
from ..calculate_pyramid_volume import calculate_pyramid_volume


class TestCalculatePyramidVolume(unittest.TestCase):
    """Test the calculate_pyramid_volume function."""

    def test_zero_volume(self):
        """Test the volume of a pyramid with one dimension as 0 is 0."""
        self.assertAlmostEqual(calculate_pyramid_volume(0, 3, 4), 0.0)

    def test_small_positive_dimensions(self):
        """Test the volume of a pyramid with small positive dimensions."""
        self.assertAlmostEqual(calculate_pyramid_volume(2, 3, 4), 8.0)

    def test_large_positive_dimensions(self):
        """Test the volume of a pyramid with large positive dimensions."""
        self.assertAlmostEqual(calculate_pyramid_volume(100, 200, 300), 2_000_000.0)

    def test_square_base(self):
        """Test the volume of a pyramid with a square base."""
        self.assertAlmostEqual(calculate_pyramid_volume(5, 5, 5), 41.666666666666664)

    def test_negative_dimensions(self):
        """Test that negative dimensions raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_pyramid_volume(-2, 3, 4)

    def test_non_numeric_inputs(self):
        """Test that non-numeric inputs raise AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_pyramid_volume("base_length", 3, 4)

        with self.assertRaises(AssertionError):
            calculate_pyramid_volume(2, None, 4)

        with self.assertRaises(AssertionError):
            calculate_pyramid_volume(2, 3, [4])

    def test_none_input(self):
        """Test that None input raises AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_pyramid_volume(None, 3, 4)


if __name__ == "__main__":
    unittest.main()
