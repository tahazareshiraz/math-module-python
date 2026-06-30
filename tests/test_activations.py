import unittest
import math
import statistics
import taha_math_shiraz as tms


class TestActivationsAndMisc(unittest.TestCase):
    def test_sigmoid(self):
        self.assertAlmostEqual(tms.sigmoid(0), 0.5)
        self.assertTrue(tms.sigmoid(10) > 0.99)
        self.assertTrue(tms.sigmoid(-10) < 0.01)

    def test_relu(self):
        self.assertEqual(tms.relu(5), 5)
        self.assertEqual(tms.relu(-5), 0.0)

    def test_clamp_lerp(self):
        self.assertEqual(tms.clamp(15, 0, 10), 10)
        self.assertEqual(tms.clamp(-5, 0, 10), 0)
        self.assertAlmostEqual(tms.lerp(0, 10, 0.5), 5.0)

    def test_sign(self):
        self.assertEqual(tms.sign(5), 1)
        self.assertEqual(tms.sign(-5), -1)
        self.assertEqual(tms.sign(0), 0)



if __name__ == "__main__":
    unittest.main(verbosity=2)
