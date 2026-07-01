from .numtheory_core import gcd
from .basics import fabs, floor, ceil, trunc


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("fraction denominator cannot be zero")
        if isinstance(numerator, float) or isinstance(denominator, float):
            numerator = int(numerator * 10 ** 9)
            denominator = int(denominator * 10 ** 9)
        n, d = int(numerator), int(denominator)
        if d < 0:
            n, d = -n, -d
        g = gcd(abs(n), abs(d))
        self.numerator = n // g
        self.denominator = d // g

    def __repr__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + "/" + str(self.denominator)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return self.numerator == other * self.denominator

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        return self.numerator < other * self.denominator

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.__add__(-other)

    def __rsub__(self, other):
        return (-self).__add__(other)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator,
        )

    def __rtruediv__(self, other):
        return Fraction(other).__truediv__(self)

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return trunc(self.numerator / self.denominator)

    def __pow__(self, exp):
        if isinstance(exp, int):
            if exp >= 0:
                return Fraction(self.numerator ** exp, self.denominator ** exp)
            return Fraction(self.denominator ** (-exp), self.numerator ** (-exp))
        return float(self) ** exp

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def mixed_number(self):
        whole = self.numerator // self.denominator
        remainder = self.numerator % self.denominator
        return whole, Fraction(remainder, self.denominator)

    def is_proper(self):
        return abs(self.numerator) < self.denominator

    def limit_denominator(self, max_denominator=10 ** 6):
        if self.denominator <= max_denominator:
            return self
        p0, q0, p1, q1 = 0, 1, 1, 0
        n, d = self.numerator, self.denominator
        while True:
            a = n // d
            q2 = q0 + a * q1
            if q2 > max_denominator:
                break
            p0, q0, p1, q1 = p1, q1, p0 + a * p1, q2
            n, d = d, n - a * d
            if d == 0:
                break
        k = (max_denominator - q0) // q1
        b1 = Fraction(p0 + k * p1, q0 + k * q1)
        b2 = Fraction(p1, q1)
        if abs(abs(float(b2) - float(self)) - abs(float(b1) - float(self))) <= 0:
            return b2
        return b1


class FixedDecimal:
    def __init__(self, value=0, precision=2):
        self.precision = precision
        scale = 10 ** precision
        if isinstance(value, FixedDecimal):
            self._val = round(value._val * scale / (10 ** value.precision))
        elif isinstance(value, float):
            self._val = round(value * scale)
        elif isinstance(value, int):
            self._val = value * scale
        elif isinstance(value, str):
            self._val = round(float(value) * scale)
        else:
            self._val = round(float(value) * scale)
        self._scale = scale

    def __repr__(self):
        s = str(abs(self._val)).zfill(self.precision + 1)
        sign = "-" if self._val < 0 else ""
        return sign + s[:-self.precision] + "." + s[-self.precision:]

    def _make(self, val):
        r = FixedDecimal(0, self.precision)
        r._val = val
        r._scale = self._scale
        return r

    def __add__(self, other):
        if not isinstance(other, FixedDecimal):
            other = FixedDecimal(other, self.precision)
        return self._make(self._val + other._val)

    def __sub__(self, other):
        if not isinstance(other, FixedDecimal):
            other = FixedDecimal(other, self.precision)
        return self._make(self._val - other._val)

    def __mul__(self, other):
        if not isinstance(other, FixedDecimal):
            other = FixedDecimal(other, self.precision)
        return self._make((self._val * other._val) // self._scale)

    def __truediv__(self, other):
        if not isinstance(other, FixedDecimal):
            other = FixedDecimal(other, self.precision)
        if other._val == 0:
            raise ZeroDivisionError("decimal division by zero")
        return self._make((self._val * self._scale) // other._val)

    def __eq__(self, other):
        if isinstance(other, FixedDecimal):
            return self._val == other._val
        return float(self) == other

    def __lt__(self, other):
        if isinstance(other, FixedDecimal):
            return self._val < other._val
        return float(self) < other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __neg__(self):
        return self._make(-self._val)

    def __abs__(self):
        return self._make(abs(self._val))

    def __float__(self):
        return self._val / self._scale

    def __int__(self):
        return self._val // self._scale

    def round(self, places=0):
        shift = self.precision - places
        factor = 10 ** shift
        return self._make(round(self._val / factor) * factor)

    def is_negative(self):
        return self._val < 0

    def is_zero(self):
        return self._val == 0


class Interval:
    def __init__(self, lo, hi):
        if lo > hi:
            raise ValueError("interval lower bound must not exceed upper bound")
        self.lo = lo
        self.hi = hi

    def __repr__(self):
        return "[" + str(self.lo) + ", " + str(self.hi) + "]"

    def __contains__(self, x):
        return self.lo <= x <= self.hi

    def __eq__(self, other):
        return self.lo == other.lo and self.hi == other.hi

    def width(self):
        return self.hi - self.lo

    def midpoint(self):
        return (self.lo + self.hi) / 2.0

    def __add__(self, other):
        if isinstance(other, Interval):
            return Interval(self.lo + other.lo, self.hi + other.hi)
        return Interval(self.lo + other, self.hi + other)

    def __sub__(self, other):
        if isinstance(other, Interval):
            return Interval(self.lo - other.hi, self.hi - other.lo)
        return Interval(self.lo - other, self.hi - other)

    def __mul__(self, other):
        if isinstance(other, Interval):
            products = [
                self.lo * other.lo, self.lo * other.hi,
                self.hi * other.lo, self.hi * other.hi,
            ]
            return Interval(min(products), max(products))
        if other >= 0:
            return Interval(self.lo * other, self.hi * other)
        return Interval(self.hi * other, self.lo * other)

    def __truediv__(self, other):
        if isinstance(other, Interval):
            if 0 in other:
                raise ZeroDivisionError("interval division by zero-containing interval")
            return self * Interval(1.0 / other.hi, 1.0 / other.lo)
        if other == 0:
            raise ZeroDivisionError("interval division by zero")
        if other > 0:
            return Interval(self.lo / other, self.hi / other)
        return Interval(self.hi / other, self.lo / other)

    def intersects(self, other):
        return self.lo <= other.hi and other.lo <= self.hi

    def intersection(self, other):
        lo = max(self.lo, other.lo)
        hi = min(self.hi, other.hi)
        if lo > hi:
            return None
        return Interval(lo, hi)

    def union(self, other):
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi))

    def is_subset_of(self, other):
        return other.lo <= self.lo and self.hi <= other.hi

    def clamp(self, x):
        if x < self.lo:
            return self.lo
        if x > self.hi:
            return self.hi
        return x

    def split(self):
        mid = self.midpoint()
        return Interval(self.lo, mid), Interval(mid, self.hi)

    def expand(self, delta):
        return Interval(self.lo - delta, self.hi + delta)


class Ratio:
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError("ratio denominator cannot be zero")
        g = gcd(abs(int(a)), abs(int(b)))
        self.a = a // g
        self.b = b // g

    def __repr__(self):
        return str(self.a) + ":" + str(self.b)

    def __eq__(self, other):
        if isinstance(other, Ratio):
            return self.a * other.b == other.a * self.b
        return False

    def as_fraction(self):
        return Fraction(self.a, self.b)

    def as_float(self):
        return self.a / self.b

    def simplify(self):
        return Ratio(self.a, self.b)

    def scale(self, factor):
        return Ratio(self.a * factor, self.b * factor)

    def reciprocal(self):
        return Ratio(self.b, self.a)

    def combine(self, other):
        return Ratio(self.a * other.b + other.a * self.b, self.b * other.b)
