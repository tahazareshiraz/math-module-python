from .constants import *
from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .trigonometry import degrees, radians, sin, cos, tan, sinh, cosh, tanh, asinh, acosh, atanh, asin, acos, atan, atan2, hypot, dist
from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf
from .aggregates import fsum, prod, isclose, comb, perm


def distance_2d(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)



def distance_3d(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)



def triangle_area(a, b, c):
    s = (a + b + c) / 2.0
    val = s * (s - a) * (s - b) * (s - c)
    if val < 0:
        raise ValueError("invalid triangle sides")
    return sqrt(val)



def triangle_area_coords(p1, p2, p3):
    return fabs(
        (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0
    )



def circle_area(r):
    return PI * r * r



def circle_circumference(r):
    return TAU * r



def sphere_volume(r):
    return (4.0 / 3.0) * PI * r ** 3



def sphere_surface_area(r):
    return 4.0 * PI * r ** 2



def cylinder_volume(r, h):
    return PI * r * r * h



def cylinder_surface_area(r, h):
    return 2 * PI * r * (r + h)



def cone_volume(r, h):
    return (1.0 / 3.0) * PI * r * r * h



def cone_surface_area(r, h):
    slant = sqrt(r * r + h * h)
    return PI * r * (r + slant)



def regular_polygon_area(n, side):
    return (n * side * side) / (4.0 * tan(PI / n))



def regular_polygon_perimeter(n, side):
    return n * side



def law_of_cosines(a, b, gamma_angle):
    return sqrt(a * a + b * b - 2 * a * b * cos(gamma_angle))



def law_of_sines_ratio(a, angle_a):
    return a / sin(angle_a)



def heron_perimeter(a, b, c):
    return a + b + c



def polygon_area_shoelace(points):
    n = len(points)
    total = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        total += x1 * y2 - x2 * y1
    return fabs(total) / 2.0



def centroid(points):
    n = len(points)
    cx = sum(p[0] for p in points) / n
    cy = sum(p[1] for p in points) / n
    return (cx, cy)



def is_collinear(p1, p2, p3):
    return isclose(
        (p2[1] - p1[1]) * (p3[0] - p2[0]),
        (p3[1] - p2[1]) * (p2[0] - p1[0]),
        abs_tol=1e-9,
    )



def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0)



def slope(p1, p2):
    if p2[0] == p1[0]:
        raise ValueError("vertical line has undefined slope")
    return (p2[1] - p1[1]) / (p2[0] - p1[0])



def line_intersection(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (px, py)



def point_in_circle(p, center, r):
    return distance_2d(p, center) <= r



def point_in_triangle(p, a, b, c):
    def sign_area(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    d1 = sign_area(p, a, b)
    d2 = sign_area(p, b, c)
    d3 = sign_area(p, c, a)
    has_neg = d1 < 0 or d2 < 0 or d3 < 0
    has_pos = d1 > 0 or d2 > 0 or d3 > 0
    return not (has_neg and has_pos)

