import unittest
import math
import statistics
import src.taha_math_shiraz as tms


class TestCalculus(unittest.TestCase):
    def test_derivative(self):
        f = lambda x: x**2
        self.assertAlmostEqual(tms.derivative(f, 3), 6.0, places=3)

    def test_integral_simpson(self):
        f = lambda x: x**2
        self.assertAlmostEqual(tms.integral_simpson(f, 0, 3), 9.0, places=4)

    def test_newton_raphson(self):
        f = lambda x: x**2 - 2
        fp = lambda x: 2 * x
        root = tms.newton_raphson(f, fp, 1.0)
        self.assertAlmostEqual(root, math.sqrt(2), places=6)

    def test_bisection(self):
        f = lambda x: x**3 - x - 2
        root = tms.bisection_method(f, 1, 2)
        self.assertAlmostEqual(f(root), 0.0, places=6)

    def test_secant(self):
        f = lambda x: math.cos(x) - x
        root = tms.secant_method(f, 0, 1)
        self.assertAlmostEqual(f(root), 0.0, places=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
