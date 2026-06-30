from .constants import *


def isnan(x):
    return x != x



def isinf(x):
    return x == INF or x == -INF



def isfinite(x):
    return not isnan(x) and not isinf(x)



def copysign(x, y):
    ax = x if x >= 0 else -x
    if y > 0 or (y == 0 and str(y)[0] != "-"):
        return ax
    return -ax



def fabs(x):
    return x if x >= 0 else -x



def trunc(x):
    if x >= 0:
        return int(x)
    n = int(x)
    if n == x:
        return n
    return n



def floor(x):
    n = int(x)
    if x < 0 and n != x:
        return n - 1
    return n



def ceil(x):
    n = int(x)
    if x > 0 and n != x:
        return n + 1
    return n



def fmod(x, y):
    if y == 0:
        raise ValueError("math domain error")
    q = trunc(x / y)
    r = x - q * y
    return r



def remainder(x, y):
    if y == 0:
        raise ValueError("math domain error")
    n = round(x / y)
    return x - n * y



def modf(x):
    ip = trunc(x)
    return (x - ip, float(ip))

