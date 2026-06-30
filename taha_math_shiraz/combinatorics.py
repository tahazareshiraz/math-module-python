from .core import factorial, comb


def double_factorial(n):
    if n < 0:
        raise ValueError("double_factorial() not defined for negative values")
    result = 1
    while n > 1:
        result *= n
        n -= 2
    return result


def fibonacci(n):
    if n < 0:
        raise ValueError("fibonacci() not defined for negative values")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_sequence(count):
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def lucas_number(n):
    if n < 0:
        raise ValueError("lucas_number() not defined for negative values")
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas_sequence(count):
    sequence = []
    a, b = 2, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def tribonacci(n):
    if n < 0:
        raise ValueError("tribonacci() not defined for negative values")
    a, b, c = 0, 1, 1
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a


def catalan_number(n):
    if n < 0:
        raise ValueError("catalan_number() not defined for negative values")
    return comb(2 * n, n) // (n + 1)


def catalan_sequence(count):
    return [catalan_number(i) for i in range(count)]


def binomial_coefficient(n, k):
    return comb(n, k)


def multinomial_coefficient(n, *ks):
    if sum(ks) != n:
        raise ValueError("sum of ks must equal n")
    result = factorial(n)
    for k in ks:
        result //= factorial(k)
    return result


def stirling_second(n, k):
    if k == 0 and n == 0:
        return 1
    if k == 0 or k > n:
        return 0
    if k == n:
        return 1
    return k * stirling_second(n - 1, k) + stirling_second(n - 1, k - 1)


def stirling_first(n, k):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    if k > n:
        return 0
    return stirling_first(n - 1, k - 1) - (n - 1) * stirling_first(n - 1, k)


def bell_number(n):
    if n == 0:
        return 1
    triangle = [[0] * (n + 1) for _ in range(n + 1)]
    triangle[0][0] = 1
    for i in range(1, n + 1):
        triangle[i][0] = triangle[i - 1][i - 1]
        for j in range(1, i + 1):
            triangle[i][j] = triangle[i][j - 1] + triangle[i - 1][j - 1]
    return triangle[n][0]


def derangements(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    a, b = 1, 0
    for i in range(2, n + 1):
        a, b = b, (i - 1) * (a + b)
    return b


def partitions_count(n):
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            dp[i] += dp[i - k]
    return dp[n]


def compositions_count(n):
    if n <= 0:
        return 0
    return 2 ** (n - 1)


def generate_permutations(items):
    items = list(items)
    if len(items) <= 1:
        return [items]
    result = []
    for i in range(len(items)):
        rest = items[:i] + items[i + 1:]
        for p in generate_permutations(rest):
            result.append([items[i]] + p)
    return result


def generate_combinations(items, k):
    items = list(items)
    n = len(items)
    if k > n or k < 0:
        return []
    if k == 0:
        return [[]]
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n):
            path.append(items[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def generate_combinations_with_repetition(items, k):
    items = list(items)
    n = len(items)
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n):
            path.append(items[i])
            backtrack(i, path)
            path.pop()

    backtrack(0, [])
    return result


def pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [comb(i, j) for j in range(i + 1)]
        triangle.append(row)
    return triangle


def motzkin_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + sum(dp[k] * dp[i - 2 - k] for k in range(i - 1))
    return dp[n]


def narayana_number(n, k):
    if k < 1 or k > n:
        return 0
    return (comb(n, k) * comb(n, k - 1)) // n
