from .core import fabs


def bisection_root(f, a, b, tolerance=1e-10, max_iterations=200):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(max_iterations):
        mid = (a + b) / 2
        fmid = f(mid)
        if fabs(fmid) < tolerance or (b - a) / 2 < tolerance:
            return mid
        if fa * fmid < 0:
            b = mid
            fb = fmid
        else:
            a = mid
            fa = fmid
    return (a + b) / 2


def newton_raphson(f, fprime, x0, tolerance=1e-12, max_iterations=200):
    x = x0
    for _ in range(max_iterations):
        fx = f(x)
        if fabs(fx) < tolerance:
            return x
        fpx = fprime(x)
        if fpx == 0:
            raise ZeroDivisionError("derivative is zero")
        x_new = x - fx / fpx
        if fabs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x


def secant_method(f, x0, x1, tolerance=1e-12, max_iterations=200):
    for _ in range(max_iterations):
        f0, f1 = f(x0), f(x1)
        if f1 - f0 == 0:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if fabs(x2 - x1) < tolerance:
            return x2
        x0, x1 = x1, x2
    return x1


def fixed_point_iteration(g, x0, tolerance=1e-10, max_iterations=200):
    x = x0
    for _ in range(max_iterations):
        x_new = g(x)
        if fabs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x


def trapezoidal_rule(f, a, b, n=1000):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def simpsons_rule(f, a, b, n=1000):
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        coeff = 4 if i % 2 != 0 else 2
        total += coeff * f(a + i * h)
    return total * h / 3.0


def midpoint_rule(f, a, b, n=1000):
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        total += f(x_mid)
    return total * h


def derivative_numeric(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def second_derivative_numeric(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


def gradient_descent_1d(f, fprime, x0, learning_rate=0.01, iterations=1000):
    x = x0
    for _ in range(iterations):
        x -= learning_rate * fprime(x)
    return x


def euler_method(f, y0, t0, t1, steps):
    h = (t1 - t0) / steps
    t, y = t0, y0
    results = [(t, y)]
    for _ in range(steps):
        y = y + h * f(t, y)
        t = t + h
        results.append((t, y))
    return results


def runge_kutta_4(f, y0, t0, t1, steps):
    h = (t1 - t0) / steps
    t, y = t0, y0
    results = [(t, y)]
    for _ in range(steps):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h
        results.append((t, y))
    return results


def linear_interpolation(x0, y0, x1, y1, x):
    if x1 == x0:
        raise ValueError("x0 and x1 must differ")
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


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
