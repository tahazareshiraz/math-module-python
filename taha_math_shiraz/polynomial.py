class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = list(coefficients)
        self._trim()

    def _trim(self):
        while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
            self.coefficients.pop()

    def degree(self):
        return len(self.coefficients) - 1

    def __repr__(self):
        terms = []
        for i, c in enumerate(self.coefficients):
            if c != 0:
                terms.append(str(c) + "x^" + str(i))
        return " + ".join(terms) if terms else "0"

    def evaluate(self, x):
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result

    def add(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        a = self.coefficients + [0] * (max_len - len(self.coefficients))
        b = other.coefficients + [0] * (max_len - len(other.coefficients))
        return Polynomial([a[i] + b[i] for i in range(max_len)])

    def subtract(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        a = self.coefficients + [0] * (max_len - len(self.coefficients))
        b = other.coefficients + [0] * (max_len - len(other.coefficients))
        return Polynomial([a[i] - b[i] for i in range(max_len)])

    def multiply(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result[i + j] += a * b
        return Polynomial(result)

    def scalar_multiply(self, scalar):
        return Polynomial([c * scalar for c in self.coefficients])

    def derivative(self):
        if len(self.coefficients) <= 1:
            return Polynomial([0])
        return Polynomial([i * c for i, c in enumerate(self.coefficients) if i > 0])

    def integral(self, constant=0):
        new_coeffs = [constant] + [c / (i + 1) for i, c in enumerate(self.coefficients)]
        return Polynomial(new_coeffs)

    def roots_numeric(self, iterations=200, guesses=None):
        degree = self.degree()
        if guesses is None:
            guesses = [complex(0.4 + 0.9j) ** k for k in range(degree)]
        roots = list(guesses)
        for _ in range(iterations):
            new_roots = []
            for i in range(degree):
                numerator = self._evaluate_complex(roots[i])
                denominator = 1
                for j in range(degree):
                    if i != j:
                        denominator *= (roots[i] - roots[j])
                if denominator == 0:
                    new_roots.append(roots[i])
                    continue
                new_roots.append(roots[i] - numerator / denominator)
            roots = new_roots
        return roots

    def _evaluate_complex(self, x):
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result

    def is_zero(self):
        return all(c == 0 for c in self.coefficients)

    def leading_coefficient(self):
        return self.coefficients[-1]

    def compose(self, other):
        result = Polynomial([0])
        power = Polynomial([1])
        for coeff in self.coefficients:
            result = result.add(power.scalar_multiply(coeff))
            power = power.multiply(other)
        return result


def polynomial_from_roots(roots):
    result = Polynomial([1])
    for r in roots:
        result = result.multiply(Polynomial([-r, 1]))
    return result


def quadratic_roots(a, b, c):
    from .power import sqrt
    discriminant = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            raise ValueError("not a valid equation")
        return (-c / b,)
    if discriminant > 0:
        sq = sqrt(discriminant)
        return ((-b + sq) / (2 * a), (-b - sq) / (2 * a))
    if discriminant == 0:
        return (-b / (2 * a),)
    sq = sqrt(-discriminant)
    real = -b / (2 * a)
    imag = sq / (2 * a)
    return (complex(real, imag), complex(real, -imag))


def cubic_real_root_count(a, b, c, d):
    discriminant = (
        18 * a * b * c * d
        - 4 * (b ** 3) * d
        + (b ** 2) * (c ** 2)
        - 4 * a * (c ** 3)
        - 27 * (a ** 2) * (d ** 2)
    )
    if discriminant > 0:
        return 3
    if discriminant == 0:
        return 2
    return 1


def synthetic_division(coefficients, root):
    result = [coefficients[-1]]
    for c in reversed(coefficients[:-1]):
        result.append(c + result[-1] * root)
    remainder = result.pop()
    result.reverse()
    return result, remainder
