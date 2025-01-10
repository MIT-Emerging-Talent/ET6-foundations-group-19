# Unit tests
import unittest

# Define the get_capital function
def get_capital(country):
    """Returns the capital city of a given country. Returns None if the country is not found."""
    capitals = {
        "Afghanistan": "Kabul",
        "Zimbabwe": "Harare",
        "Albania": "Tirana",
    }
    country = country.strip()  # Remove leading/trailing whitespace
    return capitals.get(country)

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

