from .aggregates import fsum, prod, isclose, comb, perm
from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .basics import floor, ceil


def mean(data):
    data = list(data)
    if not data:
        raise ValueError("mean requires at least one data point")
    return fsum(data) / len(data)



def geometric_mean(data):
    data = list(data)
    if not data:
        raise ValueError("geometric_mean requires at least one data point")
    total_log = 0.0
    for x in data:
        total_log += log(x)
    return exp(total_log / len(data))



def harmonic_mean(data):
    data = list(data)
    if not data:
        raise ValueError("harmonic_mean requires at least one data point")
    total = 0.0
    for x in data:
        if x == 0:
            return 0.0
        total += 1.0 / x
    return len(data) / total



def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise ValueError("median requires at least one data point")
    mid = n // 2
    if n % 2 == 1:
        return float(data[mid])
    return (data[mid - 1] + data[mid]) / 2.0



def median_low(data):
    data = sorted(data)
    n = len(data)
    mid = (n - 1) // 2
    return data[mid]



def median_high(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2
    return data[mid]



def mode(data):
    data = list(data)
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    best = None
    best_count = -1
    for x in data:
        if counts[x] > best_count:
            best_count = counts[x]
            best = x
    return best



def multimode(data):
    data = list(data)
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    if not counts:
        return []
    max_count = max(counts.values())
    result = []
    seen = set()
    for x in data:
        if counts[x] == max_count and x not in seen:
            result.append(x)
            seen.add(x)
    return result



def variance(data, xbar=None):
    data = list(data)
    n = len(data)
    if n < 2:
        raise ValueError("variance requires at least two data points")
    m = xbar if xbar is not None else mean(data)
    total = 0.0
    for x in data:
        total += (x - m) ** 2
    return total / (n - 1)



def pvariance(data, mu=None):
    data = list(data)
    n = len(data)
    if n < 1:
        raise ValueError("pvariance requires at least one data point")
    m = mu if mu is not None else mean(data)
    total = 0.0
    for x in data:
        total += (x - m) ** 2
    return total / n



def stdev(data, xbar=None):
    return sqrt(variance(data, xbar))



def pstdev(data, mu=None):
    return sqrt(pvariance(data, mu))



def covariance(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("x and y must have the same length")
    if n < 2:
        raise ValueError("covariance requires at least two data points")
    mx = mean(x)
    my = mean(y)
    total = 0.0
    for xi, yi in zip(x, y):
        total += (xi - mx) * (yi - my)
    return total / (n - 1)



def correlation(x, y):
    sx = stdev(x)
    sy = stdev(y)
    if sx == 0 or sy == 0:
        raise ValueError("correlation requires nonzero variance")
    return covariance(x, y) / (sx * sy)



def linear_regression(x, y):
    n = len(x)
    mx = mean(x)
    my = mean(y)
    num = 0.0
    den = 0.0
    for xi, yi in zip(x, y):
        num += (xi - mx) * (yi - my)
        den += (xi - mx) ** 2
    if den == 0:
        raise ValueError("x values are constant")
    slope = num / den
    intercept = my - slope * mx
    return slope, intercept



def quantiles(data, n=4):
    data = sorted(data)
    m = len(data)
    if m < 2:
        raise ValueError("quantiles requires at least two data points")
    result = []
    for i in range(1, n):
        j = i * (m - 1) / n
        lo = int(floor(j))
        hi = int(ceil(j))
        frac = j - lo
        result.append(data[lo] + (data[hi] - data[lo]) * frac)
    return result



def z_score(x, data):
    return (x - mean(data)) / stdev(data)



def range_(data):
    data = list(data)
    return max(data) - min(data)



def midrange(data):
    data = list(data)
    return (max(data) + min(data)) / 2.0



def skewness(data):
    data = list(data)
    n = len(data)
    m = mean(data)
    s = pstdev(data)
    if s == 0:
        return 0.0
    total = 0.0
    for x in data:
        total += ((x - m) / s) ** 3
    return total / n



def kurtosis(data):
    data = list(data)
    n = len(data)
    m = mean(data)
    s = pstdev(data)
    if s == 0:
        return 0.0
    total = 0.0
    for x in data:
        total += ((x - m) / s) ** 4
    return total / n - 3.0

