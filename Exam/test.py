import unittest
from main import celsius_to_fahrenheit

class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_hundred(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_decimal(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)

if __name__ == '__main__':
    unittest.main()
