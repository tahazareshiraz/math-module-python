from .constants import *
from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf


def degrees(x):
    return x * 180.0 / PI



def radians(x):
    return x * PI / 180.0



def _reduce_angle(x):
    k = round(x / TAU)
    return x - k * TAU



def sin(x):
    x = _reduce_angle(x)
    term = x
    total = x
    x2 = x * x
    for n in range(1, 30):
        term *= -x2 / ((2 * n) * (2 * n + 1))
        total += term
    return total



def cos(x):
    x = _reduce_angle(x)
    term = 1.0
    total = 1.0
    x2 = x * x
    for n in range(1, 30):
        term *= -x2 / ((2 * n - 1) * (2 * n))
        total += term
    return total



def tan(x):
    c = cos(x)
    if c == 0:
        raise ValueError("math domain error")
    return sin(x) / c



def sinh(x):
    e1 = exp(x)
    e2 = exp(-x)
    return (e1 - e2) / 2.0



def cosh(x):
    e1 = exp(x)
    e2 = exp(-x)
    return (e1 + e2) / 2.0



def tanh(x):
    if x > 20:
        return 1.0
    if x < -20:
        return -1.0
    e1 = exp(x)
    e2 = exp(-x)
    return (e1 - e2) / (e1 + e2)



def asinh(x):
    return log(x + sqrt(x * x + 1.0))



def acosh(x):
    if x < 1:
        raise ValueError("math domain error")
    return log(x + sqrt(x * x - 1.0))



def atanh(x):
    if fabs(x) >= 1:
        raise ValueError("math domain error")
    return 0.5 * log((1 + x) / (1 - x))



def asin(x):
    if x < -1 or x > 1:
        raise ValueError("math domain error")
    if x == 1:
        return PI / 2
    if x == -1:
        return -PI / 2
    return atan(x / sqrt(1 - x * x))



def acos(x):
    if x < -1 or x > 1:
        raise ValueError("math domain error")
    return PI / 2 - asin(x)



def _atan_series(x):
    total = 0.0
    term = x
    x2 = x * x
    k = 1
    for _ in range(200):
        total += term / k
        term *= -x2
        k += 2
    return total



def atan(x):
    if x == 0:
        return 0.0
    neg = x < 0
    x = fabs(x)
    if x > 1:
        result = PI / 2 - atan(1 / x)
        return -result if neg else result
    if x > 0.4142135623730951:
        result = PI / 4 + _atan_series((x - 1) / (x + 1))
        return -result if neg else result
    result = _atan_series(x)
    return -result if neg else result



def atan2(y, x):
    if x > 0:
        return atan(y / x)
    if x < 0 and y >= 0:
        return atan(y / x) + PI
    if x < 0 and y < 0:
        return atan(y / x) - PI
    if x == 0 and y > 0:
        return PI / 2
    if x == 0 and y < 0:
        return -PI / 2
    return 0.0



def hypot(*coords):
    total = 0.0
    for c in coords:
        total += c * c
    return sqrt(total)



def dist(p, q):
    total = 0.0
    for a, b in zip(p, q):
        total += (a - b) ** 2
    return sqrt(total)

