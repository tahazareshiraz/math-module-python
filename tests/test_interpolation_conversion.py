import unittest
import math
import statistics
import src.taha_math_shiraz as tms


class TestInterpolationAndConversion(unittest.TestCase):
    def test_lagrange(self):
        points = [(0, 1), (1, 3), (2, 7)]
        self.assertAlmostEqual(tms.lagrange_interpolation(points, 0), 1.0, places=6)
        self.assertAlmostEqual(tms.lagrange_interpolation(points, 1), 3.0, places=6)

    def test_base_conversion(self):
        for n in range(0, 256):
            self.assertEqual(tms.from_base(tms.to_base(n, 16), 16), n)
            self.assertEqual(tms.from_base(tms.to_base(n, 2), 2), n)

    def test_roman_numerals(self):
        self.assertEqual(tms.int_to_roman(1994), "MCMXCIV")
        self.assertEqual(tms.roman_to_int("MCMXCIV"), 1994)

    def test_unit_conversion(self):
        self.assertAlmostEqual(tms.convert_celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(tms.convert_fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(tms.convert_celsius_to_kelvin(0), 273.15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
