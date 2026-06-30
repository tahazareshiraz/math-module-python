from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf


def fsum(iterable):
    partials = []
    for x in iterable:
        i = 0
        for y in partials:
            if fabs(x) < fabs(y):
                x, y = y, x
            hi = x + y
            lo = y - (hi - x)
            if lo:
                partials[i] = lo
                i += 1
            x = hi
        partials[i:] = [x]
    return sum(partials, 0.0)



def prod(iterable, start=1):
    result = start
    for x in iterable:
        result *= x
    return result



def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    if a == b:
        return True
    if isinf(a) or isinf(b):
        return False
    diff = fabs(a - b)
    return diff <= rel_tol * max(fabs(a), fabs(b)) or diff <= abs_tol



def comb(n, k):
    n = int(n)
    k = int(k)
    if n < 0 or k < 0:
        raise ValueError("comb() not defined for negative values")
    if k > n:
        return 0
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result



def perm(n, k=None):
    n = int(n)
    if n < 0:
        raise ValueError("perm() not defined for negative values")
    if k is None:
        k = n
    k = int(k)
    if k < 0:
        raise ValueError("perm() not defined for negative values")
    if k > n:
        return 0
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result

