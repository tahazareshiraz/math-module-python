from .power import sqrt, exp, log
from .trigonometry import sin, cos, atan2


class ComplexNumber:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        sign_str = "+" if self.imag >= 0 else "-"
        return str(self.real) + sign_str + str(abs(self.imag)) + "i"

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def divide(self, other):
        denom = other.real ** 2 + other.imag ** 2
        if denom == 0:
            raise ZeroDivisionError("division by zero complex number")
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def modulus(self):
        return sqrt(self.real ** 2 + self.imag ** 2)

    def argument(self):
        return atan2(self.imag, self.real)

    def to_polar(self):
        return (self.modulus(), self.argument())

    def power(self, n):
        r, theta = self.to_polar()
        new_r = r ** n
        new_theta = theta * n
        return ComplexNumber(new_r * cos(new_theta), new_r * sin(new_theta))

    def sqrt(self):
        r, theta = self.to_polar()
        new_r = sqrt(r)
        new_theta = theta / 2
        return ComplexNumber(new_r * cos(new_theta), new_r * sin(new_theta))

    def exp(self):
        e_real = exp(self.real)
        return ComplexNumber(e_real * cos(self.imag), e_real * sin(self.imag))

    def log(self):
        return ComplexNumber(log(self.modulus()), self.argument())

    def negate(self):
        return ComplexNumber(-self.real, -self.imag)

    def is_real(self):
        return self.imag == 0

    def is_imaginary(self):
        return self.real == 0


def complex_from_polar(r, theta):
    return ComplexNumber(r * cos(theta), r * sin(theta))


def complex_add(a, b):
    return a.add(b)


def complex_sub(a, b):
    return a.subtract(b)


def complex_mul(a, b):
    return a.multiply(b)


def complex_div(a, b):
    return a.divide(b)


def complex_roots_of_unity(n):
    from .constants import TAU
    return [complex_from_polar(1.0, TAU * k / n) for k in range(n)]


def complex_distance(a, b):
    return a.subtract(b).modulus()


def complex_sum(numbers):
    result = ComplexNumber(0, 0)
    for n in numbers:
        result = result.add(n)
    return result
