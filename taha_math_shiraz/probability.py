from .constants import PI
from .core import factorial, comb
from .power import exp, sqrt, pow_
from .special_functions import erf


def factorial_probability(n, k, p):
    return comb(n, k) * pow_(p, k) * pow_(1 - p, n - k)


def binomial_pmf(k, n, p):
    if k < 0 or k > n:
        return 0.0
    return comb(n, k) * pow_(p, k) * pow_(1 - p, n - k)


def binomial_cdf(k, n, p):
    return sum(binomial_pmf(i, n, p) for i in range(0, k + 1))


def binomial_mean(n, p):
    return n * p


def binomial_variance(n, p):
    return n * p * (1 - p)


def poisson_pmf(k, lam):
    if k < 0:
        return 0.0
    return (pow_(lam, k) * exp(-lam)) / factorial(k)


def poisson_cdf(k, lam):
    return sum(poisson_pmf(i, lam) for i in range(0, k + 1))


def geometric_pmf(k, p):
    if k < 1:
        return 0.0
    return pow_(1 - p, k - 1) * p


def geometric_cdf(k, p):
    if k < 1:
        return 0.0
    return 1 - pow_(1 - p, k)


def hypergeometric_pmf(k, population, successes, draws):
    if k > successes or k > draws:
        return 0.0
    numerator = comb(successes, k) * comb(population - successes, draws - k)
    denominator = comb(population, draws)
    if denominator == 0:
        return 0.0
    return numerator / denominator


def normal_pdf(x, mu=0.0, sigma=1.0):
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    coeff = 1.0 / (sigma * sqrt(2 * PI))
    exponent = -((x - mu) ** 2) / (2 * sigma * sigma)
    return coeff * exp(exponent)


def normal_cdf(x, mu=0.0, sigma=1.0):
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    z = (x - mu) / (sigma * sqrt(2))
    return 0.5 * (1 + erf(z))


def standard_normal_pdf(x):
    return normal_pdf(x, 0.0, 1.0)


def standard_normal_cdf(x):
    return normal_cdf(x, 0.0, 1.0)


def exponential_pdf(x, rate):
    if x < 0:
        return 0.0
    return rate * exp(-rate * x)


def exponential_cdf(x, rate):
    if x < 0:
        return 0.0
    return 1 - exp(-rate * x)


def uniform_pdf(x, a, b):
    if x < a or x > b:
        return 0.0
    return 1.0 / (b - a)


def uniform_cdf(x, a, b):
    if x < a:
        return 0.0
    if x > b:
        return 1.0
    return (x - a) / (b - a)


def bernoulli_pmf(k, p):
    if k == 1:
        return p
    if k == 0:
        return 1 - p
    return 0.0


def expected_value(values, probabilities):
    if len(values) != len(probabilities):
        raise ValueError("values and probabilities must have the same length")
    return sum(v * p for v, p in zip(values, probabilities))


def variance_discrete(values, probabilities):
    mu = expected_value(values, probabilities)
    return sum(p * (v - mu) ** 2 for v, p in zip(values, probabilities))


def combinations_probability(total_ways, favorable_ways):
    if total_ways == 0:
        raise ValueError("total_ways must not be zero")
    return favorable_ways / total_ways


def odds_to_probability(odds_for, odds_against):
    return odds_for / (odds_for + odds_against)


def probability_to_odds(p):
    if p >= 1:
        raise ValueError("probability must be less than 1")
    return p / (1 - p)


def bayes_theorem(p_b_given_a, p_a, p_b):
    if p_b == 0:
        raise ValueError("p_b must not be zero")
    return (p_b_given_a * p_a) / p_b


def union_probability(p_a, p_b, p_a_and_b):
    return p_a + p_b - p_a_and_b


def conditional_probability(p_a_and_b, p_b):
    if p_b == 0:
        raise ValueError("p_b must not be zero")
    return p_a_and_b / p_b
