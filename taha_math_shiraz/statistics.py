from .power import sqrt
from .core import fabs


def mean(data):
    data = list(data)
    if not data:
        raise ValueError("mean() requires at least one data point")
    return sum(data) / len(data)


def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise ValueError("median() requires at least one data point")
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]


def mode(data):
    data = list(data)
    if not data:
        raise ValueError("mode() requires at least one data point")
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    for value in data:
        if counts[value] == max_count:
            return value


def multimode(data):
    data = list(data)
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    result = []
    for value in data:
        if counts[value] == max_count and value not in result:
            result.append(value)
    return result


def variance(data):
    data = list(data)
    n = len(data)
    if n < 2:
        raise ValueError("variance() requires at least two data points")
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (n - 1)


def pvariance(data):
    data = list(data)
    n = len(data)
    if n < 1:
        raise ValueError("pvariance() requires at least one data point")
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / n


def stdev(data):
    return sqrt(variance(data))


def pstdev(data):
    return sqrt(pvariance(data))


def data_range(data):
    data = list(data)
    if not data:
        raise ValueError("data_range() requires at least one data point")
    return max(data) - min(data)


def percentile(data, p):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise ValueError("percentile() requires at least one data point")
    if p <= 0:
        return data[0]
    if p >= 100:
        return data[-1]
    k = (n - 1) * (p / 100)
    f = int(k)
    c = f + 1 if f + 1 < n else f
    d = k - f
    return data[f] + d * (data[c] - data[f])


def quartiles(data):
    return (percentile(data, 25), percentile(data, 50), percentile(data, 75))


def iqr(data):
    q1, _, q3 = quartiles(data)
    return q3 - q1


def covariance(x, y):
    x = list(x)
    y = list(y)
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    n = len(x)
    if n < 2:
        raise ValueError("covariance() requires at least two data points")
    mx = mean(x)
    my = mean(y)
    return sum((x[i] - mx) * (y[i] - my) for i in range(n)) / (n - 1)


def correlation(x, y):
    sx = stdev(x)
    sy = stdev(y)
    if sx == 0 or sy == 0:
        raise ValueError("correlation undefined when variance is zero")
    return covariance(x, y) / (sx * sy)


def skewness(data):
    data = list(data)
    n = len(data)
    if n < 3:
        raise ValueError("skewness() requires at least three data points")
    m = mean(data)
    s = pstdev(data)
    if s == 0:
        return 0.0
    return (sum((x - m) ** 3 for x in data) / n) / (s ** 3)


def kurtosis(data):
    data = list(data)
    n = len(data)
    if n < 4:
        raise ValueError("kurtosis() requires at least four data points")
    m = mean(data)
    s = pstdev(data)
    if s == 0:
        return 0.0
    return (sum((x - m) ** 4 for x in data) / n) / (s ** 4) - 3


def z_score(x, data):
    m = mean(data)
    s = stdev(data)
    if s == 0:
        raise ValueError("z_score undefined when standard deviation is zero")
    return (x - m) / s


def geometric_mean(data):
    data = list(data)
    if not data:
        raise ValueError("geometric_mean() requires at least one data point")
    product = 1.0
    for value in data:
        if value <= 0:
            raise ValueError("geometric_mean() requires positive values")
        product *= value
    return product ** (1.0 / len(data))


def harmonic_mean(data):
    data = list(data)
    if not data:
        raise ValueError("harmonic_mean() requires at least one data point")
    if any(value == 0 for value in data):
        return 0.0
    return len(data) / sum(1.0 / value for value in data)


def weighted_mean(data, weights):
    data = list(data)
    weights = list(weights)
    if len(data) != len(weights):
        raise ValueError("data and weights must have the same length")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("sum of weights must not be zero")
    return sum(d * w for d, w in zip(data, weights)) / total_weight


def moving_average(data, window):
    data = list(data)
    if window <= 0 or window > len(data):
        raise ValueError("invalid window size")
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i + window]) / window)
    return result


def cumulative_sum(data):
    result = []
    total = 0
    for value in data:
        total += value
        result.append(total)
    return result


def normalize_data(data):
    data = list(data)
    lo = min(data)
    hi = max(data)
    if hi == lo:
        return [0.0 for _ in data]
    return [(x - lo) / (hi - lo) for x in data]


def standardize_data(data):
    m = mean(data)
    s = stdev(data)
    if s == 0:
        return [0.0 for _ in data]
    return [(x - m) / s for x in data]


def mean_absolute_deviation(data):
    data = list(data)
    m = mean(data)
    return sum(fabs(x - m) for x in data) / len(data)


def coefficient_of_variation(data):
    m = mean(data)
    if m == 0:
        raise ValueError("coefficient_of_variation undefined when mean is zero")
    return stdev(data) / m


def root_mean_square(data):
    data = list(data)
    if not data:
        raise ValueError("root_mean_square() requires at least one data point")
    return sqrt(sum(x * x for x in data) / len(data))


def frequency_table(data):
    table = {}
    for value in data:
        table[value] = table.get(value, 0) + 1
    return table
