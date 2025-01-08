import unittest
from ..pascal_triangle import pascals_triangle


class TestMathSequences(unittest.TestCase):
    """UTest Pascal's Triangle generation"""

    def test_pascals_triangle4(self):
        """Generate four rows."""
        self.assertEqual(pascals_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_pascals_triangle1(self):
        """Generate one row."""
        self.assertEqual(pascals_triangle(1), [[1]])

    def test_pascals_triangle0(self):
        """Generate no row."""
        self.assertEqual(pascals_triangle(0), [])

    def test_pascals_triangle5(self):
        """Generate five rows."""
        self.assertEqual(
            pascals_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        )

    def test_pascals_trianglen(self):
        """Handling a negative input."""
        with self.assertRaises(AssertionError):
            pascals_triangle(-3)
        with self.assertRaises(AssertionError):
            pascals_triangle("3")


if __name__ == "__main__":
    unittest.main()
