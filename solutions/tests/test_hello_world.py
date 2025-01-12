"""
Unit tests for the `print_hello_world` function.

Author: Tamara Saqer
Date: 2025-01-12
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from solutions.hello_world import print_hello_world


class TestPrintHelloWorld(unittest.TestCase):
    """
    Test cases for the `print_hello_world` function.
    """

    def test_hello_world_output(self):
        """
        Test that the function returns 'Hello, World!'.
        """
        self.assertEqual(print_hello_world(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
