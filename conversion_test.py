import unittest

import conversion


class TestConversion(unittest.TestCase):
    def test_celsius2fahrenheit(self):
        self.assertEqual(conversion.celsius2fahrenheit(0), 32)
        self.assertAlmostEqual(conversion.celsius2fahrenheit(31), 87.8)
        self.assertAlmostEqual(conversion.celsius2fahrenheit(-12), 10.4)

    def test_fahrenheit2celsius(self):
        self.assertEqual(conversion.fahrenheit2celsius(0), -32 / 1.8)
        self.assertEqual(conversion.fahrenheit2celsius(32), 0)
        self.assertEqual(conversion.fahrenheit2celsius(99.2), 67.2 / 1.8)
