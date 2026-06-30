from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .trigonometry import degrees, radians, sin, cos, tan, sinh, cosh, tanh, asinh, acosh, atanh, asin, acos, atan, atan2, hypot, dist
from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf


class Vector:
    def __init__(self, components):
        self.components = list(components)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, idx):
        return self.components[idx]

    def __setitem__(self, idx, value):
        self.components[idx] = value

    def __repr__(self):
        return "Vector(" + repr(self.components) + ")"

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        return Vector([a * scalar for a in self.components])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __neg__(self):
        return Vector([-a for a in self.components])

    def __eq__(self, other):
        return self.components == other.components

    def dot(self, other):
        total = 0.0
        for a, b in zip(self.components, other.components):
            total += a * b
        return total

    def norm(self):
        return sqrt(self.dot(self))

    def normalize(self):
        n = self.norm()
        if n == 0:
            raise ValueError("cannot normalize zero vector")
        return Vector([a / n for a in self.components])

    def cross(self, other):
        a = self.components
        b = other.components
        if len(a) != 3 or len(b) != 3:
            raise ValueError("cross product requires 3D vectors")
        return Vector([
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        ])

    def angle_with(self, other):
        denom = self.norm() * other.norm()
        if denom == 0:
            raise ValueError("cannot compute angle with zero vector")
        return acos(max(-1.0, min(1.0, self.dot(other) / denom)))



class Matrix:
    def __init__(self, rows):
        self.rows = [list(r) for r in rows]
        self.nrows = len(self.rows)
        self.ncols = len(self.rows[0]) if self.nrows > 0 else 0

    def __repr__(self):
        return "Matrix(" + repr(self.rows) + ")"

    def __getitem__(self, idx):
        return self.rows[idx]

    def __eq__(self, other):
        return self.rows == other.rows

    def __add__(self, other):
        result = []
        for r1, r2 in zip(self.rows, other.rows):
            result.append([a + b for a, b in zip(r1, r2)])
        return Matrix(result)

    def __sub__(self, other):
        result = []
        for r1, r2 in zip(self.rows, other.rows):
            result.append([a - b for a, b in zip(r1, r2)])
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            result = []
            for i in range(self.nrows):
                row = []
                for j in range(other.ncols):
                    total = 0.0
                    for k in range(self.ncols):
                        total += self.rows[i][k] * other.rows[k][j]
                    row.append(total)
                result.append(row)
            return Matrix(result)
        return Matrix([[a * other for a in row] for row in self.rows])

    def __rmul__(self, other):
        if isinstance(other, Matrix):
            return other.__mul__(self)
        return self.__mul__(other)

    def transpose(self):
        return Matrix([[self.rows[r][c] for r in range(self.nrows)] for c in range(self.ncols)])

    def trace(self):
        total = 0.0
        for i in range(min(self.nrows, self.ncols)):
            total += self.rows[i][i]
        return total

    @staticmethod
    def identity(n):
        return Matrix([[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)])

    @staticmethod
    def zeros(rows, cols):
        return Matrix([[0.0 for _ in range(cols)] for _ in range(rows)])

    def minor(self, i, j):
        rows = [row[:j] + row[j + 1:] for k, row in enumerate(self.rows) if k != i]
        return Matrix(rows)

    def determinant(self):
        if self.nrows != self.ncols:
            raise ValueError("determinant requires a square matrix")
        n = self.nrows
        if n == 1:
            return self.rows[0][0]
        if n == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]
        total = 0.0
        for j in range(n):
            sign = 1 if j % 2 == 0 else -1
            total += sign * self.rows[0][j] * self.minor(0, j).determinant()
        return total

    def cofactor(self, i, j):
        sign = 1 if (i + j) % 2 == 0 else -1
        return sign * self.minor(i, j).determinant()

    def adjugate(self):
        n = self.nrows
        result = [[self.cofactor(j, i) for j in range(n)] for i in range(n)]
        return Matrix(result)

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("matrix is singular")
        adj = self.adjugate()
        return adj * (1.0 / det)

    def apply(self, vector):
        result = []
        for row in self.rows:
            total = 0.0
            for a, b in zip(row, vector.components):
                total += a * b
            result.append(total)
        return Vector(result)

    def is_symmetric(self):
        return self.rows == self.transpose().rows

    def rank(self):
        mat = [row[:] for row in self.rows]
        rows = len(mat)
        cols = len(mat[0]) if rows else 0
        rank_count = 0
        for col in range(cols):
            pivot_row = None
            for r in range(rank_count, rows):
                if fabs(mat[r][col]) > 1e-12:
                    pivot_row = r
                    break
            if pivot_row is None:
                continue
            mat[rank_count], mat[pivot_row] = mat[pivot_row], mat[rank_count]
            pivot_val = mat[rank_count][col]
            mat[rank_count] = [v / pivot_val for v in mat[rank_count]]
            for r in range(rows):
                if r != rank_count and fabs(mat[r][col]) > 1e-12:
                    factor = mat[r][col]
                    mat[r] = [v - factor * pv for v, pv in zip(mat[r], mat[rank_count])]
            rank_count += 1
        return rank_count



class Complex:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        sign = "+" if self.imag >= 0 else "-"
        return "(" + str(self.real) + sign + str(fabs(self.imag)) + "j)"

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        if denom == 0:
            raise ZeroDivisionError("division by zero complex number")
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denom,
            (self.imag * other.real - self.real * other.imag) / denom,
        )

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def modulus(self):
        return sqrt(self.real ** 2 + self.imag ** 2)

    def argument(self):
        return atan2(self.imag, self.real)

    def exp(self):
        r = exp(self.real)
        return Complex(r * cos(self.imag), r * sin(self.imag))

    def power(self, n):
        r = self.modulus()
        theta = self.argument()
        new_r = r ** n
        new_theta = theta * n
        return Complex(new_r * cos(new_theta), new_r * sin(new_theta))

    def sqrt(self):
        r = self.modulus()
        theta = self.argument()
        new_r = sqrt(r)
        return Complex(new_r * cos(theta / 2), new_r * sin(theta / 2))



def vector_projection(a, b):
    av = Vector(a)
    bv = Vector(b)
    scalar = av.dot(bv) / bv.dot(bv)
    return Vector([scalar * c for c in bv.components])



def vector_reflection(v, normal):
    vv = Vector(v)
    nv = Vector(normal).normalize()
    d = 2 * vv.dot(nv)
    return Vector([vv[i] - d * nv[i] for i in range(len(vv))])



def matrix_power(m, n):
    size = m.nrows
    result = Matrix.identity(size)
    base = m
    while n > 0:
        if n & 1:
            result = result * base
        base = base * base
        n >>= 1
    return result



def matrix_from_function(rows, cols, f):
    return Matrix([[f(i, j) for j in range(cols)] for i in range(rows)])



def rotation_matrix_2d(theta):
    return Matrix([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])



def rotation_matrix_x(theta):
    return Matrix([
        [1, 0, 0],
        [0, cos(theta), -sin(theta)],
        [0, sin(theta), cos(theta)],
    ])



def rotation_matrix_y(theta):
    return Matrix([
        [cos(theta), 0, sin(theta)],
        [0, 1, 0],
        [-sin(theta), 0, cos(theta)],
    ])



def rotation_matrix_z(theta):
    return Matrix([
        [cos(theta), -sin(theta), 0],
        [sin(theta), cos(theta), 0],
        [0, 0, 1],
    ])



def scaling_matrix(sx, sy):
    return Matrix([[sx, 0], [0, sy]])



def translation_apply(point, dx, dy):
    return (point[0] + dx, point[1] + dy)

