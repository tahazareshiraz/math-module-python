_DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decimal_to_base(n, base):
    if base < 2 or base > 36:
        raise ValueError("base must be between 2 and 36")
    if n == 0:
        return "0"
    neg = n < 0
    n = abs(n)
    digits = []
    while n > 0:
        digits.append(_DIGITS[n % base])
        n //= base
    if neg:
        digits.append("-")
    return "".join(reversed(digits))


def base_to_decimal(s, base):
    if base < 2 or base > 36:
        raise ValueError("base must be between 2 and 36")
    s = s.upper()
    neg = s.startswith("-")
    if neg:
        s = s[1:]
    result = 0
    for char in s:
        value = _DIGITS.index(char)
        if value >= base:
            raise ValueError("invalid digit for base")
        result = result * base + value
    return -result if neg else result


def binary_to_decimal(s):
    return base_to_decimal(s, 2)


def decimal_to_binary(n):
    return decimal_to_base(n, 2)


def hex_to_decimal(s):
    return base_to_decimal(s, 16)


def decimal_to_hex(n):
    return decimal_to_base(n, 16)


def octal_to_decimal(s):
    return base_to_decimal(s, 8)


def decimal_to_octal(n):
    return decimal_to_base(n, 8)


def roman_to_decimal(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for char in reversed(s.upper()):
        value = values[char]
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total


def decimal_to_roman(n):
    if n <= 0 or n > 3999:
        raise ValueError("number out of range for roman numerals")
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = []
    for value, symbol in values:
        while n >= value:
            result.append(symbol)
            n -= value
    return "".join(result)


def celsius_to_fahrenheit(c):
    return c * 9.0 / 5.0 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0


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


def feet_to_meters(f):
    return f / 3.280839895


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


def bytes_to_kilobytes(b):
    return b / 1024.0


def bytes_to_megabytes(b):
    return b / (1024.0 ** 2)


def bytes_to_gigabytes(b):
    return b / (1024.0 ** 3)


def seconds_to_minutes(s):
    return s / 60.0


def seconds_to_hours(s):
    return s / 3600.0


def hours_to_seconds(h):
    return h * 3600.0


def minutes_to_seconds(m):
    return m * 60.0


def days_to_seconds(d):
    return d * 86400.0


def radians_to_gradians(r):
    from .constants import PI
    return r * 200.0 / PI


def gradians_to_radians(g):
    from .constants import PI
    return g * PI / 200.0


def joules_to_calories(j):
    return j / 4.184


def calories_to_joules(c):
    return c * 4.184


def pascals_to_atm(pa):
    return pa / 101325.0


def atm_to_pascals(atm):
    return atm * 101325.0
