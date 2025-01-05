"""
a module that extract all the integers found in a given string.

@author: Mohammad R Al Salloum.
@date: 01/05/2025

"""

import re


def extract_integers(input_string: str) -> list:
    """
    This function takes a string as in input then it outputs
          a list of all integers found in input string.

          Parameters:
              input_string: str, the input string that may contain
                                the integers.
          Returns:
              list: the integers found in the input_string.

          Raises:
            AssertionError: if the input_string argument is not a str.


        >>> extract_integers(I have 1 apple and 3 bananas)
            [1, 3]
        >>> guessing_game(200 people liked the show)
            [200]
        >>> guessing_game (The temperature was -200 yesterday)
            [-200]
        >>> guessing_game (I like the flowers)
            []
    """
    assert isinstance(input_string, str), "The argument must be a string"

    return list(map(int, re.findall(r"-?\d+", input_string)))
