"""
A simple module to print 'Hello, World!'.

Author: Tamara Saqer
Date: 2025-01-12
"""


def print_hello_world() -> str:
    """
    Return the string 'Hello, World!'.

    Returns:
        str: The string 'Hello, World!'.

    Examples:
        >>> print_hello_world()
        'Hello, World!'
    """
    return "Hello, World!"


if __name__ == "__main__":
    import doctest

    # Run doctests to validate the function
    doctest.testmod()
