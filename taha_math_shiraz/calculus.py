from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, 
floor, ceil, fmod, remainder, modf


def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)



def second_derivative(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)



def integral_trapezoid(f, a, b, n=1000):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h



def integral_simpson(f, a, b, n=1000):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        total += f(x) * (4 if i % 2 == 1 else 2)
    return total * h / 3.0



def newton_raphson(f, fprime, x0, tol=1e-12, max_iter=200):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if fabs(fx) < tol:
            return x
        dfx = fprime(x)
        if dfx == 0:
            raise ValueError("derivative is zero")
        x = x - fx / dfx
    return x



def bisection_method(f, a, b, tol=1e-12, max_iter=500):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)
        if fabs(fc) < tol or (b - a) / 2 < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2.0



def taylor_series_exp(x, terms=20):
    total = 0.0
    term = 1.0
    for n in range(terms):
        total += term
        term *= x / (n + 1)
    return total



def secant_method(f, x0, x1, tol=1e-12, max_iter=200):
    for _ in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 == 0:
            raise ValueError("division by zero in secant method")
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if fabs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1



def golden_section_search(f, a, b, tol=1e-9):
    gr = (sqrt(5) - 1) / 2
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    while fabs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - gr * (b - a)
        d = a + gr * (b - a)
    return (b + a) / 2.0

