class Matrix:
    def __init__(self, data):
        self.data = [row[:] for row in data]
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    @staticmethod
    def zeros(rows, cols):
        return Matrix([[0 for _ in range(cols)] for _ in range(rows)])

    @staticmethod
    def identity(n):
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    def __repr__(self):
        return "Matrix(" + str(self.data) + ")"

    def __eq__(self, other):
        return self.data == other.data

    def __getitem__(self, idx):
        return self.data[idx]

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("matrix dimensions must match")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("matrix dimensions must match")
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def scalar_multiply(self, scalar):
        return Matrix([[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)])

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("incompatible matrix dimensions for multiplication")
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                result[i][j] = total
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)])

    def trace(self):
        if self.rows != self.cols:
            raise ValueError("trace requires a square matrix")
        return sum(self.data[i][i] for i in range(self.rows))

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("determinant requires a square matrix")
        n = self.rows
        mat = [row[:] for row in self.data]
        det = 1.0
        for i in range(n):
            pivot = mat[i][i]
            pivot_row = i
            for k in range(i + 1, n):
                if abs(mat[k][i]) > abs(pivot):
                    pivot = mat[k][i]
                    pivot_row = k
            if pivot == 0:
                return 0.0
            if pivot_row != i:
                mat[i], mat[pivot_row] = mat[pivot_row], mat[i]
                det *= -1
            det *= mat[i][i]
            for k in range(i + 1, n):
                factor = mat[k][i] / mat[i][i]
                for j in range(i, n):
                    mat[k][j] -= factor * mat[i][j]
        return det

    def minor(self, row, col):
        new_data = [r[:col] + r[col + 1:] for i, r in enumerate(self.data) if i != row]
        return Matrix(new_data)

    def cofactor(self, row, col):
        sign = 1 if (row + col) % 2 == 0 else -1
        return sign * self.minor(row, col).determinant()

    def adjugate(self):
        n = self.rows
        cofactor_matrix = [[self.cofactor(i, j) for j in range(n)] for i in range(n)]
        return Matrix(cofactor_matrix).transpose()

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("matrix is singular and has no inverse")
        adj = self.adjugate()
        return adj.scalar_multiply(1.0 / det)

    def is_square(self):
        return self.rows == self.cols

    def is_symmetric(self):
        return self.is_square() and self.data == self.transpose().data

    def to_list(self):
        return [row[:] for row in self.data]

    def row_echelon(self):
        mat = [row[:] for row in self.data]
        rows, cols = self.rows, self.cols
        pivot_row = 0
        for col in range(cols):
            if pivot_row >= rows:
                break
            max_row = pivot_row
            for r in range(pivot_row + 1, rows):
                if abs(mat[r][col]) > abs(mat[max_row][col]):
                    max_row = r
            if mat[max_row][col] == 0:
                continue
            mat[pivot_row], mat[max_row] = mat[max_row], mat[pivot_row]
            pivot_value = mat[pivot_row][col]
            mat[pivot_row] = [v / pivot_value for v in mat[pivot_row]]
            for r in range(rows):
                if r != pivot_row:
                    factor = mat[r][col]
                    mat[r] = [mat[r][c] - factor * mat[pivot_row][c] for c in range(cols)]
            pivot_row += 1
        return Matrix(mat)

    def rank(self):
        echelon = self.row_echelon().data
        rank = 0
        for row in echelon:
            if any(abs(v) > 1e-10 for v in row):
                rank += 1
        return rank


def matrix_from_vectors(vectors):
    return Matrix([list(v) for v in vectors])


def hadamard_product(a, b):
    if a.rows != b.rows or a.cols != b.cols:
        raise ValueError("matrix dimensions must match")
    return Matrix([[a.data[i][j] * b.data[i][j] for j in range(a.cols)] for i in range(a.rows)])


def kronecker_product(a, b):
    result = [[0] * (a.cols * b.cols) for _ in range(a.rows * b.rows)]
    for i in range(a.rows):
        for j in range(a.cols):
            for k in range(b.rows):
                for l in range(b.cols):
                    result[i * b.rows + k][j * b.cols + l] = a.data[i][j] * b.data[k][l]
    return Matrix(result)
