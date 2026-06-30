def clamp(x, lo, hi):
    if lo > hi:
        raise ValueError("lo must be less than or equal to hi")
    return max(lo, min(hi, x))


def lerp(a, b, t):
    return a + (b - a) * t


def inverse_lerp(a, b, value):
    if a == b:
        raise ValueError("a and b must differ")
    return (value - a) / (b - a)


def map_range(value, in_min, in_max, out_min, out_max):
    t = inverse_lerp(in_min, in_max, value)
    return lerp(out_min, out_max, t)


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def is_close(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance


def normalize_angle(angle, period=360):
    result = angle % period
    if result < 0:
        result += period
    return result


def wrap(value, lo, hi):
    span = hi - lo
    if span == 0:
        return lo
    return lo + (value - lo) % span


def smoothstep(edge0, edge1, x):
    if edge0 == edge1:
        raise ValueError("edge0 and edge1 must differ")
    t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def smootherstep(edge0, edge1, x):
    t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * t * (t * (t * 6 - 15) + 10)


def step(edge, x):
    return 0.0 if x < edge else 1.0


def ping_pong(t, length):
    t = t % (2 * length)
    if t < length:
        return t
    return 2 * length - t


def remap_clamped(value, in_min, in_max, out_min, out_max):
    value = clamp(value, min(in_min, in_max), max(in_min, in_max))
    return map_range(value, in_min, in_max, out_min, out_max)


def approx_equal_list(a, b, tolerance=1e-9):
    if len(a) != len(b):
        return False
    return all(is_close(x, y, tolerance) for x, y in zip(a, b))


def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk_list(data, size):
    if size <= 0:
        raise ValueError("size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]


def transpose_list(matrix):
    return [list(row) for row in zip(*matrix)]


def linspace(start, stop, num):
    if num < 2:
        return [start]
    step_size = (stop - start) / (num - 1)
    return [start + i * step_size for i in range(num)]


def arange(start, stop, step_size=1):
    result = []
    current = start
    if step_size > 0:
        while current < stop:
            result.append(current)
            current += step_size
    elif step_size < 0:
        while current > stop:
            result.append(current)
            current += step_size
    return result


def safe_divide(a, b, default=0.0):
    if b == 0:
        return default
    return a / b


def percentage_change(old_value, new_value):
    if old_value == 0:
        raise ValueError("old_value must not be zero")
    return (new_value - old_value) / old_value * 100


def percentage_of(part, whole):
    if whole == 0:
        raise ValueError("whole must not be zero")
    return part / whole * 100


def value_from_percentage(percentage, whole):
    return percentage / 100 * whole


def round_to_nearest(value, multiple):
    if multiple == 0:
        raise ValueError("multiple must not be zero")
    return round(value / multiple) * multiple


def truncate_decimals(value, places):
    factor = 10 ** places
    return int(value * factor) / factor


def split_integer_fraction(value):
    integer_part = int(value)
    fraction_part = value - integer_part
    return (integer_part, fraction_part)


def average_of(*values):
    if not values:
        raise ValueError("at least one value is required")
    return sum(values) / len(values)


def min_max(data):
    data = list(data)
    if not data:
        raise ValueError("data must not be empty")
    return (min(data), max(data))


def is_within_range(value, lo, hi):
    return lo <= value <= hi

