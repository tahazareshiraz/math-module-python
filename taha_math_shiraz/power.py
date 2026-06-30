from .constants import E, LN2, LN10, EPSILON
from .core import fabs, trunc, isclose


def sqrt(x):
    if x < 0:
        raise ValueError("math domain error")
    if x == 0:
        return 0.0
    guess = x if x >= 1 else 1.0
    for _ in range(100):
        new_guess = 0.5 * (guess + x / guess)
        if isclose(new_guess, guess, rel_tol=1e-16):
            return new_guess
        guess = new_guess
    return guess


def cbrt(x):
    if x == 0:
        return 0.0
    neg = x < 0
    x = fabs(x)
    guess = x if x >= 1 else 1.0
    for _ in range(100):
        new_guess = (2 * guess + x / (guess * guess)) / 3
        if isclose(new_guess, guess, rel_tol=1e-16):
            guess = new_guess
            break
        guess = new_guess
    return -guess if neg else guess


def nth_root(x, n):
    if n == 0:
        raise ValueError("n must not be zero")
    if x < 0 and n % 2 == 0:
        raise ValueError("math domain error")
    neg = x < 0
    x = fabs(x)
    if x == 0:
        return 0.0
    guess = x if x >= 1 else 1.0
    for _ in range(200):
        new_guess = ((n - 1) * guess + x / (guess ** (n - 1))) / n
        if isclose(new_guess, guess, rel_tol=1e-16):
            guess = new_guess
            break
        guess = new_guess
    return -guess if neg and n % 2 == 1 else guess


def _exp_small(x):
    term = 1.0
    total = 1.0
    for k in range(1, 200):
        term *= x / k
        total += term
        if fabs(term) < EPSILON * fabs(total):
            break
    return total


def exp(x):
    if x == 0:
        return 1.0
    n = trunc(x / LN2)
    r = x - n * LN2
    result = _exp_small(r)
    if n >= 0:
        for _ in range(abs(n)):
            result *= 2.0
    else:
        for _ in range(abs(n)):
            result /= 2.0
    return result


def expm1(x):
    if fabs(x) < 1e-5:
        return x + x * x / 2 + x * x * x / 6
    return exp(x) - 1.0


def _ln_small(x):
    y = (x - 1) / (x + 1)
    y2 = y * y
    term = y
    total = 0.0
    k = 1
    while True:
        contribution = term / k
        total += contribution
        if fabs(contribution) < EPSILON * (fabs(total) + 1e-300):
            break
        term *= y2
        k += 2
        if k > 1000:
            break
    return 2 * total


def log(x, base=None):
    if x <= 0:
        raise ValueError("math domain error")
    n = 0
    mantissa = x
    while mantissa >= 2:
        mantissa /= 2
        n += 1
    while mantissa < 1:
        mantissa *= 2
        n -= 1
    result = n * LN2 + _ln_small(mantissa)
    if base is not None:
        return result / log(base)
    return result


def log2(x):
    return log(x) / LN2


def log10(x):
    return log(x) / LN10


def log1p(x):
    if fabs(x) < 1e-5:
        return x - x * x / 2 + x * x * x / 3
    return log(1 + x)


def pow_(x, y):
    if y == 0:
        return 1.0
    if x == 0:
        if y > 0:
            return 0.0
        raise ZeroDivisionError("0.0 cannot be raised to a negative power")
    if x < 0:
        if isclose(y, round(y)):
            n = round(y)
            result = pow_(fabs(x), n)
            if n % 2 != 0:
                result = -result
            return result
        raise ValueError("math domain error")
    if isclose(y, round(y)) and fabs(y) < 1e6:
        n = int(round(y))
        neg = n < 0
        n = abs(n)
        result = 1.0
        base = x
        while n > 0:
            if n & 1:
                result *= base
            base *= base
            n >>= 1
        return 1.0 / result if neg else result
    return exp(y * log(x))


def hypot(*coords):
    total = 0.0
    for c in coords:
        total += c * c
    return sqrt(total)


def square(x):
    return x * x


def cube(x):
    return x * x * x


def reciprocal(x):
    if x == 0:
        raise ZeroDivisionError("reciprocal of zero")
    return 1.0 / x


def power_tower(x, n):
    if n <= 0:
        return 1.0
    result = x
    for _ in range(n - 1):
        result = pow_(x, result)
    return result


def integer_power(base, exponent):
    if exponent < 0:
        return 1.0 / integer_power(base, -exponent)
    result = 1
    while exponent > 0:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result


def is_power_of(n, base):
    if n <= 0 or base <= 1:
        return False
    while n % base == 0:
        n //= base
    return n == 1


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
