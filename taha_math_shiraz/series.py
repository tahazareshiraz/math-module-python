from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf
from .numtheory_core import factorial, gcd, lcm, isqrt


def arithmetic_series_sum(a1, d, n):
    return n * (2 * a1 + (n - 1) * d) / 2.0



def geometric_series_sum(a1, r, n):
    if r == 1:
        return a1 * n
    return a1 * (1 - r ** n) / (1 - r)



def infinite_geometric_series_sum(a1, r):
    if fabs(r) >= 1:
        raise ValueError("series does not converge")
    return a1 / (1 - r)

