import unittest
import math
import statistics
import taha_math_shiraz as tms


class TestPowerLog(unittest.TestCase):
    def test_sqrt(self):
        for x in [0, 1, 2, 4, 9, 16, 100, 0.25, 12345.6789]:
            self.assertAlmostEqual(tms.sqrt(x), math.sqrt(x), places=8)

    def test_cbrt(self):
        for x in [-27, -8, 0, 1, 8, 27, 64]:
            self.assertAlmostEqual(tms.cbrt(x) ** 3, x, places=4)

    def test_isqrt(self):
        for x in range(0, 500):
            self.assertEqual(tms.isqrt(x), math.isqrt(x))

    def test_exp(self):
        for x in [-5, -1, 0, 1, 2, 5, 10]:
            self.assertAlmostEqual(tms.exp(x), math.exp(x), places=6)

    def test_log(self):
        for x in [0.001, 0.5, 1, 2, math.e, 10, 1000]:
            self.assertAlmostEqual(tms.log(x), math.log(x), places=6)

    def test_log_base(self):
        self.assertAlmostEqual(tms.log(8, 2), math.log(8, 2), places=6)
        self.assertAlmostEqual(tms.log(100, 10), math.log(100, 10), places=6)

    def test_log2_log10(self):
        for x in [1, 2, 8, 1024, 100, 1000]:
            self.assertAlmostEqual(tms.log2(x), math.log2(x), places=6)
            self.assertAlmostEqual(tms.log10(x), math.log10(x), places=6)

    def test_log1p_expm1(self):
        for x in [-0.5, -0.1, 0, 0.1, 1, 5]:
            self.assertAlmostEqual(tms.log1p(x), math.log1p(x), places=6)
            self.assertAlmostEqual(tms.expm1(x), math.expm1(x), places=6)

    def test_pow(self):
        cases = [(2, 10), (3, 5), (2.5, 3), (4, 0.5), (10, -2)]
        for x, y in cases:
            self.assertAlmostEqual(tms.pow_(x, y), math.pow(x, y), places=4)

    def test_domain_errors(self):
        with self.assertRaises(ValueError):
            tms.sqrt(-1)
        with self.assertRaises(ValueError):
            tms.log(-1)
        with self.assertRaises(ValueError):
            tms.log(0)



if __name__ == "__main__":
    unittest.main(verbosity=2)
