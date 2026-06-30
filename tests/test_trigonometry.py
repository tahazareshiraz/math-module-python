import unittest
import math
import statistics
import taha_math_shiraz as tms


class TestTrigonometry(unittest.TestCase):
    def test_sin_cos(self):
        for i in range(-50, 50):
            x = i * 0.1
            self.assertAlmostEqual(tms.sin(x), math.sin(x), places=6)
            self.assertAlmostEqual(tms.cos(x), math.cos(x), places=6)

    def test_tan(self):
        for i in range(-20, 20):
            x = i * 0.05
            self.assertAlmostEqual(tms.tan(x), math.tan(x), places=5)

    def test_asin_acos(self):
        for i in range(-99, 100):
            x = i / 100.0
            self.assertAlmostEqual(tms.asin(x), math.asin(x), places=5)
            self.assertAlmostEqual(tms.acos(x), math.acos(x), places=5)

    def test_atan_atan2(self):
        for i in range(-50, 50):
            x = i * 0.2
            self.assertAlmostEqual(tms.atan(x), math.atan(x), places=5)
        coords = [(1, 1), (-1, 1), (-1, -1), (1, -1), (0, 5), (0, -5)]
        for y, x in coords:
            self.assertAlmostEqual(tms.atan2(y, x), math.atan2(y, x), places=6)

    def test_hyperbolic(self):
        for i in range(-30, 30):
            x = i * 0.1
            self.assertAlmostEqual(tms.sinh(x), math.sinh(x), places=5)
            self.assertAlmostEqual(tms.cosh(x), math.cosh(x), places=5)
            self.assertAlmostEqual(tms.tanh(x), math.tanh(x), places=5)

    def test_inverse_hyperbolic(self):
        for x in [-5, -1, 0, 1, 5, 10]:
            self.assertAlmostEqual(tms.asinh(x), math.asinh(x), places=5)
        for x in [1, 1.5, 2, 5, 10]:
            self.assertAlmostEqual(tms.acosh(x), math.acosh(x), places=5)
        for x in [-0.9, -0.5, 0, 0.5, 0.9]:
            self.assertAlmostEqual(tms.atanh(x), math.atanh(x), places=5)

    def test_degrees_radians(self):
        for x in [0, 30, 45, 90, 180, 360]:
            self.assertAlmostEqual(tms.radians(x), math.radians(x), places=6)
        for x in [0, math.pi / 4, math.pi / 2, math.pi]:
            self.assertAlmostEqual(tms.degrees(x), math.degrees(x), places=6)

    def test_domain_errors(self):
        with self.assertRaises(ValueError):
            tms.asin(2)
        with self.assertRaises(ValueError):
            tms.acos(-2)
        with self.assertRaises(ValueError):
            tms.acosh(0)
        with self.assertRaises(ValueError):
            tms.atanh(1.5)



if __name__ == "__main__":
    unittest.main(verbosity=2)
