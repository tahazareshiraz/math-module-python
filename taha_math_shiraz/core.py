from .constants import EPSILON


def fabs(x):
    return x if x >= 0 else -x


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def copysign(x, y):
    mag = fabs(x)
    return mag if y >= 0 else -mag


def floor(x):
    n = int(x)
    if x < 0 and n != x:
        n -= 1
    return n


def ceil(x):
    n = int(x)
    if x > 0 and n != x:
        n += 1
    return n


def trunc(x):
    return int(x)


def modf(x):
    ip = trunc(x)
    return (x - ip, float(ip))


def fmod(x, y):
    if y == 0:
        raise ZeroDivisionError("fmod() division by zero")
    r = x - y * trunc(x / y)
    return r


def remainder(x, y):
    if y == 0:
        raise ZeroDivisionError("remainder() division by zero")
    q = round(x / y)
    return x - q * y


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    if a == b:
        return True
    diff = fabs(a - b)
    return diff <= max(rel_tol * max(fabs(a), fabs(b)), abs_tol)


def isnan(x):
    return x != x


def isinf(x):
    return x == float("inf") or x == float("-inf")


def isfinite(x):
    return not isnan(x) and not isinf(x)


def factorial(n):
    if not isinstance(n, int):
        raise TypeError("factorial() only accepts integral values")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a, b):
    a, b = abs(int(a)), abs(int(b))
    while b:
        a, b = b, a % b
    return a


def gcd_many(*numbers):
    if not numbers:
        return 0
    result = abs(int(numbers[0]))
    for n in numbers[1:]:
        result = gcd(result, n)
    return result


def lcm(a, b):
    a, b = abs(int(a)), abs(int(b))
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b


def lcm_many(*numbers):
    if not numbers:
        return 1
    result = abs(int(numbers[0]))
    for n in numbers[1:]:
        result = lcm(result, n)
    return result


def comb(n, k):
    if k < 0 or n < 0:
        raise ValueError("comb() not defined for negative values")
    if k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


def perm(n, k=None):
    if n < 0:
        raise ValueError("perm() not defined for negative values")
    if k is None:
        k = n
    if k < 0:
        raise ValueError("perm() not defined for negative values")
    if k > n:
        return 0
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result


def isqrt(n):
    if n < 0:
        raise ValueError("isqrt() argument must be nonnegative")
    if n == 0:
        return 0
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def is_perfect_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def clamp_int(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


def frexp(x):
    if x == 0:
        return (0.0, 0)
    neg = x < 0
    x = fabs(x)
    exponent = 0
    while x >= 1:
        x /= 2
        exponent += 1
    while x < 0.5:
        x *= 2
        exponent -= 1
    return (-x if neg else x, exponent)


def ldexp(m, e):
    return m * (2.0 ** e)


def nextafter(x, y):
    if x == y:
        return y
    if x < y:
        return x + EPSILON * max(1.0, fabs(x))
    return x - EPSILON * max(1.0, fabs(x))


def ulp(x):
    return EPSILON * max(1.0, fabs(x))


def trailing_zeros(n):
    if n == 0:
        return 0
    n = abs(int(n))
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count


def digit_sum(n):
    n = abs(int(n))
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def digit_count(n):
    n = abs(int(n))
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def reverse_digits(n):
    neg = n < 0
    n = abs(int(n))
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return -rev if neg else rev
