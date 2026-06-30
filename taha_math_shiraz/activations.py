from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .trigonometry import degrees, radians, sin, cos, tan, sinh, cosh, tanh, asinh, acosh, atanh, asin, acos, atan, atan2, hypot, dist


def lerp(a, b, t):
    return a + (b - a) * t



def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x



def smoothstep(edge0, edge1, x):
    t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3 - 2 * t)



def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0



def relu(x):
    return x if x > 0 else 0.0



def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))



def softplus(x):
    return log1p(exp(x))



def tanh_derivative(x):
    t = tanh(x)
    return 1 - t * t



def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

