from .constants import *
from .trigonometry import degrees, radians, sin, cos, tan, sinh, cosh, tanh, asinh, acosh, atanh, asin, acos, atan, atan2, hypot, dist
from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf
from .numtheory_core import factorial, gcd, lcm, isqrt


def lgamma(x):
    g = 7
    coefficients = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ]
    if x < 0.5:
        return log(PI / sin(PI * x)) - lgamma(1 - x)
    x -= 1
    a = coefficients[0]
    t = x + g + 0.5
    for i in range(1, g + 2):
        a += coefficients[i] / (x + i)
    return 0.5 * log(2 * PI) + (x + 0.5) * log(t) - t + log(a)



def gamma(x):
    if x == int(x) and x <= 0:
        raise ValueError("math domain error")
    if x == int(x) and x > 0:
        return float(factorial(int(x) - 1))
    if x < 0.5:
        return PI / (sin(PI * x) * gamma(1 - x))
    return exp(lgamma(x))



def erf(x):
    sign = 1 if x >= 0 else -1
    x = fabs(x)
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911
    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * exp(-x * x)
    return sign * y



def erfc(x):
    return 1.0 - erf(x)



def frexp(x):
    if x == 0:
        return (0.0, 0)
    neg = x < 0
    x = fabs(x)
    e = 0
    while x >= 1:
        x /= 2
        e += 1
    while x < 0.5:
        x *= 2
        e -= 1
    return (-x if neg else x, e)



def ldexp(m, e):
    return m * (2.0 ** e)



def nextafter(x, y):
    if x == y:
        return y
    eps = 2.220446049250313e-16
    if y > x:
        return x + eps * max(fabs(x), 1.0)
    return x - eps * max(fabs(x), 1.0)



def ulp(x):
    eps = 2.220446049250313e-16
    return eps * max(fabs(x), 2.2250738585072014e-308)



def signbit(x):
    return x < 0 or (x == 0 and str(x)[0] == "-")

