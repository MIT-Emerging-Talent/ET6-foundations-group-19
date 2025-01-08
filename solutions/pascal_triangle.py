#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating mathematical sequences.

Module contents:
    - prime_list: generates a list of prime numbers up to a given limit.
    - factorial_list: generates a list of factorials up to a given number.
    - pascals_triangle: generates Pascal's Triangle up to a given number of rows.

Created on Jan 3, 2025
@author: Dadi Ishimwe
"""


def pascals_triangle(rows: int) -> list[list[int]]:
    """Generates Pascal's Triangle up to a given number of rows.

    Parameters:
        rows: int, the number of rows to generate.

    Returns:
        list[list[int]]: A list of lists representing Pascal's Triangle.

    Raises:
        AssertionError: if the argument is not a non-negative integer.

    >>> pascals_triangle(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> pascals_triangle(1)
    [[1]]
    >>> pascals_triangle(0)
    []
    """
    assert isinstance(rows, int) and rows >= 0, "Rows must be a non-negative integer."
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
