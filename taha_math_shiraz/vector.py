from .power import sqrt


class Vector:
    def __init__(self, components):
        self.components = list(components)
        self.dimension = len(self.components)

    def __repr__(self):
        return "Vector(" + str(self.components) + ")"

    def __eq__(self, other):
        return self.components == other.components

    def __getitem__(self, idx):
        return self.components[idx]

    def __len__(self):
        return self.dimension

    def add(self, other):
        self._check_dimension(other)
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def subtract(self, other):
        self._check_dimension(other)
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def scalar_multiply(self, scalar):
        return Vector([a * scalar for a in self.components])

    def dot(self, other):
        self._check_dimension(other)
        return sum(a * b for a, b in zip(self.components, other.components))

    def cross(self, other):
        if self.dimension != 3 or other.dimension != 3:
            raise ValueError("cross product requires 3-dimensional vectors")
        a, b = self.components, other.components
        return Vector([
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        ])

    def magnitude(self):
        return sqrt(sum(c * c for c in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("cannot normalize the zero vector")
        return Vector([c / mag for c in self.components])

    def angle_between(self, other):
        from .trigonometry import acos
        denom = self.magnitude() * other.magnitude()
        if denom == 0:
            raise ValueError("cannot compute angle with zero vector")
        cos_theta = self.dot(other) / denom
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return acos(cos_theta)

    def projection_onto(self, other):
        denom = other.dot(other)
        if denom == 0:
            raise ValueError("cannot project onto the zero vector")
        scalar = self.dot(other) / denom
        return other.scalar_multiply(scalar)

    def is_orthogonal_to(self, other):
        return abs(self.dot(other)) < 1e-9

    def is_parallel_to(self, other):
        if self.dimension != other.dimension:
            return False
        ratios = []
        for a, b in zip(self.components, other.components):
            if b == 0:
                if a != 0:
                    return False
                continue
            ratios.append(a / b)
        return len(set(round(r, 9) for r in ratios)) <= 1

    def to_list(self):
        return self.components[:]

    def distance_to(self, other):
        return self.subtract(other).magnitude()

    def lerp(self, other, t):
        self._check_dimension(other)
        return Vector([a + (b - a) * t for a, b in zip(self.components, other.components)])

    def negate(self):
        return Vector([-c for c in self.components])

    def _check_dimension(self, other):
        if self.dimension != other.dimension:
            raise ValueError("vectors must have the same dimension")


def zero_vector(dimension):
    return Vector([0] * dimension)


def unit_vector(dimension, axis):
    components = [0] * dimension
    components[axis] = 1
    return Vector(components)


def sum_vectors(vectors):
    if not vectors:
        raise ValueError("at least one vector is required")
    result = vectors[0]
    for v in vectors[1:]:
        result = result.add(v)
    return result


def average_vector(vectors):
    total = sum_vectors(vectors)
    return total.scalar_multiply(1.0 / len(vectors))


def triple_product(a, b, c):
    return a.dot(b.cross(c))
