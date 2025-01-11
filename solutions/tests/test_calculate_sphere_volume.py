#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the calculate_sphere_volume function.

Test categories:
    - Standard cases: small positive numbers
    - Edge cases: 0, 1, large positive numbers
    - Defensive tests: assertions, wrong input types

Created on 11-Jan-2025

@author: Mahmoud Alnouri
"""

import unittest
from ..calculate_sphere_volume import calculate_sphere_volume


class TestCalculateSphereVolume(unittest.TestCase):
    """Test the calculate_sphere_volume function."""

    def test_zero_radius(self):
        """Test the volume of a sphere with radius 0 is 0."""
        self.assertAlmostEqual(calculate_sphere_volume(0), 0.0)

    def test_one_radius(self):
        """Test the volume of a sphere with radius 1."""
        self.assertAlmostEqual(calculate_sphere_volume(1), 4.1887902047863905)

    def test_small_positive_radius(self):
        """Test the volume of a sphere with small positive radius."""
        self.assertAlmostEqual(calculate_sphere_volume(2.5), 65.44984694978736)

    def test_large_positive_radius(self):
        """Test the volume of a sphere with a large positive radius."""
        self.assertAlmostEqual(calculate_sphere_volume(1000), 4188790204786.3905)

    def test_none_input(self):
        """Test that None input raises AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_sphere_volume(None)

    def test_negative_radius(self):
        """Test that a negative radius raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-5)

    def test_non_numeric_input(self):
        """Test that a non-numeric input raises AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_sphere_volume("radius")

    def test_list_input(self):
        """Test that a list input raises AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_sphere_volume([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
