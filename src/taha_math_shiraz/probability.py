from .aggregates import fsum, prod, isclose, comb, perm
from .constants import TAU
from .numtheory_core import factorial, gcd, lcm, isqrt
from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .trigonometry import degrees, radians, sin, cos, tan, sinh, cosh, tanh, asinh, acosh, atanh, asin, acos, atan, atan2, hypot, dist
from .special import lgamma, gamma, erf, erfc, frexp, ldexp, nextafter, ulp, signbit


def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))



def poisson_probability(lam, k):
    return (lam ** k) * exp(-lam) / factorial(k)



def normal_pdf(x, mu=0.0, sigma=1.0):
    coeff = 1.0 / (sigma * sqrt(TAU))
    expo = -((x - mu) ** 2) / (2 * sigma * sigma)
    return coeff * exp(expo)



def normal_cdf(x, mu=0.0, sigma=1.0):
    z = (x - mu) / (sigma * sqrt(2))
    return 0.5 * (1.0 + erf(z))



def exponential_pdf(x, lam):
    if x < 0:
        return 0.0
    return lam * exp(-lam * x)



def exponential_cdf(x, lam):
    if x < 0:
        return 0.0
    return 1.0 - exp(-lam * x)



def uniform_pdf(x, a, b):
    if x < a or x > b:
        return 0.0
    return 1.0 / (b - a)



def uniform_cdf(x, a, b):
    if x < a:
        return 0.0
    if x > b:
        return 1.0
    return (x - a) / (b - a)



def geometric_pdf(k, p):
    return ((1 - p) ** (k - 1)) * p



def binomial_mean(n, p):
    return n * p



def binomial_variance(n, p):
    return n * p * (1 - p)

