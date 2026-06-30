import unittest
import math
import statistics
import taha_math_shiraz as tms


class TestBasicArithmetic(unittest.TestCase):
    def test_fabs(self):
        for x in [-5, -1.5, 0, 1.5, 5]:
            self.assertEqual(tms.fabs(x), math.fabs(x))

    def test_floor_ceil_trunc(self):
        for x in [-3.7, -1.0, -0.5, 0.0, 0.5, 1.0, 3.7]:
            self.assertEqual(tms.floor(x), math.floor(x))
            self.assertEqual(tms.ceil(x), math.ceil(x))
            self.assertEqual(tms.trunc(x), math.trunc(x))

    def test_fmod(self):
        for x, y in [(10, 3), (-10, 3), (10, -3), (7.5, 2.5)]:
            self.assertAlmostEqual(tms.fmod(x, y), math.fmod(x, y), places=9)

    def test_copysign(self):
        self.assertEqual(tms.copysign(3, -1), math.copysign(3, -1))
        self.assertEqual(tms.copysign(-3, 1), math.copysign(-3, 1))

    def test_isclose(self):
        self.assertTrue(tms.isclose(1.0000000001, 1.0000000002))
        self.assertFalse(tms.isclose(1.0, 2.0))

    def test_isfinite_isinf_isnan(self):
        self.assertTrue(tms.isfinite(1.0))
        self.assertFalse(tms.isfinite(tms.INF))
        self.assertTrue(tms.isinf(tms.INF))
        self.assertTrue(tms.isnan(tms.NAN))



if __name__ == "__main__":
    unittest.main(verbosity=2)
