import unittest
import math
import statistics
import src.taha_math_shiraz as tms


class TestSpecialFunctions(unittest.TestCase):
    def test_gamma(self):
        for n in range(1, 10):
            self.assertAlmostEqual(tms.gamma(n), math.gamma(n), places=3)

    def test_lgamma(self):
        for x in [1.5, 2.5, 5.5, 10.5]:
            self.assertAlmostEqual(tms.lgamma(x), math.lgamma(x), places=3)

    def test_erf_erfc(self):
        for x in [-2, -1, 0, 1, 2]:
            self.assertAlmostEqual(tms.erf(x), math.erf(x), places=4)
            self.assertAlmostEqual(tms.erfc(x), math.erfc(x), places=4)

    def test_hypot_dist(self):
        self.assertAlmostEqual(tms.hypot(3, 4), math.hypot(3, 4))
        self.assertAlmostEqual(tms.dist((0, 0), (3, 4)), math.dist((0, 0), (3, 4)))

    def test_fsum_prod(self):
        nums = [0.1] * 10
        self.assertAlmostEqual(tms.fsum(nums), math.fsum(nums), places=9)
        self.assertEqual(tms.prod([1, 2, 3, 4]), math.prod([1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
