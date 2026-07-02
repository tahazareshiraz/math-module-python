import unittest
import math
import statistics
import src.taha_math_shiraz as tms


class TestGeometry(unittest.TestCase):
    def test_distances(self):
        self.assertAlmostEqual(tms.distance_2d((0, 0), (3, 4)), 5.0)
        self.assertAlmostEqual(tms.distance_3d((0, 0, 0), (1, 2, 2)), 3.0)

    def test_triangle_area(self):
        self.assertAlmostEqual(tms.triangle_area(3, 4, 5), 6.0)
        self.assertAlmostEqual(tms.triangle_area_coords((0, 0), (4, 0), (0, 3)), 6.0)

    def test_circle_sphere(self):
        self.assertAlmostEqual(tms.circle_area(2), math.pi * 4)
        self.assertAlmostEqual(tms.sphere_volume(3), (4 / 3) * math.pi * 27)

    def test_polygon_shoelace(self):
        square = [(0, 0), (4, 0), (4, 4), (0, 4)]
        self.assertAlmostEqual(tms.polygon_area_shoelace(square), 16.0)

    def test_point_in_triangle(self):
        self.assertTrue(tms.point_in_triangle((1, 1), (0, 0), (5, 0), (0, 5)))
        self.assertFalse(tms.point_in_triangle((10, 10), (0, 0), (5, 0), (0, 5)))

    def test_line_intersection(self):
        p = tms.line_intersection((0, 0), (4, 4), (0, 4), (4, 0))
        self.assertAlmostEqual(p[0], 2.0)
        self.assertAlmostEqual(p[1], 2.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
