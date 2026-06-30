import struct

__version__ = "3.0.0"

pi = 3.14159265358979323846
e = 2.71828182845904523536
tau = 2 * pi
inf = float("inf")
nan = float("nan")
phi = 1.61803398874989484820
sqrt2 = 1.41421356237309504880
sqrt3 = 1.73205080756887729352
ln2 = 0.69314718055994530942
ln10 = 2.30258509299404568402
euler_gamma = 0.57721566490153286061
catalan = 0.91596559417721901505


def _check(x):
    if not isinstance(x, (int, float)):
        raise TypeError("must be real number, not %s" % type(x).__name__)


def fabs(x):
    _check(x)
    return float(x) if x >= 0 else float(-x)


def floor(x):
    _check(x)
    i = int(x)
    if x < 0 and i != x:
        i -= 1
    return i


def ceil(x):
    _check(x)
    i = int(x)
    if x > 0 and i != x:
        i += 1
    return i


def trunc(x):
    _check(x)
    return int(x)


def isnan(x):
    return x != x


def isinf(x):
    return x == inf or x == -inf


def isfinite(x):
    return not (isnan(x) or isinf(x))


def copysign(x, y):
    x = fabs(x)
    return x if y >= 0 or y != y else -x


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def lerp(a, b, t):
    return a + (b - a) * t


def smoothstep(a, b, x):
    t = clamp((x - a) / (b - a), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    if a == b:
        return True
    if isinf(a) or isinf(b):
        return False
    diff = fabs(a - b)
    return diff <= max(rel_tol * max(fabs(a), fabs(b)), abs_tol)


def pow(x, y):
    _check(x)
    _check(y)
    if y == 0:
        return 1.0
    if isinstance(y, int) or y == int(y):
        n = int(y)
        neg = n < 0
        n = abs(n)
        result = 1.0
        base = float(x)
        while n > 0:
            if n & 1:
                result *= base
            base *= base
            n >>= 1
        return 1.0 / result if neg else result
    if x < 0:
        raise ValueError("math domain error")
    return exp(y * log(x))


def sqrt(x):
    _check(x)
    if x < 0:
        raise ValueError("math domain error")
    if x == 0:
        return 0.0
    guess = x
    for _ in range(100):
        ng = 0.5 * (guess + x / guess)
        if fabs(ng - guess) < 1e-15:
            return ng
        guess = ng
    return guess


def cbrt(x):
    _check(x)
    if x == 0:
        return 0.0
    neg = x < 0
    x = fabs(x)
    guess = x
    for _ in range(100):
        ng = (2 * guess + x / (guess * guess)) / 3
        if fabs(ng - guess) < 1e-15:
            guess = ng
            break
        guess = ng
    return -guess if neg else guess


def isqrt(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("isqrt() argument must be a nonnegative integer")
    if n == 0:
        return 0
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def hypot(*coords):
    return sqrt(sum(c * c for c in coords))


def dist(p, q):
    return sqrt(sum((a - b) ** 2 for a, b in zip(p, q)))


def nth_root(x, n):
    if n == 0:
        raise ValueError("math domain error")
    if x < 0 and n % 2 == 0:
        raise ValueError("math domain error")
    neg = x < 0
    x = fabs(x)
    result = pow(x, 1.0 / n)
    return -result if neg else result


def exp(x):
    _check(x)
    if x == 0:
        return 1.0
    neg = x < 0
    x = fabs(x)
    n = int(x) + 1
    xn = x / n
    term = 1.0
    result = 1.0
    for i in range(1, 200):
        term *= xn / i
        result += term
        if fabs(term) < 1e-18:
            break
    result = pow(result, n)
    return 1.0 / result if neg else result


def exp2(x):
    return pow(2.0, x)


def exp10(x):
    return pow(10.0, x)


def expm1(x):
    return exp(x) - 1


def log(x, base=None):
    _check(x)
    if x <= 0:
        raise ValueError("math domain error")
    k = 0
    while x > 1.5:
        x /= e
        k += 1
    while x < 0.5:
        x *= e
        k -= 1
    y = x - 1
    term = y
    result = 0.0
    for n in range(1, 300):
        result += term / n if n % 2 else -term / n
        term *= y
        if fabs(term) < 1e-18:
            break
    result += k
    if base is not None:
        return result / log(base)
    return result


def log2(x):
    return log(x, 2)


def log10(x):
    return log(x, 10)


def log1p(x):
    return log(1 + x)


def logb(x, b):
    return log(x, b)


def _atan_series(x):
    term = x
    result = 0.0
    x2 = x * x
    n = 0
    while fabs(term) > 1e-18 and n < 10000:
        result += term / (2 * n + 1) if n % 2 == 0 else -term / (2 * n + 1)
        term *= x2
        n += 1
    return result


def atan(x):
    _check(x)
    neg = x < 0
    x = fabs(x)
    flip = x > 1
    if flip:
        x = 1 / x
    halvings = 0
    while x > 0.4:
        x = x / (1 + sqrt(1 + x * x))
        halvings += 1
    result = _atan_series(x) * (2 ** halvings)
    if flip:
        result = pi / 2 - result
    return -result if neg else result


def atan2(y, x):
    if x > 0:
        return atan(y / x)
    if x < 0 and y >= 0:
        return atan(y / x) + pi
    if x < 0 and y < 0:
        return atan(y / x) - pi
    if x == 0 and y > 0:
        return pi / 2
    if x == 0 and y < 0:
        return -pi / 2
    return 0.0


def _reduce_angle(x):
    while x > pi:
        x -= tau
    while x < -pi:
        x += tau
    return x


def sin(x):
    _check(x)
    x = _reduce_angle(x)
    term = x
    result = 0.0
    for n in range(1, 50):
        result += term
        term *= -x * x / ((2 * n) * (2 * n + 1))
        if fabs(term) < 1e-18:
            break
    return result


def cos(x):
    _check(x)
    x = _reduce_angle(x)
    term = 1.0
    result = 0.0
    for n in range(1, 50):
        result += term
        term *= -x * x / ((2 * n - 1) * (2 * n))
        if fabs(term) < 1e-18:
            break
    return result


def tan(x):
    c = cos(x)
    if fabs(c) < 1e-15:
        raise ValueError("math domain error")
    return sin(x) / c


def cot(x):
    s = sin(x)
    if fabs(s) < 1e-15:
        raise ValueError("math domain error")
    return cos(x) / s


def sec(x):
    c = cos(x)
    if fabs(c) < 1e-15:
        raise ValueError("math domain error")
    return 1 / c


def csc(x):
    s = sin(x)
    if fabs(s) < 1e-15:
        raise ValueError("math domain error")
    return 1 / s


def asin(x):
    if x < -1 or x > 1:
        raise ValueError("math domain error")
    if fabs(x) == 1:
        return copysign(pi / 2, x)
    return atan(x / sqrt(1 - x * x))


def acos(x):
    if x < -1 or x > 1:
        raise ValueError("math domain error")
    return pi / 2 - asin(x)


def acot(x):
    return pi / 2 - atan(x)


def asec(x):
    if fabs(x) < 1:
        raise ValueError("math domain error")
    return acos(1 / x)


def acsc(x):
    if fabs(x) < 1:
        raise ValueError("math domain error")
    return asin(1 / x)


def degrees(x):
    return x * 180.0 / pi


def radians(x):
    return x * pi / 180.0


def deg2rad(x):
    return radians(x)


def rad2deg(x):
    return degrees(x)


def sinh(x):
    return (exp(x) - exp(-x)) / 2


def cosh(x):
    return (exp(x) + exp(-x)) / 2


def tanh(x):
    a = exp(2 * x)
    return (a - 1) / (a + 1)


def coth(x):
    return 1 / tanh(x)


def sech(x):
    return 1 / cosh(x)


def csch(x):
    return 1 / sinh(x)


def asinh(x):
    return log(x + sqrt(x * x + 1))


def acosh(x):
    if x < 1:
        raise ValueError("math domain error")
    return log(x + sqrt(x * x - 1))


def atanh(x):
    if x <= -1 or x >= 1:
        raise ValueError("math domain error")
    return 0.5 * log((1 + x) / (1 - x))


def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def double_factorial(n):
    if n < 0:
        raise ValueError("double_factorial() not defined for negative values")
    result = 1
    while n > 1:
        result *= n
        n -= 2
    return result


def subfactorial(n):
    if n < 0:
        raise ValueError("subfactorial() not defined for negative values")
    if n == 0:
        return 1
    result = 0
    for k in range(n + 1):
        result += ((-1) ** k) * factorial(n) // factorial(k)
    return result


def gcd(*nums):
    if not nums:
        return 0
    result = 0
    for n in nums:
        n = abs(n)
        while n:
            result, n = n, result % n
    return result


def lcm(*nums):
    if not nums:
        return 1
    result = 1
    for n in nums:
        if n == 0:
            return 0
        result = result * abs(n) // gcd(result, n)
    return result


def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def comb(n, k):
    if k < 0 or n < 0:
        raise ValueError("negative values not allowed")
    if k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


def perm(n, k=None):
    if n < 0 or (k is not None and k < 0):
        raise ValueError("negative values not allowed")
    if k is None:
        k = n
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i)
    return result


def multinomial(n, *ks):
    if sum(ks) != n:
        raise ValueError("sum of ks must equal n")
    result = factorial(n)
    for k in ks:
        result //= factorial(k)
    return result


def catalan_number(n):
    if n < 0:
        raise ValueError("catalan_number() not defined for negative values")
    return comb(2 * n, n) // (n + 1)


def stirling_second(n, k):
    if k == 0 and n == 0:
        return 1
    if k == 0 or k > n:
        return 0
    if k == n:
        return 1
    return k * stirling_second(n - 1, k) + stirling_second(n - 1, k - 1)


def stirling_first(n, k):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return stirling_first(n - 1, k - 1) - (n - 1) * stirling_first(n - 1, k)


def bell_number(n):
    bell = [[0] * (n + 1) for _ in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
    return bell[n][0]


def partition_count(n):
    if n < 0:
        return 0
    p = [0] * (n + 1)
    p[0] = 1
    for k in range(1, n + 1):
        for v in range(k, n + 1):
            p[v] += p[v - k]
    return p[n]


def binomial_coefficient_row(n):
    return [comb(n, k) for k in range(n + 1)]


def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def next_prime(n):
    candidate = int(n) + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def prev_prime(n):
    candidate = int(n) - 1
    while candidate > 1 and not is_prime(candidate):
        candidate -= 1
    if candidate <= 1:
        raise ValueError("no prime before given number")
    return candidate


def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, isqrt(limit) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return [i for i, v in enumerate(is_p) if v]


def prime_factors(n):
    n = abs(n)
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def prime_factorization(n):
    factors = prime_factors(n)
    result = {}
    for f in factors:
        result[f] = result.get(f, 0) + 1
    return result


def divisors(n):
    n = abs(n)
    small = []
    large = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
        i += 1
    return sorted(small + large)


def divisor_count(n):
    return len(divisors(n))


def divisor_sum(n):
    return sum(divisors(n))


def is_perfect(n):
    if n < 2:
        return False
    return divisor_sum(n) - n == n


def is_abundant(n):
    return divisor_sum(n) - n > n


def is_deficient(n):
    return divisor_sum(n) - n < n


def euler_totient(n):
    result = n
    p = 2
    nn = n
    while p * p <= nn:
        if nn % p == 0:
            while nn % p == 0:
                nn //= p
            result -= result // p
        p += 1
    if nn > 1:
        result -= result // nn
    return result


def mobius(n):
    if n == 1:
        return 1
    factors = prime_factorization(n)
    for p, exp_ in factors.items():
        if exp_ > 1:
            return 0
    return (-1) ** len(factors)


def is_coprime(a, b):
    return gcd(a, b) == 1


def fibonacci(n):
    if n < 0:
        raise ValueError("fibonacci() not defined for negative values")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_sequence(count):
    seq = []
    a, b = 0, 1
    for _ in range(count):
        seq.append(a)
        a, b = b, a + b
    return seq


def lucas_number(n):
    if n < 0:
        raise ValueError("lucas_number() not defined for negative values")
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def triangular_number(n):
    return n * (n + 1) // 2


def square_number(n):
    return n * n


def pentagonal_number(n):
    return n * (3 * n - 1) // 2


def hexagonal_number(n):
    return n * (2 * n - 1)


def is_perfect_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def digit_sum(n):
    return sum(int(d) for d in str(abs(int(n))))


def digit_product(n):
    result = 1
    for d in str(abs(int(n))):
        result *= int(d)
    return result


def digital_root(n):
    n = abs(int(n))
    while n >= 10:
        n = digit_sum(n)
    return n


def is_palindrome_number(n):
    s = str(abs(int(n)))
    return s == s[::-1]


def reverse_number(n):
    neg = n < 0
    r = int(str(abs(int(n)))[::-1])
    return -r if neg else r


def to_base(n, base):
    if base < 2 or base > 36:
        raise ValueError("base must be between 2 and 36")
    if n == 0:
        return "0"
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    neg = n < 0
    n = abs(n)
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return ("-" + result) if neg else result


def from_base(s, base):
    return int(s, base)


def fsum(iterable):
    total = 0.0
    c = 0.0
    for x in iterable:
        y = x - c
        t = total + y
        c = (t - total) - y
        total = t
    return total


def prod(iterable, start=1):
    result = start
    for x in iterable:
        result *= x
    return result


def sumprod(p, q):
    return fsum(a * b for a, b in zip(p, q))


def remainder(x, y):
    return x - y * round(x / y)


def fmod(x, y):
    if y == 0:
        raise ValueError("math domain error")
    return x - int(x / y) * y


def modf(x):
    i = trunc(x)
    return (x - i, float(i))


def average(iterable):
    data = list(iterable)
    if not data:
        raise ValueError("average() arg is an empty sequence")
    return fsum(data) / len(data)


def mean(iterable):
    return average(iterable)


def geometric_mean(iterable):
    data = list(iterable)
    if not data:
        raise ValueError("geometric_mean() arg is an empty sequence")
    return exp(fsum(log(x) for x in data) / len(data))


def harmonic_mean(iterable):
    data = list(iterable)
    if not data:
        raise ValueError("harmonic_mean() arg is an empty sequence")
    return len(data) / fsum(1 / x for x in data)


def variance(iterable, ddof=0):
    data = list(iterable)
    m = average(data)
    n = len(data)
    return fsum((x - m) ** 2 for x in data) / (n - ddof)


def stdev(iterable, ddof=1):
    return sqrt(variance(iterable, ddof))


def pvariance(iterable):
    return variance(iterable, 0)


def pstdev(iterable):
    return sqrt(pvariance(iterable))


def median(iterable):
    data = sorted(iterable)
    n = len(data)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]


def mode(iterable):
    data = list(iterable)
    if not data:
        raise ValueError("mode() arg is an empty sequence")
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    best = data[0]
    best_count = 0
    for x, c in counts.items():
        if c > best_count:
            best = x
            best_count = c
    return best


def percentile(iterable, p):
    data = sorted(iterable)
    n = len(data)
    if n == 0:
        raise ValueError("percentile() arg is an empty sequence")
    if p <= 0:
        return data[0]
    if p >= 100:
        return data[-1]
    k = (n - 1) * p / 100
    f = floor(k)
    c = ceil(k)
    if f == c:
        return data[int(k)]
    return data[f] * (c - k) + data[c] * (k - f)


def covariance(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("x and y must be the same length")
    mx, my = average(x), average(y)
    return fsum((a - mx) * (b - my) for a, b in zip(x, y)) / n


def correlation(x, y):
    sx, sy = pstdev(x), pstdev(y)
    if sx == 0 or sy == 0:
        raise ValueError("correlation requires non-constant input")
    return covariance(x, y) / (sx * sy)


def linear_regression(x, y):
    n = len(x)
    mx, my = average(x), average(y)
    num = fsum((a - mx) * (b - my) for a, b in zip(x, y))
    den = fsum((a - mx) ** 2 for a in x)
    if den == 0:
        raise ValueError("cannot fit a line through vertical data")
    slope = num / den
    intercept = my - slope * mx
    return slope, intercept


def range_(iterable):
    data = list(iterable)
    return max(data) - min(data)


def z_score(x, data):
    m = average(data)
    s = pstdev(data)
    if s == 0:
        raise ValueError("z_score requires non-constant input")
    return (x - m) / s


def quartiles(iterable):
    return (percentile(iterable, 25), percentile(iterable, 50), percentile(iterable, 75))


def iqr(iterable):
    q1, _, q3 = quartiles(iterable)
    return q3 - q1


def frexp(x):
    if x == 0:
        return (0.0, 0)
    packed = struct.pack(">d", x)
    bits = struct.unpack(">Q", packed)[0]
    sign_bit = bits >> 63
    exponent = (bits >> 52) & 0x7FF
    mantissa = bits & ((1 << 52) - 1)
    if exponent == 0:
        m = mantissa / (1 << 52)
        e2 = -1022
    else:
        m = 1.0 + mantissa / (1 << 52)
        e2 = exponent - 1023
    m = m / 2
    e2 = e2 + 1
    if sign_bit:
        m = -m
    return (m, e2)


def ldexp(m, e2):
    return m * pow(2.0, e2)


def nextafter(x, y):
    if x == y:
        return y
    if x == 0:
        smallest = struct.unpack(">d", struct.pack(">Q", 1))[0]
        return smallest if y > 0 else -smallest
    bits = struct.unpack(">Q", struct.pack(">d", fabs(x)))[0]
    if (y > x) == (x > 0) or (x < 0 and y > x):
        if y > x:
            bits += 1
        else:
            bits -= 1
    else:
        bits -= 1 if y < x else -1
    result = struct.unpack(">d", struct.pack(">Q", bits))[0]
    return -result if x < 0 else result


def ulp(x):
    x = fabs(x)
    if x == 0:
        return struct.unpack(">d", struct.pack(">Q", 1))[0]
    if isinf(x) or isnan(x):
        return x
    n = nextafter(x, inf)
    return n - x


def _lanczos_gamma(x):
    g = 7
    coeffs = [
        0.99999999999980993, 676.5203681218851, -1259.1392167224028,
        771.32342877765313, -176.61502916214059, 12.507343278686905,
        -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7
    ]
    if x < 0.5:
        return pi / (sin(pi * x) * _lanczos_gamma(1 - x))
    x -= 1
    a = coeffs[0]
    t = x + g + 0.5
    for i in range(1, g + 2):
        a += coeffs[i] / (x + i)
    return sqrt(2 * pi) * pow(t, x + 0.5) * exp(-t) * a


def gamma(x):
    _check(x)
    if x == int(x) and x <= 0:
        raise ValueError("math domain error")
    if x == int(x) and x > 0:
        return float(factorial(int(x) - 1))
    return _lanczos_gamma(x)


def lgamma(x):
    g = gamma(x)
    return log(fabs(g))


def beta(a, b):
    return gamma(a) * gamma(b) / gamma(a + b)


def digamma(x, h=1e-6):
    return (lgamma(x + h) - lgamma(x - h)) / (2 * h)


def erf(x):
    _check(x)
    neg = x < 0
    x = fabs(x)
    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429
    p = 0.3275911
    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * exp(-x * x)
    return -y if neg else y


def erfc(x):
    return 1.0 - erf(x)


def normal_pdf(x, mu=0.0, sigma=1.0):
    return exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * sqrt(2 * pi))


def normal_cdf(x, mu=0.0, sigma=1.0):
    return 0.5 * (1 + erf((x - mu) / (sigma * sqrt(2))))


def vec_add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def vec_sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def vec_scale(u, k):
    return tuple(a * k for a in u)


def vec_dot(u, v):
    return fsum(a * b for a, b in zip(u, v))


def vec_cross(u, v):
    if len(u) != 3 or len(v) != 3:
        raise ValueError("cross product requires 3-dimensional vectors")
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    )


def vec_norm(u):
    return sqrt(vec_dot(u, u))


def vec_normalize(u):
    n = vec_norm(u)
    if n == 0:
        raise ValueError("cannot normalize zero vector")
    return tuple(a / n for a in u)


def vec_angle(u, v):
    return acos(clamp(vec_dot(u, v) / (vec_norm(u) * vec_norm(v)), -1.0, 1.0))


def vec_project(u, v):
    k = vec_dot(u, v) / vec_dot(v, v)
    return vec_scale(v, k)


def vec_lerp(u, v, t):
    return tuple(lerp(a, b, t) for a, b in zip(u, v))


def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_scale(A, k):
    return [[A[i][j] * k for j in range(len(A[0]))] for i in range(len(A))]


def matrix_mul(A, B):
    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])
    if cols_a != rows_b:
        raise ValueError("incompatible matrix dimensions")
    result = [[0.0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = fsum(A[i][k] * B[k][j] for k in range(cols_a))
    return result


def matrix_transpose(A):
    return [list(row) for row in zip(*A)]


def matrix_identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def matrix_trace(A):
    return fsum(A[i][i] for i in range(len(A)))


def matrix_minor(A, i, j):
    return [row[:j] + row[j + 1:] for k, row in enumerate(A) if k != i]


def matrix_det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0.0
    for j in range(n):
        det += ((-1) ** j) * A[0][j] * matrix_det(matrix_minor(A, 0, j))
    return det


def matrix_cofactor(A):
    n = len(A)
    return [[((-1) ** (i + j)) * matrix_det(matrix_minor(A, i, j)) for j in range(n)] for i in range(n)]


def matrix_adjugate(A):
    return matrix_transpose(matrix_cofactor(A))


def matrix_inverse(A):
    det = matrix_det(A)
    if fabs(det) < 1e-14:
        raise ValueError("matrix is singular")
    adj = matrix_adjugate(A)
    n = len(A)
    return [[adj[i][j] / det for j in range(n)] for i in range(n)]


def matrix_vec_mul(A, v):
    return tuple(fsum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A)))


def matrix_rank(A):
    M = [row[:] for row in A]
    rows, cols = len(M), len(M[0])
    rank = 0
    for col in range(cols):
        pivot = None
        for r in range(rank, rows):
            if fabs(M[r][col]) > 1e-12:
                pivot = r
                break
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        for r in range(rows):
            if r != rank and fabs(M[r][col]) > 1e-14:
                factor = M[r][col] / M[rank][col]
                M[r] = [M[r][c] - factor * M[rank][c] for c in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def solve_linear_system(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: fabs(M[r][col]))
        if fabs(M[pivot][col]) < 1e-14:
            raise ValueError("system has no unique solution")
        M[col], M[pivot] = M[pivot], M[col]
        for r in range(n):
            if r != col:
                factor = M[r][col] / M[col][col]
                M[r] = [M[r][c] - factor * M[col][c] for c in range(n + 1)]
    return [M[i][n] / M[i][i] for i in range(n)]


def complex_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def complex_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def complex_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def complex_div(a, b):
    denom = b[0] * b[0] + b[1] * b[1]
    if denom == 0:
        raise ZeroDivisionError("complex division by zero")
    return ((a[0] * b[0] + a[1] * b[1]) / denom, (a[1] * b[0] - a[0] * b[1]) / denom)


def complex_abs(a):
    return hypot(a[0], a[1])


def complex_conjugate(a):
    return (a[0], -a[1])


def complex_arg(a):
    return atan2(a[1], a[0])


def complex_from_polar(r, theta):
    return (r * cos(theta), r * sin(theta))


def complex_to_polar(a):
    return (complex_abs(a), complex_arg(a))


def complex_pow(a, n):
    r, theta = complex_to_polar(a)
    rn = pow(r, n)
    return complex_from_polar(rn, theta * n)


def complex_sqrt(a):
    return complex_pow(a, 0.5)


def circle_area(r):
    return pi * r * r


def circle_circumference(r):
    return 2 * pi * r


def sphere_volume(r):
    return (4 / 3) * pi * r ** 3


def sphere_surface_area(r):
    return 4 * pi * r * r


def cylinder_volume(r, h):
    return pi * r * r * h


def cylinder_surface_area(r, h):
    return 2 * pi * r * (r + h)


def cone_volume(r, h):
    return (1 / 3) * pi * r * r * h


def cone_surface_area(r, slant_height):
    return pi * r * (r + slant_height)


def triangle_area(base, height):
    return 0.5 * base * height


def triangle_area_heron(a, b, c):
    s = (a + b + c) / 2
    val = s * (s - a) * (s - b) * (s - c)
    if val < 0:
        raise ValueError("invalid triangle sides")
    return sqrt(val)


def triangle_area_coords(p1, p2, p3):
    return fabs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2)

def rectangle_area(w, h):
    return w * h


def rectangle_perimeter(w, h):
    return 2 * (w + h)


def trapezoid_area(a, b, h):
    return (a + b) * h / 2


def regular_polygon_area(n, side):
    return (n * side * side) / (4 * tan(pi / n))


def regular_polygon_perimeter(n, side):
    return n * side


def ellipse_area(a, b):
    return pi * a * b


def ellipse_circumference_approx(a, b):
    return pi * (3 * (a + b) - sqrt((3 * a + b) * (a + 3 * b)))


def polygon_area_shoelace(points):
    n = len(points)
    s = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return fabs(s) / 2


def polygon_perimeter(points):
    n = len(points)
    return fsum(dist(points[i], points[(i + 1) % n]) for i in range(n))


def point_distance(p1, p2):
    return dist(p1, p2)


def midpoint(p1, p2):
    return tuple((a + b) / 2 for a, b in zip(p1, p2))


def slope(p1, p2):
    if p2[0] == p1[0]:
        raise ValueError("undefined slope for vertical line")
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def line_intersection(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if fabs(denom) < 1e-14:
        raise ValueError("lines are parallel")
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (px, py)


def degrees_to_dms(deg):
    d = int(deg)
    m_float = fabs(deg - d) * 60
    m = int(m_float)
    s = (m_float - m) * 60
    return (d, m, s)


def dms_to_degrees(d, m, s):
    sign_ = -1 if d < 0 else 1
    return sign_ * (fabs(d) + m / 60 + s / 3600)


def haversine_distance(lat1, lon1, lat2, lon2, radius=6371.0):
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return radius * c


def polynomial_eval(coeffs, x):
    result = 0.0
    for c in reversed(coeffs):
        result = result * x + c
    return result


def polynomial_derivative(coeffs):
    if len(coeffs) <= 1:
        return [0.0]
    return [coeffs[i] * i for i in range(1, len(coeffs))]


def polynomial_integral(coeffs, constant=0.0):
    return [constant] + [coeffs[i] / (i + 1) for i in range(len(coeffs))]


def polynomial_add(p, q):
    n = max(len(p), len(q))
    p = p + [0.0] * (n - len(p))
    q = q + [0.0] * (n - len(q))
    return [a + b for a, b in zip(p, q)]


def polynomial_mul(p, q):
    result = [0.0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result


def bisection(f, a, b, tol=1e-12, max_iter=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(max_iter):
        m = (a + b) / 2
        fm = f(m)
        if fabs(fm) < tol or (b - a) / 2 < tol:
            return m
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2


def newton_raphson(f, fprime, x0, tol=1e-12, max_iter=200):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if fabs(fx) < tol:
            return x
        dfx = fprime(x)
        if dfx == 0:
            raise ZeroDivisionError("derivative is zero")
        x = x - fx / dfx
    return x


def secant_method(f, x0, x1, tol=1e-12, max_iter=200):
    for _ in range(max_iter):
        f0, f1 = f(x0), f(x1)
        if f1 - f0 == 0:
            raise ZeroDivisionError("division by zero in secant method")
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if fabs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1


def fixed_point_iteration(g, x0, tol=1e-12, max_iter=500):
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if fabs(x_new - x) < tol:
            return x_new
        x = x_new
    return x


def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def second_derivative(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


def partial_derivative(f, point, index, h=1e-6):
    p1 = list(point)
    p2 = list(point)
    p1[index] += h
    p2[index] -= h
    return (f(*p1) - f(*p2)) / (2 * h)


def gradient(f, point, h=1e-6):
    return tuple(partial_derivative(f, point, i, h) for i in range(len(point)))


def integrate_trapezoid(f, a, b, n=1000):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def integrate_simpson(f, a, b, n=1000):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        total += (4 if i % 2 else 2) * f(x)
    return total * h / 3


def integrate_midpoint(f, a, b, n=1000):
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        total += f(a + (i + 0.5) * h)
    return total * h


def arc_length(f, a, b, n=1000):
    return integrate_simpson(lambda x: sqrt(1 + derivative(f, x) ** 2), a, b, n)


def taylor_series_exp(x, terms=20):
    return fsum(pow(x, k) / factorial(k) for k in range(terms))


def taylor_series_sin(x, terms=20):
    return fsum(((-1) ** k) * pow(x, 2 * k + 1) / factorial(2 * k + 1) for k in range(terms))


def taylor_series_cos(x, terms=20):
    return fsum(((-1) ** k) * pow(x, 2 * k) / factorial(2 * k) for k in range(terms))


class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        g = gcd(numerator, denominator) or 1
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __add__(self, other):
        other = self._coerce(other)
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __sub__(self, other):
        other = self._coerce(other)
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(self, other):
        other = self._coerce(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        other = self._coerce(other)
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        other = self._coerce(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        other = self._coerce(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __float__(self):
        return self.numerator / self.denominator

    def __repr__(self):
        return "Fraction(%d, %d)" % (self.numerator, self.denominator)

    @staticmethod
    def _coerce(other):
        if isinstance(other, Fraction):
            return other
        if isinstance(other, int):
            return Fraction(other, 1)
        raise TypeError("unsupported operand type for Fraction")

    @staticmethod
    def from_float(x, max_denominator=1000000):
        n, d = continued_fraction_to_rational(continued_fraction(x), max_denominator)
        return Fraction(n, d)


def continued_fraction(x, terms=20):
    result = []
    for _ in range(terms):
        a = floor(x)
        result.append(a)
        frac = x - a
        if fabs(frac) < 1e-14:
            break
        x = 1 / frac
    return result


def continued_fraction_to_rational(cf, max_denominator=1000000):
    n0, d0 = 1, 0
    n1, d1 = cf[0], 1
    for a in cf[1:]:
        n0, n1 = n1, a * n1 + n0
        d0, d1 = d1, a * d1 + d0
        if d1 > max_denominator:
            break
    return n1, d1


def rational_approx(x, max_denominator=1000000):
    cf = continued_fraction(x)
    return continued_fraction_to_rational(cf, max_denominator)


def simplify_fraction(n, d):
    g = gcd(n, d) or 1
    return n // g, d // g


def gcd_lcm_pair(a, b):
    g = gcd(a, b)
    l = lcm(a, b)
    return g, l


def is_pythagorean_triple(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


def pythagorean_triples(limit):
    triples = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c2 = a * a + b * b
            c = isqrt(c2)
            if c * c == c2 and c <= limit:
                triples.append((a, b, c))
    return triples


def quadratic_roots(a, b, c):
    if a == 0:
        if b == 0:
            raise ValueError("not a valid equation")
        return (-c / b,)
    disc = b * b - 4 * a * c
    if disc < 0:
        real = -b / (2 * a)
        imag = sqrt(-disc) / (2 * a)
        return ((real, imag), (real, -imag))
    if disc == 0:
        return (-b / (2 * a),)
    sq = sqrt(disc)
    return ((-b + sq) / (2 * a), (-b - sq) / (2 * a))


def cubic_roots(a, b, c, d):
    b /= a
    c /= a
    d /= a
    p = c - b * b / 3
    q = 2 * b ** 3 / 27 - b * c / 3 + d
    disc = (q / 2) ** 2 + (p / 3) ** 3
    roots = []
    if disc >= 0:
        sq = sqrt(disc)
        u = cbrt(-q / 2 + sq)
        v = cbrt(-q / 2 - sq)
        roots.append(u + v - b / 3)
    else:
        r = sqrt(-(p ** 3) / 27)
        phi_ = acos(clamp(-q / (2 * r), -1.0, 1.0))
        m = 2 * sqrt(-p / 3)
        for k in range(3):
            roots.append(m * cos((phi_ + 2 * pi * k) / 3) - b / 3)
    return roots


def distance_point_to_line(point, line_p1, line_p2):
    x0, y0 = point
    x1, y1 = line_p1
    x2, y2 = line_p2
    num = fabs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    den = dist(line_p1, line_p2)
    return num / den


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


def meters_to_feet(m):
    return m * 3.280839895


def feet_to_meters(ft):
    return ft / 3.280839895


def kilometers_to_miles(km):
    return km * 0.621371192


def miles_to_kilometers(mi):
    return mi / 0.621371192


def kilograms_to_pounds(kg):
    return kg * 2.20462262185


def pounds_to_kilograms(lb):
    return lb / 2.20462262185


def liters_to_gallons(l):
    return l * 0.264172052


def gallons_to_liters(g):
    return g / 0.264172052


def joules_to_calories(j):
    return j / 4.184


def calories_to_joules(cal):
    return cal * 4.184


def bytes_to_kilobytes(b):
    return b / 1024


def bytes_to_megabytes(b):
    return b / (1024 ** 2)


def bytes_to_gigabytes(b):
    return b / (1024 ** 3)


def ease_in_quad(t):
    return t * t


def ease_out_quad(t):
    return 1 - (1 - t) * (1 - t)


def ease_in_out_quad(t):
    return 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2


def ease_in_cubic(t):
    return t ** 3


def ease_out_cubic(t):
    return 1 - pow(1 - t, 3)


def ease_in_out_cubic(t):
    return 4 * t ** 3 if t < 0.5 else 1 - pow(-2 * t + 2, 3) / 2


def ease_in_sine(t):
    return 1 - cos((t * pi) / 2)


def ease_out_sine(t):
    return sin((t * pi) / 2)


def ease_in_out_sine(t):
    return -(cos(pi * t) - 1) / 2


def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def wrap_angle(theta):
    return atan2(sin(theta), cos(theta))


def angle_difference(a, b):
    return wrap_angle(a - b)


def normalize_angle_degrees(deg):
    return deg % 360


def is_angle_between(theta, start, end):
    theta = normalize_angle_degrees(theta)
    start = normalize_angle_degrees(start)
    end = normalize_angle_degrees(end)
    if start <= end:
        return start <= theta <= end
    return theta >= start or theta <= end


def interpolate_linear(points, x):
    points = sorted(points)
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        if x0 <= x <= x1:
            t = (x - x0) / (x1 - x0)
            return lerp(y0, y1, t)
    raise ValueError("x is out of interpolation range")


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
    coef = [p[1] for p in points]
    table = [coef[:]]
    for i in range(1, n):
        row = []
        prev = table[i - 1]
        for j in range(n - i):
            row.append((prev[j + 1] - prev[j]) / (xs[j + i] - xs[j]))
        table.append(row)
    result = table[0][0]
    product = 1.0
    for i in range(1, n):
        product *= (x - xs[i - 1])
        result += table[i][0] * product
    return result


def weighted_average(values, weights):
    if len(values) != len(weights):
        raise ValueError("values and weights must be same length")
    total_weight = fsum(weights)
    if total_weight == 0:
        raise ValueError("sum of weights cannot be zero")
    return fsum(v * w for v, w in zip(values, weights)) / total_weight


def moving_average(data, window):
    if window <= 0 or window > len(data):
        raise ValueError("invalid window size")
    result = []
    for i in range(len(data) - window + 1):
        result.append(average(data[i:i + window]))
    return result


def cumulative_sum(data):
    result = []
    total = 0.0
    for x in data:
        total += x
        result.append(total)
    return result


def cumulative_product(data):
    result = []
    total = 1.0
    for x in data:
        total *= x
        result.append(total)
    return result


def normalize_data(data):
    mn, mx = min(data), max(data)
    if mx == mn:
        raise ValueError("cannot normalize constant data")
    return [(x - mn) / (mx - mn) for x in data]


def standardize_data(data):
    m = average(data)
    s = pstdev(data)
    if s == 0:
        raise ValueError("cannot standardize constant data")
    return [(x - m) / s for x in data]


def softmax(values):
    mx = max(values)
    exps = [exp(v - mx) for v in values]
    total = fsum(exps)
    return [v / total for v in exps]


def sigmoid(x):
    return 1 / (1 + exp(-x))


def relu(x):
    return x if x > 0 else 0.0


def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x


def gaussian(x, mu=0.0, sigma=1.0):
    return normal_pdf(x, mu, sigma)


class LCG:
    def __init__(self, seed=12345):
        self.state = seed & 0xFFFFFFFFFFFF
        self.a = 25214903917
        self.c = 11
        self.m = 1 << 48

    def next_bits(self, bits):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state >> (48 - bits)

    def next_int(self, bound=None):
        if bound is None:
            return self.next_bits(32)
        return self.next_bits(32) % bound

    def next_float(self):
        return self.next_bits(48) / (1 << 48)

    def uniform(self, lo, hi):
        return lo + (hi - lo) * self.next_float()

    def choice(self, seq):
        return seq[self.next_int(len(seq))]

    def shuffle(self, seq):
        seq = list(seq)
        for i in range(len(seq) - 1, 0, -1):
            j = self.next_int(i + 1)
            seq[i], seq[j] = seq[j], seq[i]
        return seq

    def sample(self, seq, k):
        return self.shuffle(seq)[:k]

    def gauss(self, mu=0.0, sigma=1.0):
        u1 = max(self.next_float(), 1e-12)
        u2 = self.next_float()
        z0 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
        return mu + z0 * sigma

    def exponential(self, lam=1.0):
        u = max(self.next_float(), 1e-12)
        return -log(u) / lam

    def poisson(self, lam):
        l_exp = exp(-lam)
        k = 0
        p = 1.0
        while True:
            k += 1
            p *= self.next_float()
            if p <= l_exp:
                return k - 1


class XorShift32:
    def __init__(self, seed=2463534242):
        self.state = seed & 0xFFFFFFFF

    def next(self):
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17)
        x ^= (x << 5) & 0xFFFFFFFF
        self.state = x & 0xFFFFFFFF
        return self.state

    def next_float(self):
        return self.next() / 0xFFFFFFFF


def binomial_pmf(k, n, p):
    return comb(n, k) * pow(p, k) * pow(1 - p, n - k)


def binomial_cdf(k, n, p):
    return fsum(binomial_pmf(i, n, p) for i in range(0, k + 1))


def poisson_pmf(k, lam):
    return pow(lam, k) * exp(-lam) / factorial(k)


def poisson_cdf(k, lam):
    return fsum(poisson_pmf(i, lam) for i in range(0, k + 1))


def geometric_pmf(k, p):
    return pow(1 - p, k - 1) * p


def hypergeometric_pmf(k, N, K, n):
    return comb(K, k) * comb(N - K, n - k) / comb(N, n)


def negative_binomial_pmf(k, r, p):
    return comb(k + r - 1, k) * pow(p, r) * pow(1 - p, k)


def expected_value(values, probabilities):
    return fsum(v * p for v, p in zip(values, probabilities))


def variance_discrete(values, probabilities):
    mu = expected_value(values, probabilities)
    return fsum(p * (v - mu) ** 2 for v, p in zip(values, probabilities))


def entropy(probabilities, base=2):
    return -fsum(p * log(p, base) for p in probabilities if p > 0)


def cross_entropy(p, q, base=2):
    return -fsum(pi_ * log(qi, base) for pi_, qi in zip(p, q) if qi > 0)


def kl_divergence(p, q, base=2):
    return fsum(pi_ * log(pi_ / qi, base) for pi_, qi in zip(p, q) if pi_ > 0 and qi > 0)


def bayes_theorem(p_a, p_b_given_a, p_b):
    return (p_b_given_a * p_a) / p_b


def odds_to_probability(odds):
    return odds / (1 + odds)


def probability_to_odds(p):
    if p >= 1:
        raise ValueError("probability must be less than 1")
    return p / (1 - p)


def confidence_interval_mean(data, confidence=0.95):
    n = len(data)
    m = average(data)
    s = stdev(data)
    z_table = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
    z = z_table.get(confidence, 1.96)
    margin = z * s / sqrt(n)
    return (m - margin, m + margin)


def t_statistic(sample_mean, population_mean, sample_std, n):
    return (sample_mean - population_mean) / (sample_std / sqrt(n))


def chi_square_statistic(observed, expected):
    return fsum((o - e) ** 2 / e for o, e in zip(observed, expected))


def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity * velocity


def potential_energy(mass, height, g=9.80665):
    return mass * g * height


def gravitational_force(m1, m2, r, G=6.6743e-11):
    return G * m1 * m2 / (r * r)


def gravitational_potential_energy(m1, m2, r, G=6.6743e-11):
    return -G * m1 * m2 / r


def escape_velocity(mass, radius, G=6.6743e-11):
    return sqrt(2 * G * mass / radius)


def orbital_velocity(mass, radius, G=6.6743e-11):
    return sqrt(G * mass / radius)


def orbital_period(mass, radius, G=6.6743e-11):
    return 2 * pi * sqrt(radius ** 3 / (G * mass))


def momentum(mass, velocity):
    return mass * velocity


def force(mass, acceleration):
    return mass * acceleration


def work(force_, distance, angle=0.0):
    return force_ * distance * cos(angle)


def power_physics(work_, time):
    return work_ / time


def velocity_from_distance_time(distance, time):
    return distance / time


def acceleration_from_velocity_time(dv, dt):
    return dv / dt


def final_velocity(initial_velocity, acceleration, time):
    return initial_velocity + acceleration * time


def displacement(initial_velocity, acceleration, time):
    return initial_velocity * time + 0.5 * acceleration * time * time


def projectile_range(velocity, angle, g=9.80665):
    return (velocity * velocity * sin(2 * angle)) / g


def projectile_max_height(velocity, angle, g=9.80665):
    return (velocity * velocity * sin(angle) ** 2) / (2 * g)


def projectile_time_of_flight(velocity, angle, g=9.80665):
    return (2 * velocity * sin(angle)) / g


def ohms_law_voltage(current, resistance):
    return current * resistance


def ohms_law_current(voltage, resistance):
    return voltage / resistance


def ohms_law_resistance(voltage, current):
    return voltage / current


def electrical_power(voltage, current):
    return voltage * current


def series_resistance(*resistors):
    return fsum(resistors)


def parallel_resistance(*resistors):
    return 1 / fsum(1 / r for r in resistors)


def capacitor_energy(capacitance, voltage):
    return 0.5 * capacitance * voltage * voltage


def wave_speed(frequency, wavelength):
    return frequency * wavelength


def wave_frequency(speed, wavelength):
    return speed / wavelength


def doppler_shift(source_freq, observer_velocity, source_velocity, sound_speed=343.0):
    return source_freq * (sound_speed + observer_velocity) / (sound_speed - source_velocity)


def snells_law(n1, theta1, n2):
    sin_theta2 = (n1 * sin(theta1)) / n2
    if fabs(sin_theta2) > 1:
        raise ValueError("total internal reflection")
    return asin(sin_theta2)


def lens_equation_focal(do, di):
    return 1 / (1 / do + 1 / di)


def magnification(di, do):
    return -di / do


def ideal_gas_pressure(n, T, V, R=8.314462618):
    return n * R * T / V


def ideal_gas_volume(n, T, P, R=8.314462618):
    return n * R * T / P


def relativistic_mass(rest_mass, velocity, c=299792458.0):
    beta_ = velocity / c
    if fabs(beta_) >= 1:
        raise ValueError("velocity must be less than speed of light")
    return rest_mass / sqrt(1 - beta_ * beta_)


def time_dilation(proper_time, velocity, c=299792458.0):
    beta_ = velocity / c
    if fabs(beta_) >= 1:
        raise ValueError("velocity must be less than speed of light")
    return proper_time / sqrt(1 - beta_ * beta_)


def length_contraction(proper_length, velocity, c=299792458.0):
    beta_ = velocity / c
    if fabs(beta_) >= 1:
        raise ValueError("velocity must be less than speed of light")
    return proper_length * sqrt(1 - beta_ * beta_)


def mass_energy_equivalence(mass, c=299792458.0):
    return mass * c * c


def half_life_remaining(initial, half_life, time):
    return initial * pow(0.5, time / half_life)


def decay_constant(half_life):
    return ln2 / half_life


def radioactive_decay(initial, decay_const, time):
    return initial * exp(-decay_const * time)


def compound_interest(principal, rate, times_per_year, years):
    return principal * pow(1 + rate / times_per_year, times_per_year * years)


def continuous_compound_interest(principal, rate, years):
    return principal * exp(rate * years)


def simple_interest(principal, rate, years):
    return principal * (1 + rate * years)


def present_value(future_value, rate, periods):
    return future_value / pow(1 + rate, periods)


def future_value(present_value_, rate, periods):
    return present_value_ * pow(1 + rate, periods)


def annuity_present_value(payment, rate, periods):
    if rate == 0:
        return payment * periods
    return payment * (1 - pow(1 + rate, -periods)) / rate


def annuity_future_value(payment, rate, periods):
    if rate == 0:
        return payment * periods
    return payment * (pow(1 + rate, periods) - 1) / rate


def loan_payment(principal, rate, periods):
    if rate == 0:
        return principal / periods
    return principal * rate / (1 - pow(1 + rate, -periods))


def net_present_value(rate, cashflows):
    return fsum(cf / pow(1 + rate, t) for t, cf in enumerate(cashflows))


def internal_rate_of_return(cashflows, guess=0.1, tol=1e-9, max_iter=1000):
    rate = guess
    for _ in range(max_iter):
        npv = net_present_value(rate, cashflows)
        d_npv = fsum(-t * cf / pow(1 + rate, t + 1) for t, cf in enumerate(cashflows))
        if d_npv == 0:
            break
        new_rate = rate - npv / d_npv
        if fabs(new_rate - rate) < tol:
            return new_rate
        rate = new_rate
    return rate


def amortization_schedule(principal, rate, periods):
    payment = loan_payment(principal, rate, periods)
    balance = principal
    schedule = []
    for period in range(1, periods + 1):
        interest_payment = balance * rate
        principal_payment = payment - interest_payment
        balance -= principal_payment
        schedule.append({
            "period": period,
            "payment": payment,
            "interest": interest_payment,
            "principal": principal_payment,
            "balance": max(balance, 0.0),
        })
    return schedule


def effective_annual_rate(nominal_rate, periods_per_year):
    return pow(1 + nominal_rate / periods_per_year, periods_per_year) - 1


def real_interest_rate(nominal_rate, inflation_rate):
    return (1 + nominal_rate) / (1 + inflation_rate) - 1


def rule_of_72(rate_percent):
    return 72 / rate_percent


def break_even_point(fixed_costs, price_per_unit, variable_cost_per_unit):
    return fixed_costs / (price_per_unit - variable_cost_per_unit)


def markup_price(cost, markup_percent):
    return cost * (1 + markup_percent / 100)


def discount_price(price, discount_percent):
    return price * (1 - discount_percent / 100)


def percentage_change(old_value, new_value):
    if old_value == 0:
        raise ValueError("old_value cannot be zero")
    return (new_value - old_value) / old_value * 100


def compound_annual_growth_rate(beginning_value, ending_value, years):
    return pow(ending_value / beginning_value, 1 / years) - 1


def sharpe_ratio(returns, risk_free_rate):
    excess_returns = [r - risk_free_rate for r in returns]
    return average(excess_returns) / pstdev(excess_returns)


def black_scholes_call(S, K, T, r, sigma):
    d1 = (log(S / K) + (r + sigma * sigma / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    return S * normal_cdf(d1) - K * exp(-r * T) * normal_cdf(d2)


def black_scholes_put(S, K, T, r, sigma):
    d1 = (log(S / K) + (r + sigma * sigma / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    return K * exp(-r * T) * normal_cdf(-d2) - S * normal_cdf(-d1)


def gradient_descent(f, grad_f, x0, learning_rate=0.01, max_iter=10000, tol=1e-10):
    x = list(x0)
    for _ in range(max_iter):
        g = grad_f(x)
        new_x = [xi - learning_rate * gi for xi, gi in zip(x, g)]
        if fsum((a - b) ** 2 for a, b in zip(new_x, x)) < tol * tol:
            return new_x
        x = new_x
    return x


def golden_section_search(f, a, b, tol=1e-10, max_iter=500):
    gr = (sqrt(5) - 1) / 2
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    for _ in range(max_iter):
        if fabs(c - d) < tol:
            break
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - gr * (b - a)
        d = a + gr * (b - a)
    return (a + b) / 2


def simulated_annealing_1d(f, x0, bounds, rng=None, iterations=1000, initial_temp=10.0, cooling=0.995):
    if rng is None:
        rng = LCG(1)
    lo, hi = bounds
    x = x0
    best = x
    best_val = f(x)
    temp = initial_temp
    for _ in range(iterations):
        candidate = clamp(x + rng.uniform(-1, 1) * (hi - lo) * 0.1, lo, hi)
        delta = f(candidate) - f(x)
        if delta < 0 or rng.next_float() < exp(-delta / max(temp, 1e-12)):
            x = candidate
            if f(x) < best_val:
                best, best_val = x, f(x)
        temp *= cooling
    return best


def newton_method_multivariate(f, grad_f, hessian_f, x0, tol=1e-10, max_iter=100):
    x = list(x0)
    for _ in range(max_iter):
        g = grad_f(x)
        H = hessian_f(x)
        delta = solve_linear_system(H, [-gi for gi in g])
        x = [xi + di for xi, di in zip(x, delta)]
        if fsum(d * d for d in delta) < tol * tol:
            break
    return x


def linear_programming_simplex_2var(c, constraints):
    best_value = -inf
    best_point = None
    vertices = []
    n = len(constraints)
    for i in range(n):
        for j in range(i + 1, n):
            a1, b1, c1 = constraints[i]
            a2, b2, c2 = constraints[j]
            det = a1 * b2 - a2 * b1
            if fabs(det) < 1e-12:
                continue
            x = (c1 * b2 - c2 * b1) / det
            y = (a1 * c2 - a2 * c1) / det
            vertices.append((x, y))
    for x, y in vertices:
        if all(a * x + b * y <= cc + 1e-9 for a, b, cc in constraints) and x >= -1e-9 and y >= -1e-9:
            value = c[0] * x + c[1] * y
            if value > best_value:
                best_value = value
                best_point = (x, y)
    return best_point, best_value


def power_iteration(A, iterations=1000, tol=1e-12):
    n = len(A)
    v = [1.0] * n
    eigenvalue = 0.0
    for _ in range(iterations):
        Av = matrix_vec_mul(A, v)
        norm = vec_norm(Av)
        if norm == 0:
            break
        new_v = tuple(x / norm for x in Av)
        new_eigenvalue = vec_dot(new_v, matrix_vec_mul(A, new_v))
        if fabs(new_eigenvalue - eigenvalue) < tol:
            v = new_v
            eigenvalue = new_eigenvalue
            break
        v = new_v
        eigenvalue = new_eigenvalue
    return eigenvalue, v


def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = list(v)
        for b in basis:
            proj = vec_dot(v, b) / vec_dot(b, b)
            w = [wi - proj * bi for wi, bi in zip(w, b)]
        norm = sqrt(fsum(wi * wi for wi in w))
        if norm > 1e-12:
            basis.append(tuple(wi / norm for wi in w))
    return basis


def qr_decomposition(A):
    n = len(A)
    columns = matrix_transpose(A)
    Q_cols = gram_schmidt(columns)
    Q = matrix_transpose(Q_cols)
    R = [[vec_dot(Q_cols[i], columns[j]) if i <= j else 0.0 for j in range(n)] for i in range(len(Q_cols))]
    return Q, R


def vector_norm_p(v, p=2):
    if p == inf:
        return max(fabs(x) for x in v)
    return pow(fsum(fabs(x) ** p for x in v), 1 / p)


def matrix_norm_frobenius(A):
    return sqrt(fsum(A[i][j] ** 2 for i in range(len(A)) for j in range(len(A[0]))))


def condition_number(A):
    inv = matrix_inverse(A)
    return matrix_norm_frobenius(A) * matrix_norm_frobenius(inv)


def cholesky_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = fsum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = A[i][i] - s
                if val <= 0:
                    raise ValueError("matrix is not positive definite")
                L[i][j] = sqrt(val)
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    return L


def lu_decomposition(A):
    n = len(A)
    L = matrix_identity(n)
    U = [row[:] for row in A]
    for i in range(n):
        for j in range(i + 1, n):
            if U[i][i] == 0:
                raise ValueError("zero pivot encountered")
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            U[j] = [U[j][k] - factor * U[i][k] for k in range(n)]
    return L, U


def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]
    visited = {start}
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


def dfs_path(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path = path + [start]
    if start == end:
        return path
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, end, visited, path)
            if result:
                return result
    return None


def dijkstra(graph, start):
    distances = {node: inf for node in graph}
    distances[start] = 0
    unvisited = set(graph.keys())
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        if distances[current] == inf:
            break
        unvisited.remove(current)
        for neighbor, weight in graph.get(current, {}).items():
            new_dist = distances[current] + weight
            if new_dist < distances.get(neighbor, inf):
                distances[neighbor] = new_dist
    return distances


def bellman_ford(graph, start, nodes):
    distances = {node: inf for node in nodes}
    distances[start] = 0
    for _ in range(len(nodes) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
    return distances


def floyd_warshall(graph_matrix):
    n = len(graph_matrix)
    dist_matrix = [row[:] for row in graph_matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist_matrix[i][k] + dist_matrix[k][j] < dist_matrix[i][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
    return dist_matrix


def topological_sort(graph):
    visited = set()
    stack = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)
        stack.append(node)

    for node in graph:
        visit(node)
    return stack[::-1]


def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def visit(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if visit(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.discard(node)
        return False

    for node in graph:
        if node not in visited:
            if visit(node):
                return True
    return False


def connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            stack = [node]
            component = []
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    stack.extend(graph.get(current, []))
            components.append(component)
    return components


def bubble_sort(data):
    arr = list(data)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(data):
    arr = list(data)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(data):
    arr = list(data)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def merge_sort(data):
    arr = list(data)
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(data):
    arr = list(data)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(data):
    arr = list(data)
    n = len(arr)

    def heapify(size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr


def binary_search(data, target):
    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def linear_search(data, target):
    for i, x in enumerate(data):
        if x == target:
            return i
    return -1


def levenshtein_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[m][n]


def hamming_distance(a, b):
    if len(a) != len(b):
        raise ValueError("sequences must be the same length")
    return sum(1 for x, y in zip(a, b) if x != y)


def jaccard_similarity(set_a, set_b):
    set_a, set_b = set(set_a), set(set_b)
    union = set_a | set_b
    if not union:
        return 1.0
    return len(set_a & set_b) / len(union)


def cosine_similarity(u, v):
    return vec_dot(u, v) / (vec_norm(u) * vec_norm(v))


def power_set(s):
    s = list(s)
    result = [[]]
    for elem in s:
        result += [subset + [elem] for subset in result]
    return result


def permutations_list(s):
    s = list(s)
    if len(s) <= 1:
        return [s]
    result = []
    for i in range(len(s)):
        rest = s[:i] + s[i + 1:]
        for p in permutations_list(rest):
            result.append([s[i]] + p)
    return result


def combinations_list(s, k):
    s = list(s)
    if k == 0:
        return [[]]
    if not s:
        return []
    first, rest = s[0], s[1:]
    with_first = [[first] + c for c in combinations_list(rest, k - 1)]
    without_first = combinations_list(rest, k)
    return with_first + without_first


def cartesian_product(*sequences):
    result = [[]]
    for seq in sequences:
        result = [combo + [item] for combo in result for item in seq]
    return result


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        raise ValueError("month must be between 1 and 12")
    return days[month - 1]


def day_of_week_zeller(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return names[h]


def julian_day_number(day, month, year):
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045


def days_between(d1, m1, y1, d2, m2, y2):
    return julian_day_number(d2, m2, y2) - julian_day_number(d1, m1, y1)


def age_in_years(birth_day, birth_month, birth_year, current_day, current_month, current_year):
    age = current_year - birth_year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1
    return age


def is_palindrome_string(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def is_anagram(a, b):
    return sorted(a.lower().replace(" ", "")) == sorted(b.lower().replace(" ", ""))


def gcd_of_list(nums):
    return gcd(*nums)


def lcm_of_list(nums):
    return lcm(*nums)


def mod_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


def modular_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("modular inverse does not exist")
    return x % m


def chinese_remainder_theorem(remainders, moduli):
    total = 0
    product = prod(moduli)
    for r, m in zip(remainders, moduli):
        p = product // m
        total += r * modular_inverse(p, m) * p
    return total % product


def miller_rabin(n, k=20, rng=None):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    if rng is None:
        rng = LCG(7)
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = 2 + rng.next_int(n - 4)
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True


def discrete_log_baby_step_giant_step(g, h, p):
    m = ceil(sqrt(p - 1))
    table = {}
    e_ = 1
    for j in range(m):
        table[e_] = j
        e_ = (e_ * g) % p
    factor = mod_pow(g, m * (p - 2), p)
    gamma_ = h
    for i in range(m):
        if gamma_ in table:
            return i * m + table[gamma_]
        gamma_ = (gamma_ * factor) % p
    return None


def caesar_cipher_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def xor_checksum(data):
    result = 0
    for b in data:
        result ^= b
    return result


def dft(signal):
    n = len(signal)
    result = []
    for k in range(n):
        re = fsum(signal[t] * cos(2 * pi * k * t / n) for t in range(n))
        im = -fsum(signal[t] * sin(2 * pi * k * t / n) for t in range(n))
        result.append((re, im))
    return result


def idft(spectrum):
    n = len(spectrum)
    result = []
    for t in range(n):
        re = fsum(spectrum[k][0] * cos(2 * pi * k * t / n) - spectrum[k][1] * sin(2 * pi * k * t / n) for k in range(n)) / n
        result.append(re)
    return result


def magnitude_spectrum(spectrum):
    return [complex_abs(c) for c in spectrum]


def exponential_smoothing(data, alpha):
    if not data:
        return []
    result = [data[0]]
    for x in data[1:]:
        result.append(alpha * x + (1 - alpha) * result[-1])
    return result


def double_exponential_smoothing(data, alpha, beta_):
    if len(data) < 2:
        return data[:]
    level = data[0]
    trend = data[1] - data[0]
    result = [level]
    for x in data[1:]:
        last_level = level
        level = alpha * x + (1 - alpha) * (level + trend)
        trend = beta_ * (level - last_level) + (1 - beta_) * trend
        result.append(level)
    return result


def autocorrelation(data, lag):
    n = len(data)
    m = average(data)
    num = fsum((data[t] - m) * (data[t + lag] - m) for t in range(n - lag))
    den = fsum((x - m) ** 2 for x in data)
    return num / den if den != 0 else 0.0


def least_squares_polynomial_fit(x, y, degree):
    n = degree + 1
    A = [[fsum(xi ** (i + j) for xi in x) for j in range(n)] for i in range(n)]
    b = [fsum(yi * xi ** i for xi, yi in zip(x, y)) for i in range(n)]
    return solve_linear_system(A, b)


def r_squared(y_actual, y_predicted):
    m = average(y_actual)
    ss_res = fsum((a - p) ** 2 for a, p in zip(y_actual, y_predicted))
    ss_tot = fsum((a - m) ** 2 for a in y_actual)
    return 1 - ss_res / ss_tot if ss_tot != 0 else 0.0


def durand_kerner(coeffs, iterations=200, tol=1e-12):
    n = len(coeffs) - 1
    leading = coeffs[-1]
    norm_coeffs = [c / leading for c in coeffs]
    roots = [complex_pow((0.4, 0.9), k) for k in range(n)]

    def evaluate(poly, z):
        result = (0.0, 0.0)
        power = (1.0, 0.0)
        for c in poly:
            result = complex_add(result, complex_mul((c, 0.0), power))
            power = complex_mul(power, z)
        return result

    for _ in range(iterations):
        max_change = 0.0
        new_roots = []
        for i in range(n):
            numerator = evaluate(norm_coeffs, roots[i])
            denom = (1.0, 0.0)
            for j in range(n):
                if i != j:
                    denom = complex_mul(denom, complex_sub(roots[i], roots[j]))
            delta = complex_div(numerator, denom)
            new_root = complex_sub(roots[i], delta)
            max_change = max(max_change, complex_abs(delta))
            new_roots.append(new_root)
        roots = new_roots
        if max_change < tol:
            break
    return roots


def horner_eval(coeffs, x):
    return polynomial_eval(coeffs, x)


def synthetic_division(coeffs, root):
    n = len(coeffs)
    result = [0.0] * (n - 1)
    result[0] = coeffs[-1]
    for i in range(1, n - 1):
        result[i] = coeffs[-1 - i] + result[i - 1] * root
    remainder_ = coeffs[0] + result[-1] * root
    return result[::-1], remainder_


def chebyshev_polynomial(n, x):
    if n == 0:
        return 1.0
    if n == 1:
        return x
    t0, t1 = 1.0, x
    for _ in range(2, n + 1):
        t0, t1 = t1, 2 * x * t1 - t0
    return t1


def legendre_polynomial(n, x):
    if n == 0:
        return 1.0
    if n == 1:
        return x
    p0, p1 = 1.0, x
    for k in range(2, n + 1):
        p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
    return p1


def hermite_polynomial(n, x):
    if n == 0:
        return 1.0
    if n == 1:
        return 2 * x
    h0, h1 = 1.0, 2 * x
    for k in range(2, n + 1):
        h0, h1 = h1, 2 * x * h1 - 2 * (k - 1) * h0
    return h1


def laguerre_polynomial(n, x):
    if n == 0:
        return 1.0
    if n == 1:
        return 1 - x
    l0, l1 = 1.0, 1 - x
    for k in range(2, n + 1):
        l0, l1 = l1, ((2 * k - 1 - x) * l1 - (k - 1) * l0) / k
    return l1


def point3d_add(p, q):
    return (p[0] + q[0], p[1] + q[1], p[2] + q[2])


def point3d_sub(p, q):
    return (p[0] - q[0], p[1] - q[1], p[2] - q[2])


def plane_from_points(p1, p2, p3):
    v1 = point3d_sub(p2, p1)
    v2 = point3d_sub(p3, p1)
    normal = vec_cross(v1, v2)
    d = -vec_dot(normal, p1)
    return normal + (d,)


def distance_point_to_plane(point, plane):
    a, b, c, d = plane
    return fabs(a * point[0] + b * point[1] + c * point[2] + d) / sqrt(a * a + b * b + c * c)


def line_plane_intersection(line_point, line_dir, plane):
    a, b, c, d = plane
    denom = a * line_dir[0] + b * line_dir[1] + c * line_dir[2]
    if fabs(denom) < 1e-14:
        return None
    t = -(a * line_point[0] + b * line_point[1] + c * line_point[2] + d) / denom
    return tuple(line_point[i] + t * line_dir[i] for i in range(3))


def tetrahedron_volume(p1, p2, p3, p4):
    v1 = point3d_sub(p2, p1)
    v2 = point3d_sub(p3, p1)
    v3 = point3d_sub(p4, p1)
    return fabs(vec_dot(v1, vec_cross(v2, v3))) / 6


def centroid(points):
    n = len(points)
    dims = len(points[0])
    return tuple(fsum(p[i] for p in points) / n for i in range(dims))


def bounding_box(points):
    dims = len(points[0])
    mins = tuple(min(p[i] for p in points) for i in range(dims))
    maxs = tuple(max(p[i] for p in points) for i in range(dims))
    return mins, maxs


def convex_hull_2d(points):
    points = sorted(set(points))
    if len(points) <= 2:
        return points

    def cross_z(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross_z(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_z(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-300) + xi):
            inside = not inside
        j = i
    return inside


def rotate_point_2d(point, angle, origin=(0.0, 0.0)):
    x, y = point[0] - origin[0], point[1] - origin[1]
    c, s = cos(angle), sin(angle)
    return (x * c - y * s + origin[0], x * s + y * c + origin[1])


def reflect_point_2d(point, line_p1, line_p2):
    x1, y1 = line_p1
    x2, y2 = line_p2
    dx, dy = x2 - x1, y2 - y1
    a = (dx * dx - dy * dy) / (dx * dx + dy * dy)
    b = 2 * dx * dy / (dx * dx + dy * dy)
    x0, y0 = point[0] - x1, point[1] - y1
    nx = a * x0 + b * y0
    ny = b * x0 - a * y0
    return (nx + x1, ny + y1)


def scale_point_2d(point, factor, origin=(0.0, 0.0)):
    return (origin[0] + (point[0] - origin[0]) * factor, origin[1] + (point[1] - origin[1]) * factor)


def rotation_matrix_2d(angle):
    c, s = cos(angle), sin(angle)
    return [[c, -s], [s, c]]


def rotation_matrix_3d_x(angle):
    c, s = cos(angle), sin(angle)
    return [[1, 0, 0], [0, c, -s], [0, s, c]]


def rotation_matrix_3d_y(angle):
    c, s = cos(angle), sin(angle)
    return [[c, 0, s], [0, 1, 0], [-s, 0, c]]


def rotation_matrix_3d_z(angle):
    c, s = cos(angle), sin(angle)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


def quaternion_mul(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return (
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
    )


def quaternion_conjugate(q):
    w, x, y, z = q
    return (w, -x, -y, -z)


def quaternion_norm(q):
    return sqrt(fsum(c * c for c in q))


def quaternion_normalize(q):
    n = quaternion_norm(q)
    return tuple(c / n for c in q)


def quaternion_from_axis_angle(axis, angle):
    half = angle / 2
    s = sin(half)
    ax, ay, az = vec_normalize(axis)
    return (cos(half), ax * s, ay * s, az * s)


def format_scientific(x, precision=4):
    if x == 0:
        return "0.%se+00" % ("0" * precision)
    neg = x < 0
    x = fabs(x)
    exponent = floor(log10(x))
    mantissa = x / pow(10, exponent)
    if mantissa >= 10:
        mantissa /= 10
        exponent += 1
    sign_str = "-" if neg else ""
    exp_sign = "+" if exponent >= 0 else "-"
    return "%s%.*fe%s%02d" % (sign_str, precision, mantissa, exp_sign, abs(int(exponent)))


def round_to_significant_figures(x, sig):
    if x == 0:
        return 0.0
    d = ceil(log10(fabs(x)))
    power = sig - int(d)
    factor = pow(10, power)
    return round(x * factor) / factor


def round_half_up(x, decimals=0):
    factor = pow(10, decimals)
    return floor(x * factor + 0.5) / factor if x >= 0 else -floor(-x * factor + 0.5) / factor


def round_to_nearest(x, multiple):
    return round(x / multiple) * multiple


def truncate_decimal(x, decimals):
    factor = pow(10, decimals)
    return trunc(x * factor) / factor


def format_currency(x, symbol="$", decimals=2):
    sign_str = "-" if x < 0 else ""
    x = fabs(x)
    s = "%.*f" % (decimals, x)
    integer_part, _, decimal_part = s.partition(".")
    groups = []
    while len(integer_part) > 3:
        groups.insert(0, integer_part[-3:])
        integer_part = integer_part[:-3]
    groups.insert(0, integer_part)
    formatted_int = ",".join(groups)
    return "%s%s%s.%s" % (sign_str, symbol, formatted_int, decimal_part)


def format_percentage(x, decimals=2):
    return "%.*f%%" % (decimals, x * 100)


def number_to_words_small(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n < 10:
        return ones[n]
    if n < 20:
        return teens[n - 10]
    if n < 100:
        return tens[n // 10] + (("-" + ones[n % 10]) if n % 10 else "")
    if n < 1000:
        return ones[n // 100] + " hundred" + ((" " + number_to_words_small(n % 100)) if n % 100 else "")
    return str(n)


def roman_to_int(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        val = values[ch]
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total


def int_to_roman(n):
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = ""
    for value, symbol in values:
        while n >= value:
            result += symbol
            n -= value
    return result


def is_armstrong_number(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


def is_automorphic(n):
    sq = n * n
    return str(sq).endswith(str(n))


def kaprekar_routine(n, digits=4):
    steps = []
    seen = set()
    while n not in seen and n != 6174:
        seen.add(n)
        s = str(n).zfill(digits)
        asc = int("".join(sorted(s)))
        desc = int("".join(sorted(s, reverse=True)))
        n = desc - asc
        steps.append(n)
    return steps


def collatz_length(n):
    return len(collatz_sequence(n))


def amicable_pair(a, b):
    return divisor_sum(a) - a == b and divisor_sum(b) - b == a


def narcissistic_numbers(limit):
    return [n for n in range(1, limit + 1) if is_armstrong_number(n)]


def perfect_numbers(limit):
    return [n for n in range(2, limit + 1) if is_perfect(n)]


def twin_primes(limit):
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)
    return [(p, p + 2) for p in primes if p + 2 in prime_set]


def goldbach_pair(n):
    if n <= 2 or n % 2 != 0:
        raise ValueError("n must be an even number greater than 2")
    for p in range(2, n):
        if is_prime(p) and is_prime(n - p):
            return (p, n - p)
    return None


def chi_square_pdf(x, k):
    if x < 0:
        return 0.0
    return pow(x, k / 2 - 1) * exp(-x / 2) / (pow(2, k / 2) * gamma(k / 2))


def t_distribution_pdf(x, nu):
    coeff = gamma((nu + 1) / 2) / (sqrt(nu * pi) * gamma(nu / 2))
    return coeff * pow(1 + x * x / nu, -(nu + 1) / 2)


def f_distribution_pdf(x, d1, d2):
    if x <= 0:
        return 0.0
    num = sqrt((pow(d1 * x, d1) * pow(d2, d2)) / pow(d1 * x + d2, d1 + d2))
    return num / (x * beta(d1 / 2, d2 / 2))


def exponential_pdf(x, lam):
    if x < 0:
        return 0.0
    return lam * exp(-lam * x)


def exponential_cdf(x, lam):
    if x < 0:
        return 0.0
    return 1 - exp(-lam * x)


def uniform_pdf(x, a, b):
    if a <= x <= b:
        return 1 / (b - a)
    return 0.0


def uniform_cdf(x, a, b):
    if x < a:
        return 0.0
    if x > b:
        return 1.0
    return (x - a) / (b - a)


def gamma_pdf(x, shape, scale):
    if x <= 0:
        return 0.0
    return pow(x, shape - 1) * exp(-x / scale) / (gamma(shape) * pow(scale, shape))


def beta_pdf(x, a, b):
    if x < 0 or x > 1:
        return 0.0
    return pow(x, a - 1) * pow(1 - x, b - 1) / beta(a, b)


def weibull_pdf(x, k, lam):
    if x < 0:
        return 0.0
    return (k / lam) * pow(x / lam, k - 1) * exp(-pow(x / lam, k))


def weibull_cdf(x, k, lam):
    if x < 0:
        return 0.0
    return 1 - exp(-pow(x / lam, k))


def laplace_pdf(x, mu, b):
    return exp(-fabs(x - mu) / b) / (2 * b)


def cauchy_pdf(x, x0, gamma_):
    return 1 / (pi * gamma_ * (1 + ((x - x0) / gamma_) ** 2))


def logistic_pdf(x, mu, s):
    z = exp(-(x - mu) / s)
    return z / (s * (1 + z) ** 2)


def manhattan_distance(p, q):
    return fsum(fabs(a - b) for a, b in zip(p, q))


def chebyshev_distance(p, q):
    return max(fabs(a - b) for a, b in zip(p, q))


def minkowski_distance(p, q, order):
    return pow(fsum(fabs(a - b) ** order for a, b in zip(p, q)), 1 / order)


def canberra_distance(p, q):
    return fsum(fabs(a - b) / (fabs(a) + fabs(b)) for a, b in zip(p, q) if (fabs(a) + fabs(b)) != 0)


def bray_curtis_distance(p, q):
    num = fsum(fabs(a - b) for a, b in zip(p, q))
    den = fsum(fabs(a + b) for a, b in zip(p, q))
    return num / den if den != 0 else 0.0


def cubic_spline_coefficients(x, y):
    n = len(x) - 1
    h = [x[i + 1] - x[i] for i in range(n)]
    alpha = [0.0] * (n + 1)
    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1]) * (y[i] - y[i - 1])
    l = [1.0] * (n + 1)
    mu = [0.0] * (n + 1)
    z = [0.0] * (n + 1)
    for i in range(1, n):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
    c = [0.0] * (n + 1)
    b = [0.0] * n
    d = [0.0] * n
    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])
    return list(zip(y[:-1], b, c[:-1], d))


def cubic_spline_eval(x_data, coeffs, x):
    n = len(coeffs)
    i = 0
    for j in range(n):
        if x_data[j] <= x <= x_data[j + 1] if j + 1 < len(x_data) else True:
            i = j
            if x_data[j] <= x:
                i = j
    a, b, c, d = coeffs[min(i, n - 1)]
    dx = x - x_data[min(i, n - 1)]
    return a + b * dx + c * dx ** 2 + d * dx ** 3


def rpn_evaluate(tokens):
    stack = []
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "^": lambda a, b: pow(a, b),
    }
    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(float(token))
    return stack[0]


def matrix_power(A, n):
    size = len(A)
    result = matrix_identity(size)
    base = [row[:] for row in A]
    while n > 0:
        if n & 1:
            result = matrix_mul(result, base)
        base = matrix_mul(base, base)
        n >>= 1
    return result


def fibonacci_matrix_power(n):
    if n == 0:
        return 0
    M = [[1, 1], [1, 0]]
    result = matrix_power(M, n)
    return int(round(result[0][1]))


def pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        triangle.append(binomial_coefficient_row(i))
    return triangle


def magic_square_odd(n):
    if n % 2 == 0:
        raise ValueError("this method only works for odd n")
    square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        square[i][j] = num
        ni, nj = (i - 1) % n, (j + 1) % n
        if square[ni][nj]:
            ni, nj = (i + 1) % n, j
        i, j = ni, nj
    return square


def ease_in_quart(t):
    return t ** 4


def ease_out_quart(t):
    return 1 - pow(1 - t, 4)


def ease_in_out_quart(t):
    return 8 * t ** 4 if t < 0.5 else 1 - pow(-2 * t + 2, 4) / 2


def ease_in_quint(t):
    return t ** 5


def ease_out_quint(t):
    return 1 - pow(1 - t, 5)


def ease_in_out_quint(t):
    return 16 * t ** 5 if t < 0.5 else 1 - pow(-2 * t + 2, 5) / 2


def ease_in_expo(t):
    return 0.0 if t == 0 else pow(2, 10 * t - 10)


def ease_out_expo(t):
    return 1.0 if t == 1 else 1 - pow(2, -10 * t)


def ease_in_circ(t):
    return 1 - sqrt(1 - pow(t, 2))


def ease_out_circ(t):
    return sqrt(1 - pow(t - 1, 2))


def ease_in_back(t, s=1.70158):
    return (s + 1) * t ** 3 - s * t * t


def ease_out_back(t, s=1.70158):
    t -= 1
    return 1 + (s + 1) * t ** 3 + s * t * t


def ease_in_elastic(t, amplitude=1.0, period=0.3):
    if t == 0 or t == 1:
        return t
    s = period / 4
    t -= 1
    return -(amplitude * pow(2, 10 * t) * sin((t - s) * (2 * pi) / period))


def ease_out_elastic(t, amplitude=1.0, period=0.3):
    if t == 0 or t == 1:
        return t
    s = period / 4
    return amplitude * pow(2, -10 * t) * sin((t - s) * (2 * pi) / period) + 1


def ease_out_bounce(t):
    n1, d1 = 7.5625, 2.75
    if t < 1 / d1:
        return n1 * t * t
    if t < 2 / d1:
        t -= 1.5 / d1
        return n1 * t * t + 0.75
    if t < 2.5 / d1:
        t -= 2.25 / d1
        return n1 * t * t + 0.9375
    t -= 2.625 / d1
    return n1 * t * t + 0.984375


def ease_in_bounce(t):
    return 1 - ease_out_bounce(1 - t)


def catmull_rom_spline(p0, p1, p2, p3, t):
    t2 = t * t
    t3 = t2 * t
    return tuple(
        0.5 * (
            2 * p1[i] + (-p0[i] + p2[i]) * t
            + (2 * p0[i] - 5 * p1[i] + 4 * p2[i] - p3[i]) * t2
            + (-p0[i] + 3 * p1[i] - 3 * p2[i] + p3[i]) * t3
        )
        for i in range(len(p0))
    )


def bezier_quadratic(p0, p1, p2, t):
    u = 1 - t
    return tuple(u * u * p0[i] + 2 * u * t * p1[i] + t * t * p2[i] for i in range(len(p0)))


def bezier_cubic(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(
        u ** 3 * p0[i] + 3 * u * u * t * p1[i] + 3 * u * t * t * p2[i] + t ** 3 * p3[i]
        for i in range(len(p0))
    )


def bezier_general(points, t):
    points = [list(p) for p in points]
    while len(points) > 1:
        points = [
            tuple(lerp(points[i][d], points[i + 1][d], t) for d in range(len(points[i])))
            for i in range(len(points) - 1)
        ]
    return points[0]


def perlin_noise_1d(x, rng=None):
    if rng is None:
        rng = LCG(42)
    x0 = floor(x)
    x1 = x0 + 1
    t = x - x0

    def grad(ix):
        state = LCG(ix * 2654435761 & 0xFFFFFFFF)
        return state.uniform(-1, 1)

    n0 = grad(x0) * (x - x0)
    n1 = grad(x1) * (x - x1)
    fade_t = ease_in_out_quint(t)
    return lerp(n0, n1, fade_t)


def smooth_noise_2d(x, y, seed=1):
    n = int(x) + int(y) * 57 + seed * 131
    n = (n << 13) ^ n
    val = (1.0 - ((n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0)
    return val


def running_max(data):
    result = []
    current = -inf
    for x in data:
        current = max(current, x)
        result.append(current)
    return result


def running_min(data):
    result = []
    current = inf
    for x in data:
        current = min(current, x)
        result.append(current)
    return result


def diff(data):
    return [data[i + 1] - data[i] for i in range(len(data) - 1)]


def cumulative_max_index(data):
    best_idx = 0
    for i, x in enumerate(data):
        if x > data[best_idx]:
            best_idx = i
    return best_idx


def zscore_normalize_matrix(matrix):
    cols = matrix_transpose(matrix)
    normalized_cols = [standardize_data(col) for col in cols]
    return matrix_transpose(normalized_cols)


def outliers_iqr(data):
    q1, _, q3 = quartiles(data)
    iqr_val = q3 - q1
    lower = q1 - 1.5 * iqr_val
    upper = q3 + 1.5 * iqr_val
    return [x for x in data if x < lower or x > upper]


def skewness(data):
    n = len(data)
    m = average(data)
    s = pstdev(data)
    return (n / ((n - 1) * (n - 2))) * fsum(((x - m) / s) ** 3 for x in data)


def kurtosis(data):
    n = len(data)
    m = average(data)
    s = pstdev(data)
    return fsum(((x - m) / s) ** 4 for x in data) / n - 3
