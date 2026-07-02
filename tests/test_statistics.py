import unittest
import math
import statistics
import src.taha_math_shiraz as tms


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.data = [2, 4, 4, 4, 5, 5, 7, 9]

    def test_mean(self):
        self.assertAlmostEqual(tms.mean(self.data), statistics.mean(self.data))

    def test_median(self):
        self.assertAlmostEqual(tms.median(self.data), statistics.median(self.data))

    def test_mode(self):
        self.assertEqual(tms.mode(self.data), statistics.mode(self.data))

    def test_variance_stdev(self):
        self.assertAlmostEqual(
            tms.variance(self.data), statistics.variance(self.data), places=6
        )
        self.assertAlmostEqual(
            tms.stdev(self.data), statistics.stdev(self.data), places=6
        )
        self.assertAlmostEqual(
            tms.pvariance(self.data), statistics.pvariance(self.data), places=6
        )
        self.assertAlmostEqual(
            tms.pstdev(self.data), statistics.pstdev(self.data), places=6
        )

    def test_geometric_harmonic_mean(self):
        pos_data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(
            tms.geometric_mean(pos_data), statistics.geometric_mean(pos_data), places=4
        )
        self.assertAlmostEqual(
            tms.harmonic_mean(pos_data), statistics.harmonic_mean(pos_data), places=6
        )

    def test_correlation_regression(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        self.assertAlmostEqual(tms.correlation(x, y), 1.0, places=6)
        slope, intercept = tms.linear_regression(x, y)
        self.assertAlmostEqual(slope, 2.0, places=6)
        self.assertAlmostEqual(intercept, 0.0, places=6)

    def test_quantiles(self):
        q = tms.quantiles(list(range(1, 101)))
        self.assertEqual(len(q), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
