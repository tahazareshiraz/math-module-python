from .constants import PI
from .power import sqrt


def circle_area(radius):
    return PI * radius * radius


def circle_circumference(radius):
    return 2 * PI * radius


def circle_diameter(radius):
    return 2 * radius


def sector_area(radius, angle_radians):
    return 0.5 * radius * radius * angle_radians


def arc_length(radius, angle_radians):
    return radius * angle_radians


def triangle_area_base_height(base, height):
    return 0.5 * base * height


def triangle_area_heron(a, b, c):
    s = (a + b + c) / 2
    value = s * (s - a) * (s - b) * (s - c)
    if value < 0:
        raise ValueError("invalid triangle sides")
    return sqrt(value)


def triangle_perimeter(a, b, c):
    return a + b + c


def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-9


def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def rectangle_area(width, height):
    return width * height


def rectangle_perimeter(width, height):
    return 2 * (width + height)


def square_area(side):
    return side * side


def square_perimeter(side):
    return 4 * side


def square_diagonal(side):
    return side * sqrt(2)


def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height


def rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2


def parallelogram_area(base, height):
    return base * height


def regular_polygon_area(sides, side_length):
    from .trigonometry import tan
    return (sides * side_length * side_length) / (4 * tan(PI / sides))


def regular_polygon_perimeter(sides, side_length):
    return sides * side_length


def regular_polygon_interior_angle(sides):
    return (sides - 2) * PI / sides


def regular_polygon_exterior_angle(sides):
    return 2 * PI / sides


def sphere_volume(radius):
    return (4.0 / 3.0) * PI * radius ** 3


def sphere_surface_area(radius):
    return 4 * PI * radius * radius


def cylinder_volume(radius, height):
    return PI * radius * radius * height


def cylinder_surface_area(radius, height):
    return 2 * PI * radius * (radius + height)


def cylinder_lateral_area(radius, height):
    return 2 * PI * radius * height


def cone_volume(radius, height):
    return (1.0 / 3.0) * PI * radius * radius * height


def cone_surface_area(radius, slant_height):
    return PI * radius * (radius + slant_height)


def cone_slant_height(radius, height):
    return sqrt(radius * radius + height * height)


def cube_volume(side):
    return side ** 3


def cube_surface_area(side):
    return 6 * side * side


def cuboid_volume(length, width, height):
    return length * width * height


def cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + length * height)


def cuboid_diagonal(length, width, height):
    return sqrt(length ** 2 + width ** 2 + height ** 2)


def pyramid_volume(base_area, height):
    return (1.0 / 3.0) * base_area * height


def ellipse_area(semi_major, semi_minor):
    return PI * semi_major * semi_minor


def ellipse_circumference_approx(semi_major, semi_minor):
    h = ((semi_major - semi_minor) ** 2) / ((semi_major + semi_minor) ** 2)
    return PI * (semi_major + semi_minor) * (1 + (3 * h) / (10 + sqrt(4 - 3 * h)))


def distance_2d(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def distance_3d(x1, y1, z1, x2, y2, z2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))


def chebyshev_distance(p1, p2):
    return max(abs(a - b) for a, b in zip(p1, p2))


def minkowski_distance(p1, p2, p):
    return sum(abs(a - b) ** p for a, b in zip(p1, p2)) ** (1.0 / p)


def polygon_area_shoelace(points):
    n = len(points)
    if n < 3:
        raise ValueError("a polygon requires at least 3 points")
    area = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


def polygon_perimeter(points):
    n = len(points)
    total = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        total += distance_2d(x1, y1, x2, y2)
    return total


def centroid(points):
    n = len(points)
    cx = sum(p[0] for p in points) / n
    cy = sum(p[1] for p in points) / n
    return (cx, cy)


def midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("slope is undefined for a vertical line")
    return (y2 - y1) / (x2 - x1)


def line_intersection(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (px, py)
