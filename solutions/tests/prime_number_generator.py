#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Test module for generating a list of prime numbers up to a given limit.
    
Created on Jan 3, 2025
@author: Dadi Ishimwe
"""

def prime_list(limit: int) -> list[int]:
    """Generates a list of prime numbers up to a given limit.
    
    Parameters:
        limit: int, the upper limit (inclusive) for prime numbers.

    Returns:
        list[int]: A list of prime numbers less than or equal to the limit.

    Raises:
        AssertionError: if the argument is not a positive integer.

    >>> prime_list(10)
    [2, 3, 5, 7]
    >>> prime_list(1)
    []
    >>> prime_list(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    assert isinstance(limit, int) and limit >= 0, "Limit must be a non-negative integer."
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes