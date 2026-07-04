def to_base(n, base):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    neg = n < 0
    n = abs(n)
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return ("-" + result) if neg else result



def from_base(s, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    neg = s.startswith("-")
    if neg:
        s = s[1:]
    s = s.upper()
    result = 0
    for ch in s:
        result = result * base + digits.index(ch)
    return -result if neg else result



def roman_to_int(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        v = values[ch]
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total



def int_to_roman(n):
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = ""
    for v, sym in vals:
        while n >= v:
            result += sym
            n -= v
    return result

