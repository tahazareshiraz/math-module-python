from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf


def lagrange_interpolation(points, x):
    total = 0.0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if i != j:
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        total += term
    return total



def newton_divided_difference(points, x):
    n = len(points)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    coef = ys[:]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - j])
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - xs[i]) + coef[i]
    return result



def linear_interpolation(x0, y0, x1, y1, x):
    if x1 == x0:
        raise ValueError("x0 and x1 must differ")
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)



def bilinear_interpolation(x, y, x1, y1, x2, y2, q11, q12, q21, q22):
    denom = (x2 - x1) * (y2 - y1)
    term1 = q11 * (x2 - x) * (y2 - y)
    term2 = q21 * (x - x1) * (y2 - y)
    term3 = q12 * (x2 - x) * (y - y1)
    term4 = q22 * (x - x1) * (y - y1)
    return (term1 + term2 + term3 + term4) / denom



def continued_fraction(x, depth=15):
    terms = []
    for _ in range(depth):
        a = floor(x)
        terms.append(a)
        frac = x - a
        if fabs(frac) < 1e-12:
            break
        x = 1.0 / frac
    return terms



def convergent_from_continued_fraction(terms):
    num, den = 1, 0
    for t in reversed(terms):
        num, den = t * num + den, num
    return num, den



def egyptian_fraction(numerator, denominator):
    result = []
    n, d = numerator, denominator
    while n != 0:
        x = -(-d // n)
        result.append(x)
        n, d = n * x - d, d * x
    return result

