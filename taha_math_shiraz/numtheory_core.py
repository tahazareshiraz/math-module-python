def factorial(n):
    if n != int(n):
        raise ValueError("factorial() only accepts integral values")
    n = int(n)
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result



def gcd(*args):
    if len(args) == 0:
        return 0
    result = abs(int(args[0]))
    for a in args[1:]:
        a = abs(int(a))
        while a:
            result, a = a, result % a
    return result



def lcm(*args):
    if len(args) == 0:
        return 1
    result = abs(int(args[0]))
    for a in args[1:]:
        a = abs(int(a))
        if result == 0 or a == 0:
            result = 0
            continue
        result = result * a // gcd(result, a)
    return result



def isqrt(n):
    n = int(n)
    if n < 0:
        raise ValueError("isqrt() argument must be nonnegative")
    if n == 0:
        return 0
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

