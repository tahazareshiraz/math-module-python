def set_union(a, b):
    return set(a) | set(b)


def set_intersection(a, b):
    return set(a) & set(b)


def set_difference(a, b):
    return set(a) - set(b)


def set_symmetric_difference(a, b):
    return set(a) ^ set(b)


def is_subset(a, b):
    return set(a).issubset(set(b))


def is_superset(a, b):
    return set(a).issuperset(set(b))


def is_disjoint(a, b):
    return set(a).isdisjoint(set(b))


def power_set(items):
    items = list(items)
    n = len(items)
    result = []
    for i in range(2 ** n):
        subset = [items[j] for j in range(n) if (i >> j) & 1]
        result.append(subset)
    return result


def cartesian_product(a, b):
    return [(x, y) for x in a for y in b]


def jaccard_similarity(a, b):
    set_a, set_b = set(a), set(b)
    union = set_a | set_b
    if not union:
        return 1.0
    return len(set_a & set_b) / len(union)


def logical_and(a, b):
    return a and b


def logical_or(a, b):
    return a or b


def logical_not(a):
    return not a


def logical_xor(a, b):
    return bool(a) != bool(b)


def logical_implies(a, b):
    return (not a) or b


def logical_iff(a, b):
    return bool(a) == bool(b)


def truth_table(n_vars, expression):
    rows = []
    for i in range(2 ** n_vars):
        values = [(i >> j) & 1 for j in range(n_vars - 1, -1, -1)]
        bool_values = [bool(v) for v in values]
        result = expression(*bool_values)
        rows.append((tuple(values), result))
    return rows


def is_tautology(n_vars, expression):
    return all(result for _, result in truth_table(n_vars, expression))


def is_contradiction(n_vars, expression):
    return all(not result for _, result in truth_table(n_vars, expression))


def bitwise_and(a, b):
    return a & b


def bitwise_or(a, b):
    return a | b


def bitwise_xor(a, b):
    return a ^ b


def bitwise_not(a, bits=32):
    mask = (1 << bits) - 1
    return (~a) & mask


def bitwise_shift_left(a, n):
    return a << n


def bitwise_shift_right(a, n):
    return a >> n


def count_set_bits(n):
    count = 0
    n = abs(n)
    while n:
        count += n & 1
        n >>= 1
    return count


def is_subset_sum_possible(numbers, target):
    n = len(numbers)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for s in range(1, target + 1):
            dp[i][s] = dp[i - 1][s]
            if numbers[i - 1] <= s:
                dp[i][s] = dp[i][s] or dp[i - 1][s - numbers[i - 1]]
    return dp[n][target]


def power_set_size(n):
    return 2 ** n


def relation_is_reflexive(relation, elements):
    return all((x, x) in relation for x in elements)


def relation_is_symmetric(relation):
    return all((b, a) in relation for a, b in relation)


def relation_is_transitive(relation):
    relation_set = set(relation)
    for a, b in relation_set:
        for c, d in relation_set:
            if b == c and (a, d) not in relation_set:
                return False
    return True


def relation_is_equivalence(relation, elements):
    return (
        relation_is_reflexive(relation, elements)
        and relation_is_symmetric(relation)
        and relation_is_transitive(relation)
    )
