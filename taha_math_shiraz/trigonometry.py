from .constants import PI, TAU, EPSILON
from .core import fabs, trunc, isclose
from .power import sqrt


def _reduce_angle(x):
    n = trunc(x / TAU)
    r = x - n * TAU
    if r > PI:
        r -= TAU
    elif r < -PI:
        r += TAU
    return r


def sin(x):
    x = _reduce_angle(x)
    term = x
    total = x
    x2 = x * x
    k = 1
    while True:
        term *= -x2 / ((2 * k) * (2 * k + 1))
        total += term
        if fabs(term) < EPSILON * (fabs(total) + 1e-300):
            break
        k += 1
        if k > 200:
            break
    return total


def cos(x):
    x = _reduce_angle(x)
    term = 1.0
    total = 1.0
    x2 = x * x
    k = 1
    while True:
        term *= -x2 / ((2 * k - 1) * (2 * k))
        total += term
        if fabs(term) < EPSILON * (fabs(total) + 1e-300):
            break
        k += 1
        if k > 200:
            break
    return total


def tan(x):
    c = cos(x)
    if fabs(c) < 1e-15:
        raise ValueError("math domain error")
    return sin(x) / c


def sec(x):
    c = cos(x)
    if fabs(c) < 1e-15:
        raise ValueError("math domain error")
    return 1.0 / c


def csc(x):
    s = sin(x)
    if fabs(s) < 1e-15:
        raise ValueError("math domain error")
    return 1.0 / s


def cot(x):
    s = sin(x)
    if fabs(s) < 1e-15:
        raise ValueError("math domain error")
    return cos(x) / s


def asin(x):
    if x < -1 or x > 1:
        raise ValueError("math domain error")
    if isclose(x, 1.0):
        return PI / 2
    if isclose(x, -1.0):
        return -PI / 2
    guess = x
    for _ in range(100):
        f = sin(guess) - x
        fp = cos(guess)
        if fabs(fp) < 1e-15:
            break
        new_guess = guess - f / fp
        if isclose(new_guess, guess, rel_tol=1e-15):
            guess = new_guess
            break
        guess = new_guess
    return guess


def acos(x):
    if x < -1 or x > 1:
        raise ValueError("math domain error")
    return PI / 2 - asin(x)


def _atan_series(x):
    if fabs(x) > 1:
        sign = 1 if x > 0 else -1
        return sign * (PI / 2) - _atan_series(1 / x)
    term = x
    total = x
    x2 = x * x
    k = 1
    while True:
        term *= -x2
        contribution = term / (2 * k + 1)
        total += contribution
        if fabs(contribution) < EPSILON * (fabs(total) + 1e-300):
            break
        k += 1
        if k > 1000:
            break
    return total


def atan(x):
    if fabs(x) <= 1:
        return _atan_series(x)
    sign = 1 if x > 0 else -1
    return sign * PI / 2 - _atan_series(1 / x)


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


def degrees(x):
    return x * 180.0 / PI


def radians(x):
    return x * PI / 180.0


def sinc(x):
    if x == 0:
        return 1.0
    return sin(PI * x) / (PI * x)


def versin(x):
    return 1 - cos(x)


def coversin(x):
    return 1 - sin(x)


def haversine(x):
    return (1 - cos(x)) / 2


def haversine_distance(lat1, lon1, lat2, lon2, radius=6371000):
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = haversine(dphi) + cos(phi1) * cos(phi2) * haversine(dlambda)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return radius * c


def exsec(x):
    return sec(x) - 1


def excsc(x):
    return csc(x) - 1
