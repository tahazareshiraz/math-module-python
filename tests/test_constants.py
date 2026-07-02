import unittest
import math
import statistics
import src.taha_math_shiraz as tms


class TestConstants(unittest.TestCase):
    def test_pi(self):
        self.assertAlmostEqual(tms.PI, math.pi, places=10)

    def test_e(self):
        self.assertAlmostEqual(tms.E, math.e, places=10)

    def test_tau(self):
        self.assertAlmostEqual(tms.TAU, math.tau, places=10)

    def test_inf(self):
        self.assertEqual(tms.INF, math.inf)

    def test_nan(self):
        self.assertTrue(math.isnan(tms.NAN))


if __name__ == "__main__":
    unittest.main(verbosity=2)
