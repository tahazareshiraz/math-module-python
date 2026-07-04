from .constants import *
from .basics import fabs


def _newton_sqrt(x, iterations=60):
    if x < 0:
        raise ValueError("math domain error")
    if x == 0:
        return 0.0
    guess = x
    for _ in range(iterations):
        guess = 0.5 * (guess + x / guess)
    return guess



def sqrt(x):
    return _newton_sqrt(float(x))



def cbrt(x):
    if x == 0:
        return 0.0
    sign = -1 if x < 0 else 1
    x = fabs(x)
    guess = x
    for _ in range(100):
        guess = guess - (guess ** 3 - x) / (3 * guess ** 2)
    return sign * guess



def pow_(x, y):
    if y == int(y) and fabs(y) < 1000:
        n = int(y)
        neg = n < 0
        n = -n if neg else n
        result = 1.0
        base = float(x)
        while n > 0:
            if n & 1:
                result *= base
            base *= base
            n >>= 1
        if neg:
            if result == 0:
                raise ZeroDivisionError("0.0 cannot be raised to a negative power")
            return 1.0 / result
        return result
    if x < 0:
        raise ValueError("math domain error")
    if x == 0:
        if y > 0:
            return 0.0
        raise ValueError("math domain error")
    return exp(y * log(x))



def exp(x):
    if x != x:
        return NAN
    if x == INF:
        return INF
    if x == -INF:
        return 0.0
    n = 0
    reduced = x
    while reduced > 0.5:
        reduced /= 2
        n += 1
    while reduced < -0.5:
        reduced /= 2
        n += 1
    term = 1.0
    total = 1.0
    for k in range(1, 60):
        term *= reduced / k
        total += term
    for _ in range(n):
        total *= total
    return total



def expm1(x):
    return exp(x) - 1.0



def log1p(x):
    if x <= -1:
        raise ValueError("math domain error")
    if fabs(x) < 1e-4:
        term = x
        total = 0.0
        sign = 1.0
        for k in range(1, 40):
            total += sign * (x ** k) / k
            sign = -sign
        return total
    return log(1.0 + x)



def _ln_series(y):
    z = (y - 1) / (y + 1)
    z2 = z * z
    term = z
    total = 0.0
    k = 1
    for _ in range(200):
        total += term / k
        term *= z2
        k += 2
    return 2 * total



def log(x, base=None):
    if base is not None:
        return log(x) / log(base)
    if x <= 0:
        if x == 0:
            raise ValueError("math domain error")
        raise ValueError("math domain error")
    if x != x:
        return NAN
    if x == INF:
        return INF
    n = 0
    y = x
    while y > 1.5:
        y /= E
        n += 1
    while y < 0.667:
        y *= E
        n -= 1
    return _ln_series(y) + n



def log2(x):
    return log(x) / LN2



def log10(x):
    return log(x) / LN10

