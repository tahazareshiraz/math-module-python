import unittest
import math
import statistics
import src.taha_math_shiraz as tms


class TestVectorMatrixComplex(unittest.TestCase):
    def test_vector_ops(self):
        a = tms.Vector([1, 2, 3])
        b = tms.Vector([4, 5, 6])
        self.assertEqual((a + b).components, [5, 7, 9])
        self.assertEqual((a - b).components, [-3, -3, -3])
        self.assertEqual(a.dot(b), 32)
        self.assertAlmostEqual(a.norm(), math.sqrt(14))

    def test_vector_cross(self):
        a = tms.Vector([1, 0, 0])
        b = tms.Vector([0, 1, 0])
        c = a.cross(b)
        self.assertEqual(c.components, [0, 0, 1])

    def test_matrix_determinant_inverse(self):
        m = tms.Matrix([[4, 7], [2, 6]])
        self.assertAlmostEqual(m.determinant(), 10)
        inv = m.inverse()
        identity = m * inv
        for i in range(2):
            for j in range(2):
                expected = 1.0 if i == j else 0.0
                self.assertAlmostEqual(identity[i][j], expected, places=6)

    def test_matrix_transpose_trace(self):
        m = tms.Matrix([[1, 2], [3, 4]])
        self.assertEqual(m.transpose().rows, [[1, 3], [2, 4]])
        self.assertEqual(m.trace(), 5)

    def test_matrix_power(self):
        m = tms.Matrix([[1, 1], [0, 1]])
        result = tms.matrix_power(m, 3)
        self.assertEqual(result.rows, [[1, 3], [0, 1]])

    def test_complex_ops(self):
        z1 = tms.Complex(3, 4)
        z2 = tms.Complex(1, 2)
        self.assertEqual((z1 + z2).real, 4)
        self.assertEqual((z1 + z2).imag, 6)
        self.assertAlmostEqual(z1.modulus(), 5.0)
        product = z1 * z2
        self.assertEqual(product.real, 3 * 1 - 4 * 2)
        self.assertEqual(product.imag, 3 * 2 + 4 * 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
