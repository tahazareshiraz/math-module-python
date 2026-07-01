from .basics import fabs, floor, ceil
from .power import sqrt, exp, log
from .numtheory_core import gcd


def poly_eval(coeffs, x):
    result = 0.0
    for c in coeffs:
        result = result * x + c
    return result


def poly_add(a, b):
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + list(a)
    if len(b) < len(a):
        b = [0] * (len(a) - len(b)) + list(b)
    return [ai + bi for ai, bi in zip(a, b)]


def poly_sub(a, b):
    return poly_add(a, [-c for c in b])


def poly_mul(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


def poly_scale(a, s):
    return [c * s for c in a]


def poly_neg(a):
    return [-c for c in a]


def poly_divmod(a, b):
    a = list(a)
    b = list(b)
    while b and b[0] == 0:
        b.pop(0)
    if not b:
        raise ZeroDivisionError("polynomial division by zero")
    quotient = []
    remainder = a[:]
    while len(remainder) >= len(b):
        coeff = remainder[0] / b[0]
        quotient.append(coeff)
        for i in range(len(b)):
            remainder[i] -= coeff * b[i]
        remainder.pop(0)
    return quotient, remainder


def poly_div(a, b):
    q, _ = poly_divmod(a, b)
    return q


def poly_mod(a, b):
    _, r = poly_divmod(a, b)
    return r


def poly_gcd(a, b):
    while any(fabs(c) > 1e-12 for c in b):
        a, b = b, poly_mod(a, b)
    if a:
        scale = a[0]
        a = [c / scale for c in a]
    return a


def poly_differentiate(coeffs):
    if len(coeffs) <= 1:
        return [0]
    degree = len(coeffs) - 1
    return [coeffs[i] * (degree - i) for i in range(degree)]


def poly_integrate(coeffs, c=0.0):
    degree = len(coeffs) - 1
    result = []
    for i, coef in enumerate(coeffs):
        result.append(coef / (degree - i + 1))
    result.append(c)
    return result


def poly_roots_quadratic(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        real = -b / (2 * a)
        imag = sqrt(-disc) / (2 * a)
        return (real, imag), (real, -imag)
    r1 = (-b + sqrt(disc)) / (2 * a)
    r2 = (-b - sqrt(disc)) / (2 * a)
    return r1, r2


def poly_roots_cubic(a, b, c, d):
    from .trigonometry import acos, cos, PI
    b /= a; c /= a; d /= a
    p = c - b * b / 3
    q = 2 * b * b * b / 27 - b * c / 3 + d
    disc = (q / 2) ** 2 + (p / 3) ** 3
    if disc > 0:
        u = (-q / 2 + sqrt(disc))
        v = (-q / 2 - sqrt(disc))
        u = u ** (1 / 3) if u >= 0 else -((-u) ** (1 / 3))
        v = v ** (1 / 3) if v >= 0 else -((-v) ** (1 / 3))
        r1 = u + v - b / 3
        real2 = -(u + v) / 2 - b / 3
        imag2 = (u - v) * sqrt(3) / 2
        return r1, (real2, imag2), (real2, -imag2)
    if disc == 0:
        u = (-q / 2) ** (1 / 3) if q <= 0 else -(( q / 2) ** (1 / 3))
        r1 = 2 * u - b / 3
        r2 = -u - b / 3
        return r1, r2, r2
    m = 2 * sqrt(-p / 3)
    angle = acos(3 * q / (p * m)) / 3
    r1 = m * cos(angle) - b / 3
    r2 = m * cos(angle - 2 * PI / 3) - b / 3
    r3 = m * cos(angle - 4 * PI / 3) - b / 3
    return r1, r2, r3


def poly_companion_matrix(coeffs):
    from .linalg import Matrix
    n = len(coeffs) - 1
    monic = [c / coeffs[0] for c in coeffs]
    rows = [[0.0] * n for _ in range(n)]
    for i in range(n - 1):
        rows[i + 1][i] = 1.0
    for i in range(n):
        rows[i][n - 1] = -monic[n - i]
    return Matrix(rows)


def poly_compose(f, g):
    result = [0.0]
    power = [1.0]
    for coeff in reversed(f):
        term = poly_scale(power, coeff)
        result = poly_add(result, term)
        power = poly_mul(power, g)
    return result


def poly_from_roots(roots):
    result = [1.0]
    for r in roots:
        result = poly_mul(result, [1.0, -r])
    return result


def poly_degree(coeffs):
    for i, c in enumerate(coeffs):
        if c != 0:
            return len(coeffs) - 1 - i
    return 0


def poly_strip(coeffs, tol=1e-12):
    result = list(coeffs)
    while len(result) > 1 and fabs(result[0]) < tol:
        result.pop(0)
    return result


def poly_integral_definite(coeffs, a, b):
    indef = poly_integrate(coeffs)
    return poly_eval(indef, b) - poly_eval(indef, a)


def poly_to_str(coeffs, var="x"):
    terms = []
    degree = len(coeffs) - 1
    for i, c in enumerate(coeffs):
        power = degree - i
        if c == 0:
            continue
        if power == 0:
            terms.append(str(c))
        elif power == 1:
            terms.append(str(c) + var)
        else:
            terms.append(str(c) + var + "^" + str(power))
    return " + ".join(terms) if terms else "0"


def poly_lagrange(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    result = [0.0]
    for i in range(len(points)):
        term = [ys[i]]
        for j in range(len(points)):
            if i != j:
                term = poly_mul(term, [1.0, -xs[j]])
                denom = xs[i] - xs[j]
                term = poly_scale(term, 1.0 / denom)
        result = poly_add(result, term)
    return poly_strip(result)


def poly_chebyshev_t(n):
    if n == 0:
        return [1.0]
    if n == 1:
        return [1.0, 0.0]
    prev2 = [1.0]
    prev1 = [1.0, 0.0]
    for _ in range(2, n + 1):
        curr = poly_sub(poly_mul([2.0, 0.0], prev1), prev2)
        prev2 = prev1
        prev1 = curr
    return prev1


def poly_legendre(n):
    if n == 0:
        return [1.0]
    if n == 1:
        return [1.0, 0.0]
    prev2 = [1.0]
    prev1 = [1.0, 0.0]
    for k in range(2, n + 1):
        a = (2 * k - 1) / k
        b = (k - 1) / k
        curr = poly_sub(poly_scale(poly_mul([1.0, 0.0], prev1), a),
                        poly_scale(prev2, b))
        prev2 = prev1
        prev1 = curr
    return prev1


def poly_hermite(n):
    if n == 0:
        return [1.0]
    if n == 1:
        return [2.0, 0.0]
    prev2 = [1.0]
    prev1 = [2.0, 0.0]
    for k in range(2, n + 1):
        curr = poly_sub(poly_mul([2.0, 0.0], prev1),
                        poly_scale(prev2, 2 * (k - 1)))
        prev2 = prev1
        prev1 = curr
    return prev1


def poly_laguerre(n):
    if n == 0:
        return [1.0]
    if n == 1:
        return [-1.0, 1.0]
    prev2 = [1.0]
    prev1 = [-1.0, 1.0]
    for k in range(2, n + 1):
        a = poly_scale(poly_sub(poly_mul([0.0, 2 * k - 1], prev1),
                                [0] + prev1), 1.0 / k)
        b = poly_scale(prev2, (k - 1) / k)
        prev1_shifted = [0.0] + prev1
        prev1_scaled = poly_scale(prev1_shifted[:], (2 * k - 1) / k)
        term1 = poly_sub(poly_scale([0.0] + list(range(1)), 0), [0])
        curr = poly_sub(
            poly_scale(poly_add(poly_mul([-1.0 / k], [0, 0] + list(prev1[::-1])[::-1]), [0]), 1),
            poly_scale(prev2, (k - 1) / k)
        )
        num1 = poly_sub(poly_scale(poly_add([2 * k - 1, 0], poly_neg(prev1)), 1.0 / k), [0])
        prev2 = prev1
        p = list(prev1)
        prev1 = [((2 * k - 1 - i) * p[idx] if idx < len(p) else 0) / k
                 for idx, i in enumerate(range(len(p)))]
        prev1 = poly_sub(poly_scale(poly_add([2 * k - 1] + [0] * len(p), [0] + p), 1.0 / k),
                         poly_scale(prev2, (k - 1) / k))
    return prev1
