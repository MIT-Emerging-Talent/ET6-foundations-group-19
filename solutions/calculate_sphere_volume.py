#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the volume of a sphere

Created on 11-Jan-2025
@author: Mahmoud Alnouri
"""

from math import pi


def calculate_sphere_volume(radius: float) -> float:
    """Calculate the volume of a sphere given its radius.

    Parameters:
        radius: float, The radius of the sphere. Must be a non-negative number.

    Returns -> float, The volume of the sphere.

    Raises:
        AssertionError: If the argument is not a float or int.
        ValueError: If the radius is less than 0.

    Examples:
    >>> calculate_sphere_volume(1)
    4.1887902047863905

    >>> calculate_sphere_volume(0)
    0.0

    >>> calculate_sphere_volume(2.5)
    65.44984694978736

    >>> calculate_sphere_volume(10)
    4188.790204786391
    """
    # Validate the input type
    assert isinstance(radius, (int, float)), "Radius must be a number (int or float)."

    # Validate the radius value
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    # Formula for the volume of a sphere: (4/3) * π * r^3
    return (4 / 3) * pi * (radius**3)


if __name__ == "__main__":
    # Interactive testing
    try:
        radius_input = float(input("Enter the radius of the sphere: "))
        volume = calculate_sphere_volume(radius_input)
        print(f"The volume of the sphere with radius {radius_input} is {volume:.2f}")
    except (AssertionError, ValueError) as e:
        print(f"Error: {e}")
