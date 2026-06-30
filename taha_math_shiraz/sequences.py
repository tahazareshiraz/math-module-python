from .power import sqrt


def arithmetic_sequence(first, diff, count):
    return [first + i * diff for i in range(count)]


def arithmetic_sum(first, diff, count):
    return count * (2 * first + (count - 1) * diff) / 2


def arithmetic_nth_term(first, diff, n):
    return first + (n - 1) * diff


def geometric_sequence(first, ratio, count):
    return [first * (ratio ** i) for i in range(count)]


def geometric_sum(first, ratio, count):
    if ratio == 1:
        return first * count
    return first * (1 - ratio ** count) / (1 - ratio)


def geometric_nth_term(first, ratio, n):
    return first * (ratio ** (n - 1))


def infinite_geometric_sum(first, ratio):
    if abs(ratio) >= 1:
        raise ValueError("series does not converge")
    return first / (1 - ratio)


def harmonic_sequence(count):
    return [1.0 / n for n in range(1, count + 1)]


def harmonic_sum(count):
    return sum(1.0 / n for n in range(1, count + 1))


def triangular_number(n):
    return n * (n + 1) // 2


def is_triangular(n):
    if n < 0:
        return False
    x = (sqrt(8 * n + 1) - 1) / 2
    return abs(x - round(x)) < 1e-9


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


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


def sum_of_cubes(n):
    return (n * (n + 1) // 2) ** 2


def sum_of_natural_numbers(n):
    return n * (n + 1) // 2


def power_sum(n, p):
    return sum(i ** p for i in range(1, n + 1))


def sequence_differences(sequence):
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def is_arithmetic(sequence):
    diffs = sequence_differences(sequence)
    return len(set(diffs)) <= 1


def is_geometric(sequence):
    if any(v == 0 for v in sequence[:-1]):
        return False
    ratios = [sequence[i + 1] / sequence[i] for i in range(len(sequence) - 1)]
    first = ratios[0]
    return all(abs(r - first) < 1e-9 for r in ratios)


def pell_number(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, 2 * b + a
    return b


def padovan_sequence(count):
    sequence = [1, 1, 1]
    while len(sequence) < count:
        sequence.append(sequence[-2] + sequence[-3])
    return sequence[:count]


def recaman_sequence(count):
    sequence = [0]
    seen = {0}
    for n in range(1, count):
        prev = sequence[-1]
        candidate = prev - n
        if candidate > 0 and candidate not in seen:
            sequence.append(candidate)
        else:
            sequence.append(prev + n)
        seen.add(sequence[-1])
    return sequence


def look_and_say(n, start="1"):
    result = start
    for _ in range(n):
        next_result = []
        i = 0
        while i < len(result):
            count = 1
            while i + 1 < len(result) and result[i] == result[i + 1]:
                i += 1
                count += 1
            next_result.append(str(count) + result[i])
            i += 1
        result = "".join(next_result)
    return result
