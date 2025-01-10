# Unit tests
import unittest

class TestGetCapital(unittest.TestCase):

    def test_valid_country(self):
        self.assertEqual(get_capital("Afghanistan"), "Kabul")
        self.assertEqual(get_capital("Zimbabwe"), "Harare")
        self.assertEqual(get_capital("Albania"), "Tirana")

    def test_invalid_country(self):
        self.assertIsNone(get_capital("Atlantis"))
        self.assertIsNone(get_capital("Wakanda"))

    def test_case_insensitivity(self):
        # Assuming the dictionary is case-sensitive and requires exact match
        self.assertIsNone(get_capital("afghanistan"))  # Invalid as lowercase
        self.assertEqual(get_capital("Afghanistan"), "Kabul")  # Valid case

    def test_strip_whitespace(self):
        self.assertEqual(get_capital(" Afghanistan "), "Kabul")
        self.assertEqual(get_capital("\tZimbabwe\n"), "Harare")

if __name__ == "__main__":
    unittest.main()
