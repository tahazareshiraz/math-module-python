import unittest
import math
import statistics
import taha_math_shiraz as tms


class TestCombinatoricsNumberTheory(unittest.TestCase):
    def test_factorial(self):
        for n in range(0, 50):
            self.assertEqual(tms.factorial(n), math.factorial(n))

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            tms.factorial(-1)

    def test_gcd_lcm(self):
        for a in range(1, 40):
            for b in range(1, 10):
                self.assertEqual(tms.gcd(a, b), math.gcd(a, b))
                self.assertEqual(tms.lcm(a, b), math.lcm(a, b))

    def test_comb_perm(self):
        for n in range(0, 25):
            for k in range(0, n + 1):
                self.assertEqual(tms.comb(n, k), math.comb(n, k))
                self.assertEqual(tms.perm(n, k), math.perm(n, k))

    def test_is_prime(self):
        primes_under_100 = [p for p in range(2, 100) if all(p % i for i in range(2, int(p ** 0.5) + 1))]
        detected = [p for p in range(2, 100) if tms.is_prime(p)]
        self.assertEqual(primes_under_100, detected)

    def test_prime_factors(self):
        self.assertEqual(tms.prime_factors(360), [2, 2, 2, 3, 3, 5])
        self.assertEqual(sorted(set(tms.prime_factors(97))), [97])

    def test_divisors(self):
        self.assertEqual(tms.divisors(28), [1, 2, 4, 7, 14, 28])
        self.assertTrue(tms.is_perfect(28))
        self.assertTrue(tms.is_perfect(6))
        self.assertFalse(tms.is_perfect(10))

    def test_euler_totient(self):
        known = {1: 1, 2: 1, 3: 2, 4: 2, 9: 6, 10: 4, 36: 12}
        for n, val in known.items():
            self.assertEqual(tms.euler_totient(n), val)

    def test_fibonacci(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, val in enumerate(expected):
            self.assertEqual(tms.fibonacci(i), val)

    def test_catalan(self):
        expected = [1, 1, 2, 5, 14, 42, 132]
        for i, val in enumerate(expected):
            self.assertEqual(tms.catalan(i), val)

    def test_collatz(self):
        self.assertEqual(tms.collatz_length(1), 0)
        self.assertTrue(tms.collatz_length(27) > 0)

    def test_mod_inverse_and_pow(self):
        self.assertEqual((tms.mod_inverse(3, 11) * 3) % 11, 1)
        self.assertEqual(tms.mod_pow(2, 10, 1000), pow(2, 10, 1000))

    def test_amicable_pairs(self):
        self.assertIn((220, 284), tms.find_amicable_pairs(300))

    def test_polygonal_numbers(self):
        for n in range(1, 30):
            self.assertEqual(tms.triangular_number(n), n * (n + 1) // 2)
            self.assertEqual(tms.square_number(n), n * n)



if __name__ == "__main__":
    unittest.main(verbosity=2)
