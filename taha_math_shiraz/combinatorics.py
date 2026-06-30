from .aggregates import comb
from .numtheory_core import factorial


def permutations_list(iterable, r=None):
    pool = list(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return



def combinations_list(iterable, r):
    pool = list(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)



def cartesian_product(*pools):
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod_item in result:
        yield tuple(prod_item)



def power_set(iterable):
    items = list(iterable)
    n = len(items)
    for mask in range(1 << n):
        subset = [items[i] for i in range(n) if mask & (1 << i)]
        yield subset



def partitions(n, k=None):
    if k is None or k > n:
        k = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, k), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest



def derangement_count(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    a, b = 1, 0
    for i in range(2, n + 1):
        a, b = b, (i - 1) * (a + b)
    return b



def stirling_second(n, k):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    if k > n:
        return 0
    total = 0
    for j in range(k + 1):
        sign = 1 if (k - j) % 2 == 0 else -1
        total += sign * comb(k, j) * (j ** n)
    return total // factorial(k)



_bell_cache = {0: 1}



def bell_number(n):
    if n in _bell_cache:
        return _bell_cache[n]
    total = 0
    for k in range(n):
        total += comb(n - 1, k) * bell_number(k)
    _bell_cache[n] = total
    return total

