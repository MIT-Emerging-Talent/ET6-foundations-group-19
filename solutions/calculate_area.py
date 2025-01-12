"""
This module provides a function to calculate the area of a square.

The function takes the length of a side as input and returns the area.
Created on 12 Jan 2025
Author: Ahmed Khalifa
"""


def calculate_square_area(side_length: float) -> float:
    """
    Calculate the area of a square given the length of its side.

    Parameters:
        side_length (float): The length of the side of the square. Must be a positive number.

    Returns:
        float: The area of the square, calculated as side_length ** 2.

    Raises:
        ValueError: If the side_length is not a positive number.

    Examples:
        >>> calculate_square_area(5)
        25.0
        >>> calculate_square_area(2.5)
        6.25
        >>> calculate_square_area(30)
        900.0

    """
    # Defensive assertion
    assert isinstance(side_length, (int, float))
    if side_length <= 0:
        raise ValueError("side_length must be a positive number.")

    # Calculate and return the area
    return side_length**2
