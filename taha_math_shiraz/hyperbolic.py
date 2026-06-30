from .core import fabs, isclose
from .power import exp, log, sqrt


def sinh(x):
    return (exp(x) - exp(-x)) / 2.0


def cosh(x):
    return (exp(x) + exp(-x)) / 2.0


def tanh(x):
    if x > 20:
        return 1.0
    if x < -20:
        return -1.0
    e2x = exp(2 * x)
    return (e2x - 1) / (e2x + 1)


def sech(x):
    return 1.0 / cosh(x)


def csch(x):
    s = sinh(x)
    if s == 0:
        raise ValueError("math domain error")
    return 1.0 / s


def coth(x):
    t = tanh(x)
    if t == 0:
        raise ValueError("math domain error")
    return 1.0 / t


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


def asech(x):
    if x <= 0 or x > 1:
        raise ValueError("math domain error")
    return acosh(1.0 / x)


def acsch(x):
    if x == 0:
        raise ValueError("math domain error")
    return asinh(1.0 / x)


def acoth(x):
    if -1 <= x <= 1:
        raise ValueError("math domain error")
    return atanh(1.0 / x)


def gudermannian(x):
    from .trigonometry import atan
    return 2 * atan(tanh(x / 2))


def inverse_gudermannian(x):
    from .trigonometry import tan
    return 2 * atanh(tan(x / 2))


def hyperbolic_identity_check(x, tol=1e-9):
    return isclose(cosh(x) * cosh(x) - sinh(x) * sinh(x), 1.0, rel_tol=tol)
