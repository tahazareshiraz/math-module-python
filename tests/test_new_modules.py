import unittest
import taha_math_shiraz as tms


class TestPolynomial(unittest.TestCase):
    def test_eval(self):
        self.assertAlmostEqual(tms.poly_eval([1, 0, -1], 3), 8.0)
        self.assertAlmostEqual(tms.poly_eval([2, -3, 1], 2), 3.0)
        self.assertEqual(tms.poly_eval([5], 100), 5.0)

    def test_add_sub(self):
        self.assertEqual(tms.poly_add([1, 2], [3, 4]), [4, 6])
        self.assertEqual(tms.poly_sub([5, 5], [2, 3]), [3, 2])

    def test_mul(self):
        self.assertEqual(tms.poly_mul([1, 1], [1, -1]), [1, 0, -1])
        self.assertEqual(tms.poly_mul([1, 2, 1], [1]), [1, 2, 1])

    def test_differentiate(self):
        self.assertEqual(tms.poly_differentiate([1, 0, 0]), [2, 0])
        self.assertEqual(tms.poly_differentiate([3, 2, 1]), [6, 2])

    def test_integrate(self):
        p = tms.poly_integrate([2, 0], 0.0)
        self.assertAlmostEqual(tms.poly_eval(p, 3), 9.0)

    def test_integral_definite(self):
        self.assertAlmostEqual(tms.poly_integral_definite([1, 0, 0], 0, 3), 9.0, places=6)

    def test_roots_quadratic(self):
        r1, r2 = tms.poly_roots_quadratic(1, -5, 6)
        self.assertIn(round(r1, 6), [3.0, 2.0])
        self.assertIn(round(r2, 6), [3.0, 2.0])

    def test_from_roots(self):
        p = tms.poly_from_roots([1, 2])
        self.assertAlmostEqual(tms.poly_eval(p, 1), 0.0, places=6)
        self.assertAlmostEqual(tms.poly_eval(p, 2), 0.0, places=6)

    def test_compose(self):
        p = tms.poly_compose([1, 0], [1, 1])
        self.assertAlmostEqual(tms.poly_eval(p, 3), 4.0, places=6)

    def test_degree(self):
        self.assertEqual(tms.poly_degree([0, 0, 3, 1]), 1)

    def test_chebyshev(self):
        t2 = tms.poly_chebyshev_t(2)
        self.assertAlmostEqual(tms.poly_eval(t2, 1.0), 1.0, places=6)

    def test_legendre(self):
        p2 = tms.poly_legendre(2)
        self.assertAlmostEqual(tms.poly_eval(p2, 1.0), 1.0, places=6)
        self.assertAlmostEqual(tms.poly_eval(p2, 0.0), -0.5, places=6)

    def test_lagrange(self):
        pts = [(0, 1), (1, 2), (2, 5)]
        p = tms.poly_lagrange(pts)
        for x, y in pts:
            self.assertAlmostEqual(tms.poly_eval(p, x), y, places=5)

    def test_divmod(self):
        q, r = tms.poly_divmod([1, -3, 2], [1, -1])
        self.assertAlmostEqual(tms.poly_eval(q, 5), tms.poly_eval([1, -2], 5), places=5)

    def test_strip(self):
        self.assertEqual(tms.poly_strip([0, 0, 1, 2]), [1, 2])


class TestDatatypes(unittest.TestCase):
    def test_fraction_basic(self):
        f = tms.Fraction(1, 3)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 3)

    def test_fraction_arithmetic(self):
        a = tms.Fraction(1, 2)
        b = tms.Fraction(1, 3)
        self.assertEqual(a + b, tms.Fraction(5, 6))
        self.assertEqual(a - b, tms.Fraction(1, 6))
        self.assertEqual(a * b, tms.Fraction(1, 6))
        self.assertEqual(a / b, tms.Fraction(3, 2))

    def test_fraction_reduction(self):
        f = tms.Fraction(6, 8)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

    def test_fraction_comparison(self):
        self.assertTrue(tms.Fraction(1, 2) < tms.Fraction(3, 4))
        self.assertTrue(tms.Fraction(2, 4) == tms.Fraction(1, 2))

    def test_fraction_proper(self):
        self.assertTrue(tms.Fraction(1, 3).is_proper())
        self.assertFalse(tms.Fraction(4, 3).is_proper())

    def test_fixed_decimal(self):
        d = tms.FixedDecimal(3.14, 2)
        self.assertAlmostEqual(float(d), 3.14, places=2)

    def test_fixed_decimal_arithmetic(self):
        a = tms.FixedDecimal(1.5, 2)
        b = tms.FixedDecimal(2.5, 2)
        self.assertAlmostEqual(float(a + b), 4.0, places=1)

    def test_interval_contains(self):
        iv = tms.Interval(1.0, 5.0)
        self.assertIn(3.0, iv)
        self.assertNotIn(6.0, iv)

    def test_interval_arithmetic(self):
        a = tms.Interval(1, 3)
        b = tms.Interval(2, 4)
        c = a + b
        self.assertEqual(c.lo, 3)
        self.assertEqual(c.hi, 7)

    def test_interval_intersection(self):
        a = tms.Interval(1, 5)
        b = tms.Interval(3, 8)
        c = a.intersection(b)
        self.assertEqual(c.lo, 3)
        self.assertEqual(c.hi, 5)

    def test_ratio(self):
        r = tms.Ratio(4, 6)
        self.assertEqual(r.a, 2)
        self.assertEqual(r.b, 3)
        self.assertAlmostEqual(r.as_float(), 2 / 3)


class TestCrypto(unittest.TestCase):
    def test_caesar(self):
        self.assertEqual(tms.caesar_encrypt("ABC", 3), "DEF")
        self.assertEqual(tms.caesar_decrypt("DEF", 3), "ABC")

    def test_caesar_roundtrip(self):
        msg = "Hello World"
        self.assertEqual(tms.caesar_decrypt(tms.caesar_encrypt(msg, 13), 13), msg)

    def test_rot13_involution(self):
        msg = "Hello"
        self.assertEqual(tms.rot13(tms.rot13(msg)), msg)

    def test_vigenere(self):
        msg = "ATTACKATDAWN"
        key = "LEMON"
        enc = tms.vigenere_encrypt(msg, key)
        self.assertEqual(tms.vigenere_decrypt(enc, key), msg)

    def test_atbash(self):
        self.assertEqual(tms.atbash_encrypt("ABC"), "ZYX")
        self.assertEqual(tms.atbash_decrypt("ZYX"), "ABC")

    def test_affine_roundtrip(self):
        msg = "HELLO"
        enc = tms.affine_encrypt(msg, 7, 3)
        self.assertEqual(tms.affine_decrypt(enc, 7, 3), msg)

    def test_rail_fence_roundtrip(self):
        msg = "HELLOWORLD"
        enc = tms.rail_fence_encrypt(msg, 3)
        self.assertEqual(tms.rail_fence_decrypt(enc, 3), msg)

    def test_rsa_roundtrip(self):
        pub, priv = tms.rsa_generate_keys(61, 53)
        ct = tms.rsa_encrypt(42, pub)
        self.assertEqual(tms.rsa_decrypt(ct, priv), 42)

    def test_xor_cipher(self):
        msg = "Hello"
        key = "key"
        enc = tms.xor_cipher(msg, key)
        self.assertEqual(tms.xor_cipher(enc, key), msg)

    def test_luhn(self):
        self.assertTrue(tms.luhn_check(4532015112830366))
        self.assertFalse(tms.luhn_check(1234567890123456))

    def test_hamming_distance(self):
        self.assertEqual(tms.hamming_distance("karolin", "kathrin"), 3)

    def test_miller_rabin(self):
        self.assertTrue(tms.is_prime_miller_rabin(97))
        self.assertFalse(tms.is_prime_miller_rabin(100))

    def test_checksums(self):
        data = "hello"
        self.assertIsInstance(tms.checksum_sum(data), int)
        self.assertIsInstance(tms.checksum_xor(data), int)


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = tms.Graph()
        self.g.add_edge("A", "B", 1)
        self.g.add_edge("B", "C", 2)
        self.g.add_edge("A", "C", 5)

    def test_vertices_edges(self):
        self.assertEqual(sorted(self.g.vertices()), ["A", "B", "C"])
        self.assertEqual(self.g.edge_count(), 3)

    def test_bfs_dfs(self):
        self.assertEqual(self.g.bfs("A"), ["A", "B", "C"])
        self.assertIn("A", self.g.dfs("A"))

    def test_dijkstra(self):
        dist, _ = self.g.dijkstra("A")
        self.assertEqual(dist["C"], 3)

    def test_shortest_path(self):
        path, cost = self.g.shortest_path("A", "C")
        self.assertEqual(cost, 3)
        self.assertEqual(path, ["A", "B", "C"])

    def test_is_connected(self):
        self.assertTrue(self.g.is_connected())

    def test_is_bipartite(self):
        g2 = tms.graph_cycle(4)
        self.assertTrue(g2.is_bipartite())
        g3 = tms.graph_cycle(3)
        self.assertFalse(g3.is_bipartite())

    def test_mst_kruskal(self):
        mst = self.g.minimum_spanning_tree_kruskal()
        total_weight = sum(w for _, _, w in mst)
        self.assertEqual(total_weight, 3)

    def test_components(self):
        self.assertEqual(len(self.g.connected_components()), 1)

    def test_floyd_warshall(self):
        fw = self.g.floyd_warshall()
        self.assertEqual(fw["A"]["C"], 3)

    def test_directed_topological(self):
        dg = tms.Graph(directed=True)
        dg.add_edge(1, 2)
        dg.add_edge(2, 3)
        order = dg.topological_sort()
        self.assertEqual(order.index(1) < order.index(2), True)

    def test_graph_factories(self):
        k4 = tms.graph_complete(4)
        self.assertEqual(k4.edge_count(), 6)
        c5 = tms.graph_cycle(5)
        self.assertEqual(c5.edge_count(), 5)


class TestAlgorithms(unittest.TestCase):
    def test_sorting(self):
        arr = [5, 3, 8, 1, 9, 2]
        expected = sorted(arr)
        self.assertEqual(tms.bubble_sort(arr), expected)
        self.assertEqual(tms.merge_sort(arr), expected)
        self.assertEqual(tms.quick_sort(arr), expected)
        self.assertEqual(tms.heap_sort(arr), expected)
        self.assertEqual(tms.shell_sort(arr), expected)
        self.assertEqual(tms.insertion_sort(arr), expected)
        self.assertEqual(tms.selection_sort(arr), expected)

    def test_counting_radix_sort(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        self.assertEqual(tms.counting_sort(arr), sorted(arr))
        self.assertEqual(tms.radix_sort(arr), sorted(arr))

    def test_binary_search(self):
        arr = [1, 3, 5, 7, 9, 11]
        self.assertEqual(tms.binary_search(arr, 7), 3)
        self.assertEqual(tms.binary_search(arr, 4), -1)

    def test_levenshtein(self):
        self.assertEqual(tms.levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(tms.levenshtein_distance("", "abc"), 3)
        self.assertEqual(tms.levenshtein_distance("abc", "abc"), 0)

    def test_lcs(self):
        self.assertEqual(tms.longest_common_subsequence("ABCBDAB", "BDCAB"), 4)

    def test_knapsack(self):
        self.assertEqual(tms.knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7), 9)

    def test_coin_change(self):
        self.assertEqual(tms.coin_change([1, 5, 10, 25], 30), 2)
        self.assertEqual(tms.coin_change([2], 3), -1)

    def test_lis(self):
        self.assertEqual(tms.longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_max_subarray(self):
        self.assertEqual(tms.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_two_sum(self):
        result = tms.two_sum([2, 7, 11, 15], 9)
        self.assertEqual(sorted(result), [0, 1])

    def test_cumulative_sum(self):
        self.assertEqual(tms.cumulative_sum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_moving_average(self):
        result = tms.moving_average([1, 2, 3, 4, 5], 3)
        self.assertAlmostEqual(result[0], 2.0)
        self.assertAlmostEqual(result[2], 4.0)

    def test_sliding_window_max(self):
        self.assertEqual(tms.sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])

    def test_flatten(self):
        self.assertEqual(tms.flatten([1, [2, [3, 4], 5]]), [1, 2, 3, 4, 5])

    def test_rotate(self):
        self.assertEqual(tms.rotate_list([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])

    def test_chunk(self):
        self.assertEqual(tms.chunk_list([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
