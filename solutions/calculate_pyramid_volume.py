#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the volume of a pyramid.

Created on 12-Jan-2025
@author: Mahmoud Alnouri
"""


def calculate_pyramid_volume(
    base_length: float, base_width: float, height: float
) -> float:
    """Calculate the volume of a pyramid given its base dimensions and height.

    Parameters:
        base_length: float, The length of the pyramid's base. Must be a non-negative number.
        base_width: float, The width of the pyramid's base. Must be a non-negative number.
        height: float, The height of the pyramid. Must be a non-negative number.

    Returns -> float, The volume of the pyramid.

    Raises:
        AssertionError: If any argument is not a float or int.
        ValueError: If any dimension is less than 0.

    Examples:
    >>> calculate_pyramid_volume(2, 3, 4)
    8.0

    >>> calculate_pyramid_volume(0, 3, 4)
    0.0

    >>> calculate_pyramid_volume(5, 5, 5)
    41.666666666666664
    """
    # Validate input types
    assert all(
        isinstance(i, (int, float)) for i in (base_length, base_width, height)
    ), "All inputs must be numbers (int or float)."

    # Validate input values
    if base_length < 0 or base_width < 0 or height < 0:
        raise ValueError("Base dimensions and height cannot be negative.")

    # Formula for the volume of a pyramid: (1/3) * base_area * height
    base_area = base_length * base_width
    return (1 / 3) * base_area * height


if __name__ == "__main__":
    # Interactive testing
    try:
        base_length = float(input("Enter the base length of the pyramid: "))
        base_width = float(input("Enter the base width of the pyramid: "))
        height = float(input("Enter the height of the pyramid: "))
        volume = calculate_pyramid_volume(base_length, base_width, height)
        print(f"The volume of the pyramid is {volume:.2f}")
    except (AssertionError, ValueError) as e:
        print(f"Error: {e}")
