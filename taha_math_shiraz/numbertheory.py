from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .aggregates import fsum, prod, isclose, comb, perm
from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf
from .numtheory_core import factorial, gcd, lcm, isqrt


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True



def next_prime(n):
    n = int(n) + 1
    while not is_prime(n):
        n += 1
    return n



def prev_prime(n):
    n = int(n) - 1
    while n > 1 and not is_prime(n):
        n -= 1
    if n < 2:
        raise ValueError("no previous prime")
    return n



def prime_factors(n):
    n = int(n)
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors



def prime_factorization(n):
    factors = prime_factors(n)
    result = {}
    for f in factors:
        result[f] = result.get(f, 0) + 1
    return result



def divisors(n):
    n = int(n)
    result = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
        i += 1
    return sorted(result)



def divisor_count(n):
    return len(divisors(n))



def divisor_sum(n):
    return sum(divisors(n))



def is_perfect(n):
    return n > 0 and divisor_sum(n) - n == n



def is_abundant(n):
    return n > 0 and divisor_sum(n) - n > n



def is_deficient(n):
    return n > 0 and divisor_sum(n) - n < n



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



def mobius(n):
    n = int(n)
    if n == 1:
        return 1
    factors = prime_factorization(n)
    for exp_ in factors.values():
        if exp_ > 1:
            return 0
    return -1 if len(factors) % 2 else 1



def fibonacci(n):
    n = int(n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a



def lucas(n):
    n = int(n)
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a



def tribonacci(n):
    n = int(n)
    a, b, c = 0, 1, 1
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(n - 1):
        a, b, c = b, c, a + b + c
    return c



def catalan(n):
    return comb(2 * n, n) // (n + 1)



def bernoulli(n):
    if n == 0:
        return 1.0
    if n == 1:
        return -0.5
    if n % 2 == 1:
        return 0.0
    A = [0.0] * (n + 1)
    for m in range(n + 1):
        A[m] = 1.0 / (m + 1)
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
    return A[0]



def harmonic(n):
    total = 0.0
    for i in range(1, n + 1):
        total += 1.0 / i
    return total



def digit_sum(n):
    n = abs(int(n))
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total



def digit_product(n):
    n = abs(int(n))
    result = 1
    while n > 0:
        result *= n % 10
        n //= 10
    return result



def digital_root(n):
    n = abs(int(n))
    while n >= 10:
        n = digit_sum(n)
    return n



def is_palindrome_number(n):
    s = str(abs(int(n)))
    return s == s[::-1]



def is_armstrong(n):
    s = str(int(n))
    power = len(s)
    return sum(int(d) ** power for d in s) == int(n)



def collatz_length(n):
    n = int(n)
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count



def is_power_of_two(n):
    n = int(n)
    return n > 0 and (n & (n - 1)) == 0



def bit_length(n):
    n = abs(int(n))
    count = 0
    while n > 0:
        n >>= 1
        count += 1
    return count



def popcount(n):
    n = abs(int(n))
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count



def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t



def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % m



def mod_pow(base, exp_, mod):
    result = 1
    base %= mod
    while exp_ > 0:
        if exp_ & 1:
            result = (result * base) % mod
        exp_ >>= 1
        base = (base * base) % mod
    return result



def chinese_remainder(remainders, moduli):
    total = 0
    prod_all = prod(moduli)
    for r_i, m_i in zip(remainders, moduli):
        p = prod_all // m_i
        total += r_i * mod_inverse(p, m_i) * p
    return total % prod_all



def is_coprime(a, b):
    return gcd(a, b) == 1



def jacobi_symbol(a, n):
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be odd and positive")
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    if n == 1:
        return result
    return 0



def sieve_of_eratosthenes(limit):
    limit = int(limit)
    is_p = [True] * (limit + 1)
    if limit >= 0:
        is_p[0] = False
    if limit >= 1:
        is_p[1] = False
    i = 2
    while i * i <= limit:
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
        i += 1
    return [i for i, v in enumerate(is_p) if v]



def count_primes_below(limit):
    return len(sieve_of_eratosthenes(limit - 1))



def goldbach_pair(n):
    n = int(n)
    if n % 2 != 0 or n < 4:
        raise ValueError("n must be an even number >= 4")
    for p in sieve_of_eratosthenes(n):
        if is_prime(n - p):
            return (p, n - p)
    raise ValueError("no pair found")



def is_amicable_pair(a, b):
    return a != b and divisor_sum(a) - a == b and divisor_sum(b) - b == a



def find_amicable_pairs(limit):
    pairs = []
    for a in range(2, limit):
        b = divisor_sum(a) - a
        if b > a and divisor_sum(b) - b == a:
            pairs.append((a, b))
    return pairs



def polygonal_number(s, n):
    return ((s - 2) * n * n - (s - 4) * n) // 2



def triangular_number(n):
    return n * (n + 1) // 2



def square_number(n):
    return n * n



def pentagonal_number(n):
    return n * (3 * n - 1) // 2



def hexagonal_number(n):
    return n * (2 * n - 1)



def heptagonal_number(n):
    return n * (5 * n - 3) // 2



def octagonal_number(n):
    return n * (3 * n - 2)



def is_triangular(n):
    x = (sqrt(8 * n + 1) - 1) / 2
    return x == trunc(x)



def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n



def is_pentagonal(n):
    x = (sqrt(24 * n + 1) + 1) / 6
    return x == trunc(x)



def pascal_triangle_row(n):
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row



def pascal_triangle(rows):
    return [pascal_triangle_row(i) for i in range(rows)]



def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6



def sum_of_cubes(n):
    return (n * (n + 1) // 2) ** 2



def is_perfect_square_fast(n):
    if n < 0:
        return False
    x = isqrt(n)
    return x * x == n

