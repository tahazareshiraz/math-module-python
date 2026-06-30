from .core import isqrt, gcd, digit_sum, reverse_digits


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def next_prime(n):
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def prev_prime(n):
    candidate = n - 1
    while candidate >= 2 and not is_prime(candidate):
        candidate -= 1
    if candidate < 2:
        raise ValueError("no prime before given value")
    return candidate


def prime_factors(n):
    n = abs(int(n))
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def prime_factorization(n):
    factors = prime_factors(n)
    result = {}
    for f in factors:
        result[f] = result.get(f, 0) + 1
    return result


def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, isqrt(limit) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return [i for i, p in enumerate(is_p) if p]


def count_primes_below(limit):
    return len(sieve_of_eratosthenes(limit - 1)) if limit > 0 else 0


def divisors(n):
    n = abs(int(n))
    if n == 0:
        return []
    small = []
    large = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
        i += 1
    return small + large[::-1]


def proper_divisors(n):
    return [d for d in divisors(n) if d != n]


def count_divisors(n):
    return len(divisors(n))


def sum_divisors(n):
    return sum(divisors(n))


def is_perfect_number(n):
    if n <= 1:
        return False
    return sum(proper_divisors(n)) == n


def is_abundant(n):
    if n <= 1:
        return False
    return sum(proper_divisors(n)) > n


def is_deficient(n):
    if n <= 1:
        return True
    return sum(proper_divisors(n)) < n


def are_amicable(a, b):
    if a == b:
        return False
    return sum(proper_divisors(a)) == b and sum(proper_divisors(b)) == a


def euler_totient(n):
    n = int(n)
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def is_coprime(a, b):
    return gcd(a, b) == 1


def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return (old_r, old_s, old_t)


def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("modular inverse does not exist")
    return x % m


def mod_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n)


def is_palindrome_number(n):
    return n == reverse_digits(n)


def digital_root(n):
    n = abs(int(n))
    while n >= 10:
        n = digit_sum(n)
    return n


def collatz_sequence(n):
    if n <= 0:
        raise ValueError("n must be positive")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def collatz_length(n):
    return len(collatz_sequence(n))


def is_twin_prime(n):
    return is_prime(n) and (is_prime(n - 2) or is_prime(n + 2))


def goldbach_pair(n):
    if n <= 2 or n % 2 != 0:
        raise ValueError("n must be even and greater than 2")
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            return (i, n - i)
    return None


def is_carmichael(n):
    if n < 2 or is_prime(n):
        return False
    factors = prime_factorization(n)
    if any(power > 1 for power in factors.values()):
        return False
    for p in factors:
        if (n - 1) % (p - 1) != 0:
            return False
    return True


def is_squarefree(n):
    n = abs(int(n))
    factors = prime_factorization(n)
    return all(power == 1 for power in factors.values())


def mobius(n):
    if n == 1:
        return 1
    factors = prime_factorization(n)
    if any(power > 1 for power in factors.values()):
        return 0
    return -1 if len(factors) % 2 == 1 else 1


def jacobi_symbol(a, n):
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0


def pythagorean_triple(m, n):
    if m <= n or n <= 0:
        raise ValueError("require m > n > 0")
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    return (a, b, c)


def is_pythagorean_triple(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
