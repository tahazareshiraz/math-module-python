from .constants import PI
from .core import fabs, factorial
from .power import exp, log, sqrt, pow_


_LANCZOS_G = 7
_LANCZOS_COEF = [
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


def sin_pi(x):
    from .trigonometry import sin
    return sin(PI * x)


def gamma(x):
    if x < 0.5:
        return PI / (sin_pi(x) * gamma(1 - x))
    x -= 1
    a = _LANCZOS_COEF[0]
    t = x + _LANCZOS_G + 0.5
    for i in range(1, _LANCZOS_G + 2):
        a += _LANCZOS_COEF[i] / (x + i)
    return sqrt(2 * PI) * pow_(t, x + 0.5) * exp(-t) * a


def lgamma(x):
    g = gamma(x)
    if g <= 0:
        raise ValueError("math domain error")
    return log(g)


def beta_function(a, b):
    return gamma(a) * gamma(b) / gamma(a + b)


def factorial_gamma(n):
    return gamma(n + 1)


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


def digamma(x):
    result = 0.0
    while x < 6:
        result -= 1.0 / x
        x += 1
    inv = 1.0 / x
    inv2 = inv * inv
    result += log(x) - 0.5 * inv
    result -= inv2 * (1.0 / 12 - inv2 * (1.0 / 120 - inv2 / 252))
    return result


def beta_incomplete_regularized(x, a, b, iterations=200):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    front = exp(log(x) * a + log(1 - x) * b - log(a) - lgamma(a) - lgamma(b) + lgamma(a + b))
    f, c, d = 1.0, 1.0, 0.0
    for i in range(iterations):
        m = i // 2
        if i == 0:
            numerator = 1.0
        elif i % 2 == 0:
            numerator = (m * (b - m) * x) / ((a + 2 * m - 1) * (a + 2 * m))
        else:
            numerator = -((a + m) * (a + b + m) * x) / ((a + 2 * m) * (a + 2 * m + 1))
        d = 1.0 + numerator * d
        if fabs(d) < 1e-30:
            d = 1e-30
        d = 1.0 / d
        c = 1.0 + numerator / c
        if fabs(c) < 1e-30:
            c = 1e-30
        cd = c * d
        f *= cd
        if fabs(1.0 - cd) < 1e-12:
            break
    return front * (f - 1.0)


def riemann_zeta_approx(s, terms=10000):
    if s <= 1:
        raise ValueError("approximation requires s > 1")
    total = 0.0
    for n in range(1, terms + 1):
        total += 1.0 / pow_(n, s)
    return total


def bessel_j0(x, terms=40):
    total = 0.0
    for k in range(terms):
        term = ((-1) ** k) / (factorial(k) ** 2) * pow_(x / 2, 2 * k)
        total += term
    return total


def bessel_j1(x, terms=40):
    total = 0.0
    for k in range(terms):
        term = ((-1) ** k) / (factorial(k) * factorial(k + 1)) * pow_(x / 2, 2 * k + 1)
        total += term
    return total


def lambert_w(x, iterations=100):
    if x < -1.0 / exp(1.0):
        raise ValueError("math domain error")
    if x == 0:
        return 0.0
    w = log(x + 1) if x > -1 else -0.5
    for _ in range(iterations):
        ew = exp(w)
        denom = ew * (w + 1) - (w + 2) * (w * ew - x) / (2 * w + 2)
        if denom == 0:
            break
        w_new = w - (w * ew - x) / denom
        if fabs(w_new - w) < 1e-15:
            w = w_new
            break
        w = w_new
    return w
