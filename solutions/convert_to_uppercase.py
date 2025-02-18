"""
A module to convert all characters in a string from lowercase to uppercase.

Author: Tamara Saqer
Date: 2025-01-10
"""


def convert_to_uppercase(input_string: str) -> str:
    """
    Convert all characters in a string from lowercase to uppercase.

    Args:
        input_string (str): The string to be converted. Must be a valid string.

    Returns:
        str: A new string with all characters converted to uppercase.

    Raises:
        ValueError: If the input is not a string.

    Examples:
        >>> convert_to_uppercase("hello world")
        'HELLO WORLD'
        >>> convert_to_uppercase("Python")
        'PYTHON'
        >>> convert_to_uppercase("")
        ''
    """
    # Check if the input is a string
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")

    # Convert the string to uppercase
    return input_string.upper()


if __name__ == "__main__":
    import doctest

    # Run doctests to validate the function
    doctest.testmod()
