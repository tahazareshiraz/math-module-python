# taha_math_shiraz Documentation

> This page is the main reference for the library. It explains each module with descriptions, examples, outputs, and practical notes, so it can be used both as a quick overview and as a detailed developer reference.

**Note:** This package is an educational/general-purpose toolkit for mathematics, numerical methods, graphs, simple cryptography, and helper utilities.

## Table of Contents

- [Overview](#overview)
- [Constants](#constants)
- [Basic Functions](#basic-functions)
- [Number Theory Core](#number-theory-core)
- [Powers, Roots and Logs](#powers-roots-and-logs)
- [Trigonometry and Hyperbolic Functions](#trigonometry-and-hyperbolic-functions)
- [Aggregates and Combinatorics](#aggregates-and-combinatorics)
- [Special Functions](#special-functions)
- [Advanced Number Theory](#advanced-number-theory)
- [Statistics](#statistics)
- [Probability](#probability)
- [Linear Algebra](#linear-algebra)
- [Geometry](#geometry)
- [Numerical Calculus](#numerical-calculus)
- [Unit Conversions](#unit-conversions)
- [Interpolation](#interpolation)
- [Pseudo-Random Utilities](#pseudo-random-utilities)
- [Base Conversion and Roman Numerals](#base-conversion-and-roman-numerals)
- [Series](#series)
- [Activation Functions](#activation-functions)
- [Metrics](#metrics)
- [Polynomials](#polynomials)
- [Custom Data Types](#custom-data-types)
- [Educational Cryptography](#educational-cryptography)
- [Graph](#graph)
- [Algorithms](#algorithms)
- [Usage and Summary](#usage-and-summary)

---

## Overview

The `__init__.py` file re-exports the public API so you can use the package directly from the root namespace.

```python
import taha_math_shiraz as tms

print(tms.PI)
print(tms.sqrt(2))
print(tms.Graph())
```

---

## Constants

**File:** `constants.py`

> This section contains the core constants used across the package. They are the numeric foundation for trigonometric, logarithmic, and numerical routines.

- **`PI`** — The constant pi with high precision
  ```python
  print(tms.PI)
  ```
  Output: `3.141592653589793`

- **`TAU`** — Two times PI
  ```python
  print(tms.TAU)
  ```
  Output: `6.283185307179586`

- **`E`** — Euler's number
  ```python
  print(tms.E)
  ```
  Output: `2.718281828459045`

- **`INF`** — Positive infinity
  ```python
  print(tms.INF)
  ```
  Output: `inf`

- **`NAN`** — Not-a-Number value
  ```python
  print(tms.NAN)
  ```
  Output: `nan`

- **`SQRT2`** — Square root of 2

- **`LN2`** — Natural logarithm of 2

- **`LN10`** — Natural logarithm of 10

---

## Basic Functions

**File:** `basics.py`

> These are lightweight, self-contained equivalents for basic numeric operations such as checking values, truncation, rounding, and floating-point remainder handling.

- **`isnan(x)`** — Checks whether x is NaN
  ```python
  result = tms.isnan(float("nan"))
  print(result)
  ```
  Output: `True`

- **`isinf(x)`** — Checks whether x is infinite
  ```python
  result = tms.isinf(float("inf"))
  print(result)
  ```
  Output: `True`

- **`isfinite(x)`** — Checks whether x is finite
  ```python
  result = tms.isfinite(3.5)
  print(result)
  ```
  Output: `True`

- **`copysign(x, y)`** — Returns x with the sign of y

- **`fabs(x)`** — Absolute value
  ```python
  result = tms.fabs(-7.25)
  print(result)
  ```
  Output: `7.25`

- **`trunc(x)`** — Truncates toward zero
  ```python
  result = tms.trunc(3.9)
  print(result)
  ```
  Output: `3`

- **`floor(x)`** — Floor
  ```python
  result = tms.floor(3.9)
  print(result)
  ```
  Output: `3`

- **`ceil(x)`** — Ceiling
  ```python
  result = tms.ceil(3.1)
  print(result)
  ```
  Output: `4`

- **`fmod(x, y)`** — Floating-point remainder

- **`remainder(x, y)`** — Remainder based on rounding

- **`modf(x)`** — Splits into fractional and integer parts
  ```python
  result = tms.modf(3.75)
  print(result)
  ```
  Output: `(0.75, 3.0)`

---

## Number Theory Core

**File:** `numtheory_core.py`

> This module provides the minimal number-theory building blocks used by many other parts of the library, including factorial, gcd, lcm, and integer square root.

- **`factorial(n)`** — Factorial
  ```python
  print(tms.factorial(5))
  ```
  Output: `120`

- **`gcd(*args)`** — Greatest common divisor
  ```python
  print(tms.gcd(12, 18))
  ```
  Output: `6`

- **`lcm(*args)`** — Least common multiple
  ```python
  print(tms.lcm(4, 6))
  ```
  Output: `12`

- **`isqrt(n)`** — Integer square root
  ```python
  print(tms.isqrt(17))
  ```
  Output: `4`

---

## Powers, Roots and Logs

**File:** `power.py`

> This is the numerical core of the library. It provides square root, exponentiation, and logarithms without relying on Python’s math module.

- **`sqrt(x)`** — Approximate square root
  ```python
  print(round(tms.sqrt(9), 1))
  ```
  Output: `3.0`

- **`cbrt(x)`** — Approximate cube root
  ```python
  print(round(tms.cbrt(27), 1))
  ```
  Output: `3.0`

- **`pow_(x, y)`** — General exponentiation
  ```python
  print(tms.pow_(2, 5))
  ```
  Output: `32.0`

- **`exp(x)`** — Exponential function
  ```python
  print(round(tms.exp(1), 6))
  ```
  Output: `2.718282`

- **`expm1(x)`** — exp(x) - 1
  ```python
  result = tms.expm1(1)
  print(result)
  ```
  Output: `1.7182818284590438`

- **`log1p(x)`** — log(1+x)
  ```python
  result = tms.log1p(1)
  print(result)
  ```
  Output: `0.6931471805599454`

- **`log(x, base=None)`** — Natural log or log with base
  ```python
  print(round(tms.log(tms.E), 6))
  ```
  Output: `1.0`

- **`log2(x)`** — Base-2 logarithm
  ```python
  result = tms.log2(8)
  print(result)
  ```
  Output: `3.0000000000000004`

- **`log10(x)`** — Base-10 logarithm
  ```python
  result = tms.log10(1000)
  print(result)
  ```
  Output: `2.9999999999999996`

---

## Trigonometry and Hyperbolic Functions

**File:** `trigonometry.py`

> All main trigonometric and hyperbolic functions live here. The implementations are based on manual approximations and series expansions to keep the package independent.

- **`degrees(x)`** — Convert radians to degrees
  ```python
  print(tms.degrees(tms.PI))
  ```
  Output: `180.0`

- **`radians(x)`** — Convert degrees to radians
  ```python
  print(round(tms.radians(180), 6))
  ```
  Output: `3.141593`

- **`sin(x)`** — Sine
  ```python
  print(round(tms.sin(tms.PI / 2), 6))
  ```
  Output: `1.0`

- **`cos(x)`** — Cosine
  ```python
  print(round(tms.cos(0), 6))
  ```
  Output: `1.0`

- **`tan(x)`** — Tangent
  ```python
  print(round(tms.tan(tms.PI / 4), 6))
  ```
  Output: `1.0`

- **`sinh(x)`** — Hyperbolic sine
  ```python
  result = tms.sinh(1)
  print(result)
  ```
  Output: `1.1752011936438007`

- **`cosh(x)`** — Hyperbolic cosine
  ```python
  result = tms.cosh(1)
  print(result)
  ```
  Output: `1.543080634815243`

- **`tanh(x)`** — Hyperbolic tangent
  ```python
  result = tms.tanh(1)
  print(result)
  ```
  Output: `0.7615941559557647`

- **`asinh(x)`** — Inverse hyperbolic sine
  ```python
  result = tms.asinh(1)
  print(result)
  ```
  Output: `0.8813735870195429`

- **`acosh(x)`** — Inverse hyperbolic cosine
  ```python
  result = tms.acosh(2)
  print(result)
  ```
  Output: `1.3169578969248168`

- **`atanh(x)`** — Inverse hyperbolic tangent
  ```python
  result = tms.atanh(0.5)
  print(result)
  ```
  Output: `0.5493061443340549`

- **`asin(x)`** — Inverse sine
  ```python
  result = tms.asin(0.5)
  print(result)
  ```
  Output: `0.5235987755982988`

- **`acos(x)`** — Inverse cosine
  ```python
  result = tms.acos(0.5)
  print(result)
  ```
  Output: `1.0471975511965979`

- **`atan(x)`** — Inverse tangent
  ```python
  result = tms.atan(1)
  print(result)
  ```
  Output: `0.7853981633974483`

- **`atan2(y, x)`** — Angle with quadrant awareness

- **`hypot(*coords)`** — Vector length

- **`dist(p, q)`** — Euclidean distance

---

## Aggregates and Combinatorics

**File:** `aggregates.py`

> This module groups together summation, product, combination, and permutation helpers that are heavily reused by statistics, probability, and number theory.

- **`fsum(iterable)`** — More accurate summation
  ```python
  result = tms.fsum([1, 2, 3, 4])
  print(result)
  ```
  Output: `10.0`

- **`prod(iterable, start=1)`** — Product
  ```python
  result = tms.prod([2, 3, 4], 2)
  print(result)
  ```
  Output: `48`

- **`isclose(a, b, rel_tol, abs_tol)`** — Approximate comparison
  ```python
  result = tms.isclose(1.0, 1.0000001, 1e-5, 1e-8)
  print(result)
  ```
  Output: `True`

- **`comb(n, k)`** — Combinations
  ```python
  print(tms.comb(5, 2))
  ```
  Output: `10`

- **`perm(n, k=None)`** — Permutations
  ```python
  print(tms.perm(5, 2))
  ```
  Output: `20`

---

## Special Functions

**File:** `special.py`

> Special functions such as gamma, erf, and floating-point helpers are placed here. They are useful for advanced numerical work and floating-point analysis.

- **`lgamma(x)`** — Log-gamma
  ```python
  result = tms.lgamma(3)
  print(result)
  ```
  Output: `0.6931471805599463`

- **`gamma(x)`** — Gamma function
  ```python
  result = tms.gamma(4)
  print(result)
  ```
  Output: `6.0`

- **`erf(x)`** — Error function
  ```python
  result = tms.erf(1)
  print(result)
  ```
  Output: `0.84270068974759`

- **`erfc(x)`** — Complementary error function
  ```python
  result = tms.erfc(1)
  print(result)
  ```
  Output: `0.15729931025240995`

- **`frexp(x)`** — Mantissa and exponent
  ```python
  result = tms.frexp(8)
  print(result)
  ```
  Output: `(0.5, 4)`

- **`ldexp(m, e)`** — Combine mantissa and exponent

- **`nextafter(x, y)`** — Next representable float toward y

- **`ulp(x)`** — Unit in the last place
  ```python
  result = tms.ulp(1.0)
  print(result)
  ```
  Output: `2.220446049250313e-16`

- **`signbit(x)`** — Sign bit
  ```python
  result = tms.signbit(-2)
  print(result)
  ```
  Output: `True`

---

## Advanced Number Theory

**File:** `numbertheory.py`

> This is the largest number-theory toolkit in the package. It includes primality, factorization, modular arithmetic, sequences, polygonal numbers, and CRT utilities.

- **`is_prime(n)`** — Prime test
  ```python
  print(tms.is_prime(97))
  ```
  Output: `True`

- **`next_prime(n)`** — Next prime
  ```python
  result = tms.next_prime(29)
  print(result)
  ```
  Output: `31`

- **`prev_prime(n)`** — Previous prime
  ```python
  result = tms.prev_prime(29)
  print(result)
  ```
  Output: `23`

- **`prime_factors(n)`** — Prime factor list
  ```python
  result = tms.prime_factors(84)
  print(result)
  ```
  Output: `[2, 2, 3, 7]`

- **`prime_factorization(n)`** — Prime factor dictionary
  ```python
  result = tms.prime_factorization(84)
  print(result)
  ```
  Output: `{2: 2, 3: 1, 7: 1}`

- **`divisors(n)`** — Divisors
  ```python
  result = tms.divisors(12)
  print(result)
  ```
  Output: `[1, 2, 3, 4, 6, 12]`

- **`divisor_count(n)`** — Number of divisors
  ```python
  result = tms.divisor_count(12)
  print(result)
  ```
  Output: `6`

- **`divisor_sum(n)`** — Sum of divisors
  ```python
  result = tms.divisor_sum(12)
  print(result)
  ```
  Output: `28`

- **`is_perfect(n)`** — Perfect number test
  ```python
  result = tms.is_perfect(28)
  print(result)
  ```
  Output: `True`

- **`is_abundant(n)`** — Abundant number test
  ```python
  result = tms.is_abundant(12)
  print(result)
  ```
  Output: `True`

- **`is_deficient(n)`** — Deficient number test
  ```python
  result = tms.is_deficient(8)
  print(result)
  ```
  Output: `True`

- **`euler_totient(n)`** — Euler's totient function
  ```python
  result = tms.euler_totient(10)
  print(result)
  ```
  Output: `4`

- **`mobius(n)`** — Mobius function
  ```python
  result = tms.mobius(30)
  print(result)
  ```
  Output: `-1`

- **`fibonacci(n)`** — Fibonacci number
  ```python
  print(tms.fibonacci(10))
  ```
  Output: `55`

- **`lucas(n)`** — Lucas number
  ```python
  result = tms.lucas(10)
  print(result)
  ```
  Output: `123`

- **`tribonacci(n)`** — Tribonacci number
  ```python
  result = tms.tribonacci(10)
  print(result)
  ```
  Output: `274`

- **`catalan(n)`** — Catalan number
  ```python
  result = tms.catalan(5)
  print(result)
  ```
  Output: `42`

- **`bernoulli(n)`** — Bernoulli number
  ```python
  result = tms.bernoulli(4)
  print(result)
  ```
  Output: `-0.03333333333333399`

- **`harmonic(n)`** — Harmonic number
  ```python
  result = tms.harmonic(5)
  print(result)
  ```
  Output: `2.283333333333333`

- **`digit_sum(n)`** — Sum of digits
  ```python
  result = tms.digit_sum(12345)
  print(result)
  ```
  Output: `15`

- **`digit_product(n)`** — Product of digits
  ```python
  result = tms.digit_product(1234)
  print(result)
  ```
  Output: `24`

- **`digital_root(n)`** — Digital root
  ```python
  result = tms.digital_root(9876)
  print(result)
  ```
  Output: `3`

- **`is_palindrome_number(n)`** — Palindrome number test
  ```python
  result = tms.is_palindrome_number(12321)
  print(result)
  ```
  Output: `True`

- **`is_armstrong(n)`** — Armstrong number test
  ```python
  result = tms.is_armstrong(153)
  print(result)
  ```
  Output: `True`

- **`collatz_length(n)`** — Collatz sequence length
  ```python
  result = tms.collatz_length(13)
  print(result)
  ```
  Output: `9`

- **`is_power_of_two(n)`** — Power-of-two test
  ```python
  result = tms.is_power_of_two(16)
  print(result)
  ```
  Output: `True`

- **`bit_length(n)`** — Binary length
  ```python
  result = tms.bit_length(255)
  print(result)
  ```
  Output: `8`

- **`popcount(n)`** — Number of set bits
  ```python
  result = tms.popcount(255)
  print(result)
  ```
  Output: `8`

- **`extended_gcd(a, b)`** — Extended Euclidean algorithm

- **`mod_inverse(a, m)`** — Modular inverse

- **`mod_pow(base, exp, mod)`** — Fast modular exponentiation

- **`chinese_remainder(remainders, moduli)`** — Chinese remainder theorem

- **`is_coprime(a, b)`** — Coprime test

- **`jacobi_symbol(a, n)`** — Jacobi symbol

- **`sieve_of_eratosthenes(limit)`** — Sieve of Eratosthenes
  ```python
  result = tms.sieve_of_eratosthenes(30)
  print(result)
  ```
  Output: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`

- **`count_primes_below(limit)`** — Count primes below limit
  ```python
  result = tms.count_primes_below(30)
  print(result)
  ```
  Output: `10`

- **`goldbach_pair(n)`** — Goldbach pair
  ```python
  result = tms.goldbach_pair(28)
  print(result)
  ```
  Output: `(5, 23)`

- **`is_amicable_pair(a, b)`** — Amicable pair test

- **`find_amicable_pairs(limit)`** — Find amicable pairs
  ```python
  result = tms.find_amicable_pairs(1000)
  print(result)
  ```
  Output: `[(220, 284)]`

- **`polygonal_number(s, n)`** — General polygonal number

- **`triangular_number(n)`** — Triangular number
  ```python
  result = tms.triangular_number(7)
  print(result)
  ```
  Output: `28`

- **`square_number(n)`** — Square number
  ```python
  result = tms.square_number(7)
  print(result)
  ```
  Output: `49`

- **`pentagonal_number(n)`** — Pentagonal number
  ```python
  result = tms.pentagonal_number(4)
  print(result)
  ```
  Output: `22`

- **`hexagonal_number(n)`** — Hexagonal number
  ```python
  result = tms.hexagonal_number(4)
  print(result)
  ```
  Output: `28`

- **`heptagonal_number(n)`** — Heptagonal number
  ```python
  result = tms.heptagonal_number(4)
  print(result)
  ```
  Output: `34`

- **`octagonal_number(n)`** — Octagonal number
  ```python
  result = tms.octagonal_number(4)
  print(result)
  ```
  Output: `40`

- **`is_triangular(n)`** — Triangular test
  ```python
  result = tms.is_triangular(15)
  print(result)
  ```
  Output: `True`

- **`is_square(n)`** — Square test
  ```python
  result = tms.is_square(16)
  print(result)
  ```
  Output: `True`

- **`is_pentagonal(n)`** — Pentagonal test
  ```python
  result = tms.is_pentagonal(12)
  print(result)
  ```
  Output: `True`

- **`pascal_triangle_row(n)`** — Row of Pascal's triangle
  ```python
  result = tms.pascal_triangle_row(5)
  print(result)
  ```
  Output: `[1, 5, 10, 10, 5, 1]`

- **`pascal_triangle(rows)`** — Pascal's triangle
  ```python
  result = tms.pascal_triangle(5)
  print(result)
  ```
  Output: `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`

- **`sum_of_squares(n)`** — Sum of squares
  ```python
  result = tms.sum_of_squares(5)
  print(result)
  ```
  Output: `55`

- **`sum_of_cubes(n)`** — Sum of cubes
  ```python
  result = tms.sum_of_cubes(5)
  print(result)
  ```
  Output: `225`

- **`is_perfect_square_fast(n)`** — Fast perfect-square test
  ```python
  result = tms.is_perfect_square_fast(144)
  print(result)
  ```
  Output: `True`

---

## Statistics

**File:** `statistics_mod.py`

> This module covers descriptive and light inferential statistics, including averages, spread measures, correlation, and linear regression.

- **`mean(data)`** — Arithmetic mean
  ```python
  print(tms.mean([1, 2, 3, 4]))
  ```
  Output: `2.5`

- **`geometric_mean(data)`** — Geometric mean
  ```python
  result = tms.geometric_mean([1, 2, 4, 8])
  print(result)
  ```
  Output: `2.8284271247461876`

- **`harmonic_mean(data)`** — Harmonic mean
  ```python
  result = tms.harmonic_mean([1, 2, 4])
  print(result)
  ```
  Output: `1.7142857142857142`

- **`median(data)`** — Median
  ```python
  print(tms.median([1, 3, 2]))
  ```
  Output: `2.0`

- **`median_low(data)`** — Lower median
  ```python
  result = tms.median_low([1, 3, 2, 4])
  print(result)
  ```
  Output: `2`

- **`median_high(data)`** — Upper median
  ```python
  result = tms.median_high([1, 3, 2, 4])
  print(result)
  ```
  Output: `3`

- **`mode(data)`** — Mode
  ```python
  print(tms.mode([1, 2, 2, 3]))
  ```
  Output: `2`

- **`multimode(data)`** — Multiple modes
  ```python
  result = tms.multimode([1, 1, 2, 2, 3])
  print(result)
  ```
  Output: `[1, 2]`

- **`variance(data, xbar=None)`** — Sample variance
  ```python
  print(round(tms.variance([1, 2, 3, 4]), 6))
  ```
  Output: `1.666667`

- **`pvariance(data, mu=None)`** — Population variance
  ```python
  result = tms.pvariance([1, 2, 3, 4])
  print(result)
  ```
  Output: `1.25`

- **`stdev(data, xbar=None)`** — Sample standard deviation
  ```python
  print(round(tms.stdev([1, 2, 3, 4]), 6))
  ```
  Output: `1.290994`

- **`pstdev(data, mu=None)`** — Population standard deviation
  ```python
  result = tms.pstdev([1, 2, 3, 4])
  print(result)
  ```
  Output: `1.118033988749895`

- **`covariance(x, y)`** — Covariance

- **`correlation(x, y)`** — Correlation

- **`linear_regression(x, y)`** — Linear regression

- **`quantiles(data, n=4)`** — Quantiles
  ```python
  result = tms.quantiles([1, 2, 3, 4, 5, 6, 7, 8])
  print(result)
  ```
  Output: `[2.75, 4.5, 6.25]`

- **`z_score(x, data)`** — Z-score

- **`range_(data)`** — Range
  ```python
  result = tms.range_([1, 9, 4, 2])
  print(result)
  ```
  Output: `8`

- **`midrange(data)`** — Midrange
  ```python
  result = tms.midrange([1, 9, 4, 2])
  print(result)
  ```
  Output: `5.0`

- **`skewness(data)`** — Skewness
  ```python
  result = tms.skewness([1, 2, 3, 4, 5])
  print(result)
  ```
  Output: `0.0`

- **`kurtosis(data)`** — Kurtosis
  ```python
  result = tms.kurtosis([1, 2, 3, 4, 5])
  print(result)
  ```
  Output: `-1.2999999999999996`

---

## Probability

**File:** `probability.py`

> Basic distributions and probability helpers are provided here for educational examples and simple stochastic calculations.

- **`binomial_probability(n, k, p)`** — Binomial probability

- **`poisson_probability(lam, k)`** — Poisson probability

- **`normal_pdf(x, mu=0.0, sigma=1.0)`** — Normal PDF
  ```python
  result = tms.normal_pdf(0)
  print(result)
  ```
  Output: `0.39894228040143265`

- **`normal_cdf(x, mu=0.0, sigma=1.0)`** — Normal CDF
  ```python
  result = tms.normal_cdf(0)
  print(result)
  ```
  Output: `0.5000000005`

- **`exponential_pdf(x, lam)`** — Exponential PDF

- **`exponential_cdf(x, lam)`** — Exponential CDF

- **`uniform_pdf(x, a, b)`** — Uniform PDF

- **`uniform_cdf(x, a, b)`** — Uniform CDF

- **`geometric_pdf(k, p)`** — Geometric probability

- **`binomial_mean(n, p)`** — Binomial mean

- **`binomial_variance(n, p)`** — Binomial variance

---

## Linear Algebra

**File:** `linalg.py`

> Vectors, matrices, and complex numbers are implemented here together with several geometric and linear-algebra helpers.

- **`Vector(components)`** — Vector class
  ```python
  v = tms.Vector([3, 4])\nprint(v.norm())
  ```
  Output: `5.0`

- **`Matrix(rows)`** — Matrix class
  ```python
  m = tms.Matrix([[1, 2], [3, 4]])\nprint(m.determinant())
  ```
  Output: `-2`

- **`Complex(real, imag=0.0)`** — Complex number class
  ```python
  z = tms.Complex(3, 4)\nprint(z.modulus())
  ```
  Output: `5.0`

- **`vector_projection(a, b)`** — Vector projection

- **`vector_reflection(v, normal)`** — Vector reflection

- **`matrix_power(m, n)`** — Matrix power

- **`matrix_from_function(rows, cols, f)`** — Matrix from function

- **`rotation_matrix_2d(theta)`** — 2D rotation matrix
  ```python
  result = tms.rotation_matrix_2d(tms.PI / 2)
  print(result)
  ```
  Output: `Matrix([[4.5907218229751464e-17, -1.0000000000000002], [1.0000000000000002, 4.5907218229751464e-17]])`

- **`rotation_matrix_x(theta)`** — Rotation about x
  ```python
  result = tms.rotation_matrix_x(tms.PI / 2)
  print(result)
  ```
  Output: `Matrix([[1, 0, 0], [0, 4.5907218229751464e-17, -1.0000000000000002], [0, 1.0000000000000002, 4.5907218229751464e-17]])`

- **`rotation_matrix_y(theta)`** — Rotation about y
  ```python
  result = tms.rotation_matrix_y(tms.PI / 2)
  print(result)
  ```
  Output: `Matrix([[4.5907218229751464e-17, 0, 1.0000000000000002], [0, 1, 0], [-1.0000000000000002, 0, 4.5907218229751464e-17]])`

- **`rotation_matrix_z(theta)`** — Rotation about z
  ```python
  result = tms.rotation_matrix_z(tms.PI / 2)
  print(result)
  ```
  Output: `Matrix([[4.5907218229751464e-17, -1.0000000000000002, 0], [1.0000000000000002, 4.5907218229751464e-17, 0], [0, 0, 1]])`

- **`scaling_matrix(sx, sy)`** — Scaling matrix

- **`translation_apply(point, dx, dy)`** — Apply translation

---

## Geometry

**File:** `geometry.py`

> Classic geometry formulas, distances, areas, volumes, and relations like the law of sines/cosines are included in this section.

- **`distance_2d(p1, p2)`** — Distance in 2D

- **`distance_3d(p1, p2)`** — Distance in 3D

- **`triangle_area(a, b, c)`** — Triangle area from sides

- **`triangle_area_coords(p1, p2, p3)`** — Triangle area from coordinates

- **`circle_area(r)`** — Circle area
  ```python
  result = tms.circle_area(3)
  print(result)
  ```
  Output: `28.274333882308138`

- **`circle_circumference(r)`** — Circle circumference
  ```python
  result = tms.circle_circumference(3)
  print(result)
  ```
  Output: `18.84955592153876`

- **`sphere_volume(r)`** — Sphere volume
  ```python
  result = tms.sphere_volume(3)
  print(result)
  ```
  Output: `113.09733552923254`

- **`sphere_surface_area(r)`** — Sphere surface area
  ```python
  result = tms.sphere_surface_area(3)
  print(result)
  ```
  Output: `113.09733552923255`

- **`cylinder_volume(r, h)`** — Cylinder volume

- **`cylinder_surface_area(r, h)`** — Cylinder surface area

- **`cone_volume(r, h)`** — Cone volume

- **`cone_surface_area(r, h)`** — Cone surface area

- **`regular_polygon_area(n, side)`** — Regular polygon area

- **`regular_polygon_perimeter(n, side)`** — Regular polygon perimeter

- **`law_of_cosines(a, b, gamma_angle)`** — Law of cosines

- **`law_of_sines_ratio(a, angle_a)`** — Law of sines ratio

- **`heron_perimeter(a, b, c)`** — Sum of triangle sides

- **`polygon_area_shoelace(points)`** — Shoelace formula
  ```python
  result = tms.polygon_area_shoelace([(0, 0), (4, 0), (4, 3)])
  print(result)
  ```
  Output: `6.0`

- **`centroid(points)`** — Centroid
  ```python
  result = tms.centroid([(0, 0), (4, 0), (4, 3)])
  print(result)
  ```
  Output: `(2.6666666666666665, 1.0)`

- **`is_collinear(p1, p2, p3)`** — Collinearity test

- **`midpoint(p1, p2)`** — Midpoint

- **`slope(p1, p2)`** — Slope

- **`line_intersection(p1, p2, p3, p4)`** — Line intersection

- **`point_in_circle(p, center, r)`** — Point in circle

- **`point_in_triangle(p, a, b, c)`** — Point in triangle

---

## Numerical Calculus

**File:** `calculus.py`

> This module provides numerical differentiation, integration, and root-finding methods for approximate calculus work.

- **`derivative(f, x, h=1e-6)`** — Numerical derivative

- **`second_derivative(f, x, h=1e-4)`** — Second numerical derivative

- **`integral_trapezoid(f, a, b, n=1000)`** — Trapezoidal integration

- **`integral_simpson(f, a, b, n=1000)`** — Simpson integration

- **`newton_raphson(f, fprime, x0, tol, max_iter)`** — Newton-Raphson root finding

- **`bisection_method(f, a, b, tol, max_iter)`** — Bisection method

- **`taylor_series_exp(x, terms=20)`** — Taylor approximation of e^x
  ```python
  result = tms.taylor_series_exp(1)
  print(result)
  ```
  Output: `2.7182818284590455`

- **`secant_method(f, x0, x1, tol, max_iter)`** — Secant method

- **`golden_section_search(f, a, b, tol)`** — Golden-section search

---

## Unit Conversions

**File:** `conversions.py`

> Common unit conversions for temperature, distance, mass, and angle are grouped here.

- **`convert_celsius_to_fahrenheit(c)`** — Celsius to Fahrenheit
  ```python
  result = tms.convert_celsius_to_fahrenheit(0)
  print(result)
  ```
  Output: `32.0`

- **`convert_fahrenheit_to_celsius(f)`** — Fahrenheit to Celsius
  ```python
  result = tms.convert_fahrenheit_to_celsius(32)
  print(result)
  ```
  Output: `0.0`

- **`convert_celsius_to_kelvin(c)`** — Celsius to Kelvin
  ```python
  result = tms.convert_celsius_to_kelvin(0)
  print(result)
  ```
  Output: `273.15`

- **`convert_kelvin_to_celsius(k)`** — Kelvin to Celsius
  ```python
  result = tms.convert_kelvin_to_celsius(273.15)
  print(result)
  ```
  Output: `0.0`

- **`convert_km_to_miles(km)`** — Kilometers to miles
  ```python
  result = tms.convert_km_to_miles(1)
  print(result)
  ```
  Output: `0.621371`

- **`convert_miles_to_km(miles)`** — Miles to kilometers
  ```python
  result = tms.convert_miles_to_km(1)
  print(result)
  ```
  Output: `1.6093444978925633`

- **`convert_kg_to_pounds(kg)`** — Kilograms to pounds
  ```python
  result = tms.convert_kg_to_pounds(1)
  print(result)
  ```
  Output: `2.20462`

- **`convert_pounds_to_kg(lb)`** — Pounds to kilograms
  ```python
  result = tms.convert_pounds_to_kg(1)
  print(result)
  ```
  Output: `0.45359290943563974`

- **`convert_degrees_to_radians(d)`** — Degrees to radians

- **`convert_radians_to_degrees(r)`** — Radians to degrees

---

## Interpolation

**File:** `interpolation.py`

> Lagrange interpolation, Newton divided differences, continued fractions, and related number transformations are included here.

- **`lagrange_interpolation(points, x)`** — Lagrange interpolation

- **`newton_divided_difference(points, x)`** — Newton divided differences

- **`linear_interpolation(x0, y0, x1, y1, x)`** — Linear interpolation

- **`bilinear_interpolation(...)`** — Bilinear interpolation

- **`continued_fraction(x, depth=15)`** — Continued fraction
  ```python
  result = tms.continued_fraction(3.245)
  print(result)
  ```
  Output: `[3, 4, 12, 3, 1, 247777268231, 4, 1, 2, 1, 2, 1, 34, 1, 3]`

- **`convergent_from_continued_fraction(terms)`** — Convergent from continued fraction
  ```python
  result = tms.convergent_from_continued_fraction([1, 2, 2])
  print(result)
  ```
  Output: `(7, 5)`

- **`egyptian_fraction(numerator, denominator)`** — Egyptian fraction

---

## Pseudo-Random Utilities

**File:** `randomutil.py`

> A simple linear congruential generator and sequence helper are provided in this module.

- **`lcg_random(seed, a=1103515245, c=12345, m=2 ** 31)`** — One LCG step
  ```python
  result = tms.lcg_random(2, 2, 2, 2)
  print(result)
  ```
  Output: `0`

- **`lcg_sequence(seed, n, a=1103515245, c=12345, m=2 ** 31)`** — LCG sequence
  ```python
  result = tms.lcg_sequence(2, 2, 2, 2, 2)
  print(result)
  ```
  Output: `[0, 0]`

---

## Base Conversion and Roman Numerals

**File:** `baseconv.py`

> This module handles conversions between numeric bases and Roman numeral formatting/parsing.

- **`to_base(n, base)`** — Convert integer to another base
  ```python
  result = tms.to_base(2, 2)
  print(result)
  ```
  Output: `'10'`

- **`from_base(s, base)`** — Convert from another base

- **`roman_to_int(s)`** — Roman numeral to integer

- **`int_to_roman(n)`** — Integer to Roman numeral
  ```python
  result = tms.int_to_roman(2)
  print(result)
  ```
  Output: `'II'`

---

## Series

**File:** `series.py`

> Arithmetic and geometric series formulas, including the convergent infinite geometric form, live here.

- **`arithmetic_series_sum(a1, d, n)`** — Arithmetic series sum
  ```python
  result = tms.arithmetic_series_sum(2, 2, 2)
  print(result)
  ```
  Output: `6.0`

- **`geometric_series_sum(a1, r, n)`** — Finite geometric series sum
  ```python
  result = tms.geometric_series_sum(2, 2, 2)
  print(result)
  ```
  Output: `6.0`

- **`infinite_geometric_series_sum(a1, r)`** — Infinite geometric series sum

---

## Activation Functions

**File:** `activations.py`

> Useful activation and interpolation-style functions such as ReLU, sigmoid, and smoothstep are provided here.

- **`lerp(a, b, t)`** — Linear interpolation
  ```python
  result = tms.lerp(2, 2, 2)
  print(result)
  ```
  Output: `2`

- **`clamp(x, lo, hi)`** — Clamp value
  ```python
  result = tms.clamp(2, 2, 2)
  print(result)
  ```
  Output: `2`

- **`smoothstep(edge0, edge1, x)`** — Smoothstep

- **`sign(x)`** — Sign
  ```python
  result = tms.sign(2)
  print(result)
  ```
  Output: `1`

- **`relu(x)`** — ReLU
  ```python
  result = tms.relu(2)
  print(result)
  ```
  Output: `2`

- **`sigmoid(x)`** — Sigmoid
  ```python
  result = tms.sigmoid(2)
  print(result)
  ```
  Output: `0.8807970779778825`

- **`softplus(x)`** — Softplus
  ```python
  result = tms.softplus(2)
  print(result)
  ```
  Output: `2.1269280110429714`

- **`tanh_derivative(x)`** — Derivative of tanh
  ```python
  result = tms.tanh_derivative(2)
  print(result)
  ```
  Output: `0.07065082485316443`

- **`sigmoid_derivative(x)`** — Derivative of sigmoid
  ```python
  result = tms.sigmoid_derivative(2)
  print(result)
  ```
  Output: `0.10499358540350645`

---

## Metrics

**File:** `metrics.py`

> Distance metrics and cosine similarity helpers are grouped in this module.

- **`euclidean_norm(v)`** — Euclidean norm

- **`manhattan_distance(p1, p2)`** — Manhattan distance

- **`chebyshev_distance(p1, p2)`** — Chebyshev distance

- **`minkowski_distance(p1, p2, p)`** — Minkowski distance

- **`cosine_similarity(a, b)`** — Cosine similarity

---

## Polynomials

**File:** `polynomial.py`

> This is a major module for polynomial arithmetic, root finding, named orthogonal polynomials, and symbolic-style manipulations.

- **`poly_eval(coeffs, x)`** — Evaluate polynomial
  ```python
  print(tms.poly_eval([1, 0, -1], 3))
  ```
  Output: `8.0`

- **`poly_add(a, b)`** — Add polynomials
  ```python
  print(tms.poly_add([1, 2], [3, 4]))
  ```
  Output: `[4, 6]`

- **`poly_sub(a, b)`** — Subtract polynomials

- **`poly_mul(a, b)`** — Multiply polynomials
  ```python
  print(tms.poly_mul([1, 1], [1, -1]))
  ```
  Output: `[1, 0, -1]`

- **`poly_scale(a, s)`** — Scale polynomial

- **`poly_neg(a)`** — Negate polynomial

- **`poly_divmod(a, b)`** — Polynomial long division

- **`poly_div(a, b)`** — Quotient

- **`poly_mod(a, b)`** — Remainder

- **`poly_gcd(a, b)`** — Polynomial gcd

- **`poly_differentiate(coeffs)`** — Derivative

- **`poly_integrate(coeffs, c=0.0)`** — Indefinite integral

- **`poly_roots_quadratic(a, b, c)`** — Quadratic roots

- **`poly_roots_cubic(a, b, c, d)`** — Cubic roots
  ```python
  result = tms.poly_roots_cubic(2, 2, 2, 2)
  print(result)
  ```
  Output: `(-0.9999999999999998, (-5.551115123125783e-17, 1.0), (-5.551115123125783e-17, -1.0))`

- **`poly_companion_matrix(coeffs)`** — Companion matrix

- **`poly_compose(f, g)`** — Polynomial composition

- **`poly_from_roots(roots)`** — Build from roots

- **`poly_degree(coeffs)`** — Polynomial degree

- **`poly_strip(coeffs, tol=1e-12)`** — Strip leading zeros

- **`poly_integral_definite(coeffs, a, b)`** — Definite integral

- **`poly_to_str(coeffs, var='x')`** — String form

- **`poly_lagrange(points)`** — Lagrange polynomial

- **`poly_chebyshev_t(n)`** — Chebyshev T
  ```python
  result = tms.poly_chebyshev_t(2)
  print(result)
  ```
  Output: `[2.0, 0.0, -1.0]`

- **`poly_legendre(n)`** — Legendre polynomial
  ```python
  result = tms.poly_legendre(2)
  print(result)
  ```
  Output: `[1.5, 0.0, -0.5]`

- **`poly_hermite(n)`** — Hermite polynomial
  ```python
  result = tms.poly_hermite(2)
  print(result)
  ```
  Output: `[4.0, 0.0, -2.0]`

- **`poly_laguerre(n)`** — Laguerre polynomial
  ```python
  result = tms.poly_laguerre(2)
  print(result)
  ```
  Output: `[1.5, 0.0, 0.0]`

---

## Custom Data Types

**File:** `datatypes.py`

> Custom numeric types such as Fraction, FixedDecimal, Interval, and Ratio are implemented here.

- **`Fraction(numerator=0, denominator=1)`** — Rational fraction
  ```python
  f = tms.Fraction(6, 8)\nprint(f)
  ```
  Output: `3/4`

- **`FixedDecimal(value=0, precision=2)`** — Fixed-precision decimal
  ```python
  d = tms.FixedDecimal(3.14, 2)\nprint(float(d))
  ```
  Output: `3.14`

- **`Interval(lo, hi)`** — Numeric interval
  ```python
  iv = tms.Interval(1, 5)\nprint(3 in iv)
  ```
  Output: `True`

- **`Ratio(a, b)`** — Simplified ratio
  ```python
  r = tms.Ratio(4, 6)\nprint(r.as_float())
  ```
  Output: `0.6666666666666666`

---

## Educational Cryptography

**File:** `crypto.py`

> Educational cryptography helpers, checksums, hashes, Luhn routines, and classic ciphers like Caesar and RSA are included here.

- **`caesar_encrypt(text, shift)`** — Caesar cipher
  ```python
  print(tms.caesar_encrypt("ABC", 3))
  ```
  Output: `DEF`

- **`caesar_decrypt(text, shift)`** — Caesar decryption
  ```python
  print(tms.caesar_decrypt("DEF", 3))
  ```
  Output: `ABC`

- **`caesar_bruteforce(text)`** — Try every shift

- **`vigenere_encrypt(text, key)`** — Vigenere cipher

- **`vigenere_decrypt(text, key)`** — Vigenere decryption

- **`atbash_encrypt(text)`** — Atbash cipher

- **`atbash_decrypt(text)`** — Atbash decryption

- **`rot13(text)`** — ROT13
  ```python
  print(tms.rot13("Hello"))
  ```
  Output: `Uryyb`

- **`affine_encrypt(text, a, b)`** — Affine cipher

- **`affine_decrypt(text, a, b)`** — Affine decryption

- **`rail_fence_encrypt(text, rails)`** — Rail fence cipher

- **`rail_fence_decrypt(text, rails)`** — Rail fence decryption

- **`columnar_encrypt(text, key)`** — Columnar transposition

- **`simple_substitution_encrypt(text, alphabet_map)`** — Simple substitution

- **`simple_substitution_decrypt(text, alphabet_map)`** — Simple substitution decryption

- **`is_prime_miller_rabin(n, witnesses=None)`** — Miller-Rabin primality test
  ```python
  result = tms.is_prime_miller_rabin(2, 2)
  print(result)
  ```
  Output: `True`

- **`rsa_generate_keys(p, q)`** — Generate RSA keys
  ```python
  pub, priv = tms.rsa_generate_keys(61, 53)\nprint(pub[1])
  ```
  Output: `3233`

- **`rsa_encrypt(message, public_key)`** — RSA encryption
  ```python
  pub, priv = tms.rsa_generate_keys(61, 53)\nprint(tms.rsa_encrypt(42, pub))
  ```
  Output: `2557`

- **`rsa_decrypt(ciphertext, private_key)`** — RSA decryption
  ```python
  pub, priv = tms.rsa_generate_keys(61, 53)\nct = tms.rsa_encrypt(42, pub)\nprint(tms.rsa_decrypt(ct, priv))
  ```
  Output: `42`

- **`diffie_hellman_keypair(p, g, private_key)`** — Diffie-Hellman public key

- **`diffie_hellman_shared_secret(public_other, private_self, p)`** — Shared secret
  ```python
  result = tms.diffie_hellman_shared_secret(2, 2, 2)
  print(result)
  ```
  Output: `0`

- **`xor_cipher(data, key)`** — XOR cipher

- **`text_to_bits(text)`** — Text to bits

- **`bits_to_text(bits)`** — Bits to text

- **`hamming_distance(s1, s2)`** — Hamming distance

- **`checksum_sum(data)`** — Sum checksum
  ```python
  result = tms.checksum_sum([1, 2, 3, 4])
  print(result)
  ```
  Output: `10`

- **`checksum_xor(data)`** — XOR checksum
  ```python
  result = tms.checksum_xor([1, 2, 3, 4])
  print(result)
  ```
  Output: `4`

- **`luhn_check(number)`** — Luhn check
  ```python
  result = tms.luhn_check(2)
  print(result)
  ```
  Output: `False`

- **`luhn_generate(partial)`** — Generate Luhn check digit
  ```python
  result = tms.luhn_generate(2)
  print(result)
  ```
  Output: `26`

- **`mod_hash(text, m=997)`** — Simple modular hash

- **`rolling_hash(text, window, base=31, mod=10**9+7)`** — Rolling hash

- **`string_similarity_coefficient(s1, s2)`** — String similarity coefficient

---

## Graph

**File:** `graph.py`

> The graph module provides adjacency-list graph representation, traversals, shortest paths, spanning trees, and ready-made graph constructors.

- **`Graph(directed=False)`** — Graph class
  ```python
  g = tms.Graph()\ng.add_edge("A", "B")\nprint(g.bfs("A"))
  ```
  Output: `A`

- **`add_vertex(v)`** — Add a vertex

- **`add_edge(u, v, weight=1)`** — Add an edge

- **`remove_edge(u, v)`** — Remove an edge

- **`remove_vertex(v)`** — Remove a vertex

- **`neighbors(v)`** — Neighbors

- **`weight(u, v)`** — Edge weight

- **`vertices()`** — Vertex list

- **`edges()`** — Edge list

- **`degree(v)`** — Vertex degree

- **`in_degree(v)`** — In-degree

- **`out_degree(v)`** — Out-degree

- **`has_edge(u, v)`** — Edge existence

- **`bfs(start)`** — Breadth-first search

- **`dfs(start)`** — Depth-first search

- **`has_path(start, end)`** — Path existence

- **`dijkstra(start)`** — Dijkstra

- **`shortest_path(start, end)`** — Shortest path

- **`bellman_ford(start)`** — Bellman-Ford

- **`floyd_warshall()`** — Floyd-Warshall

- **`is_connected()`** — Connected test

- **`topological_sort()`** — Topological sort

- **`minimum_spanning_tree_kruskal()`** — Minimum spanning tree

- **`has_cycle_undirected()`** — Undirected cycle test

- **`is_bipartite()`** — Bipartite test

- **`connected_components()`** — Connected components

- **`density()`** — Graph density

- **`vertex_count()`** — Vertex count

- **`edge_count()`** — Edge count

- **`adjacency_matrix()`** — Adjacency matrix

- **`degree_sequence()`** — Degree sequence

- **`eccentricity(v)`** — Eccentricity

- **`diameter()`** — Diameter

- **`radius()`** — Radius

- **`center()`** — Center

- **`graph_from_edge_list(edges, directed=False)`** — Build from edge list

- **`graph_complete(n)`** — Complete graph
  ```python
  result = tms.graph_complete(2)
  print(result)
  ```
  Output: `<taha_math_shiraz.graph.Graph object at 0x0000022C4A32C550>`

- **`graph_cycle(n)`** — Cycle graph
  ```python
  result = tms.graph_cycle(2)
  print(result)
  ```
  Output: `<taha_math_shiraz.graph.Graph object at 0x0000022C4A32C2D0>`

- **`graph_path(n)`** — Path graph
  ```python
  result = tms.graph_path(2)
  print(result)
  ```
  Output: `<taha_math_shiraz.graph.Graph object at 0x0000022C49EAAFD0>`

- **`graph_star(n)`** — Star graph
  ```python
  result = tms.graph_star(2)
  print(result)
  ```
  Output: `<taha_math_shiraz.graph.Graph object at 0x0000022C49EAB6F0>`

- **`traveling_salesman_brute(graph)`** — Brute-force TSP

---

## Algorithms

**File:** `algorithms.py`

> Sorting, searching, dynamic programming, and array/string algorithms are collected in this module.

- **`bubble_sort(arr)`** — Bubble sort
  ```python
  print(tms.bubble_sort([5, 3, 1]))
  ```
  Output: `[1, 3, 5]`

- **`selection_sort(arr)`** — Selection sort
  ```python
  result = tms.selection_sort([3, 1, 2])
  print(result)
  ```
  Output: `[1, 2, 3]`

- **`insertion_sort(arr)`** — Insertion sort
  ```python
  result = tms.insertion_sort([3, 1, 2])
  print(result)
  ```
  Output: `[1, 2, 3]`

- **`merge_sort(arr)`** — Merge sort
  ```python
  result = tms.merge_sort([3, 1, 2])
  print(result)
  ```
  Output: `[1, 2, 3]`

- **`quick_sort(arr)`** — Quick sort
  ```python
  result = tms.quick_sort([3, 1, 2])
  print(result)
  ```
  Output: `[1, 2, 3]`

- **`heap_sort(arr)`** — Heap sort
  ```python
  result = tms.heap_sort([3, 1, 2])
  print(result)
  ```
  Output: `[1, 2, 3]`

- **`counting_sort(arr, max_val=None)`** — Counting sort
  ```python
  result = tms.counting_sort([3, 1, 2])
  print(result)
  ```
  Output: `[1, 2, 3]`

- **`radix_sort(arr)`** — Radix sort
  ```python
  result = tms.radix_sort([3, 1, 2])
  print(result)
  ```
  Output: `[1, 2, 3]`

- **`shell_sort(arr)`** — Shell sort
  ```python
  result = tms.shell_sort([3, 1, 2])
  print(result)
  ```
  Output: `[1, 2, 3]`

- **`bucket_sort(arr, num_buckets=10)`** — Bucket sort
  ```python
  result = tms.bucket_sort([0.42, 0.32, 0.23])
  print(result)
  ```
  Output: `[0.23, 0.32, 0.42]`

- **`binary_search(arr, target)`** — Binary search
  ```python
  print(tms.binary_search([1, 3, 5, 7], 5))
  ```
  Output: `2`

- **`binary_search_leftmost(arr, target)`** — Leftmost binary search

- **`binary_search_rightmost(arr, target)`** — Rightmost binary search

- **`interpolation_search(arr, target)`** — Interpolation search

- **`exponential_search(arr, target)`** — Exponential search

- **`ternary_search(f, lo, hi, tol)`** — Ternary search

- **`levenshtein_distance(s1, s2)`** — Levenshtein distance
  ```python
  print(tms.levenshtein_distance("kitten", "sitting"))
  ```
  Output: `3`

- **`longest_common_subsequence(s1, s2)`** — LCS
  ```python
  print(tms.longest_common_subsequence("ABCBDAB", "BDCAB"))
  ```
  Output: `4`

- **`longest_common_substring(s1, s2)`** — Longest common substring

- **`knapsack_01(weights, values, capacity)`** — 0/1 knapsack
  ```python
  print(tms.knapsack_01([1, 3, 4], [1, 4, 5], 4))
  ```
  Output: `5`

- **`coin_change(coins, amount)`** — Minimum coin change
  ```python
  print(tms.coin_change([1, 5, 10], 12))
  ```
  Output: `3`

- **`longest_increasing_subsequence(arr)`** — LIS
  ```python
  result = tms.longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
  print(result)
  ```
  Output: `4`

- **`max_subarray(arr)`** — Maximum subarray sum
  ```python
  result = tms.max_subarray([1, 2, 3, 4])
  print(result)
  ```
  Output: `10`

- **`max_subarray_indices(arr)`** — Max subarray indices
  ```python
  result = tms.max_subarray_indices([1, 2, 3, 4])
  print(result)
  ```
  Output: `(0, 3, 10)`

- **`two_sum(arr, target)`** — Two-sum
  ```python
  result = tms.two_sum([1, 2, 3, 4], 2)
  print(result)
  ```
  Output: `None`

- **`three_sum(arr, target)`** — Three-sum
  ```python
  result = tms.three_sum([1, 2, 3, 4], 2)
  print(result)
  ```
  Output: `[]`

- **`flatten(nested)`** — Flatten nested structure
  ```python
  result = tms.flatten(2)
  print(result)
  ```
  Output: `[2]`

- **`rotate_list(arr, k)`** — Rotate list
  ```python
  result = tms.rotate_list([1, 2, 3, 4], 2)
  print(result)
  ```
  Output: `[3, 4, 1, 2]`

- **`chunk_list(arr, size)`** — Chunk list
  ```python
  result = tms.chunk_list([1, 2, 3, 4], 2)
  print(result)
  ```
  Output: `[[1, 2], [3, 4]]`

- **`sliding_window_max(arr, k)`** — Sliding window max
  ```python
  result = tms.sliding_window_max([1, 2, 3, 4], 2)
  print(result)
  ```
  Output: `[2, 3, 4]`

- **`sliding_window_sum(arr, k)`** — Sliding window sum
  ```python
  result = tms.sliding_window_sum([1, 2, 3, 4], 2)
  print(result)
  ```
  Output: `[3, 5, 7]`

- **`running_average(arr)`** — Running average
  ```python
  result = tms.running_average([1, 2, 3, 4])
  print(result)
  ```
  Output: `[1.0, 1.5, 2.0, 2.5]`

- **`cumulative_sum(arr)`** — Cumulative sum
  ```python
  result = tms.cumulative_sum([1, 2, 3, 4])
  print(result)
  ```
  Output: `[1, 3, 6, 10]`

- **`cumulative_product(arr)`** — Cumulative product
  ```python
  result = tms.cumulative_product([1, 2, 3, 4])
  print(result)
  ```
  Output: `[1, 2, 6, 24]`

- **`moving_average(arr, window)`** — Moving average
  ```python
  result = tms.moving_average([1, 2, 3, 4], 2)
  print(result)
  ```
  Output: `[1.5, 2.5, 3.5]`

- **`zip_with(f, a, b)`** — Apply function pairwise

- **`difference_array(arr)`** — First difference array
  ```python
  result = tms.difference_array([1, 2, 3, 4])
  print(result)
  ```
  Output: `[1, 1, 1]`

- **`second_difference_array(arr)`** — Second difference array

---

## Usage and Summary

Because everything is re-exported in `__init__.py`, the easiest way to use the package is:

```python
import taha_math_shiraz as tms

print(tms.PI)
print(tms.sin(tms.PI / 2))
print(tms.mean([1, 2, 3, 4]))
```

You can also import specific modules directly when you only need one part of the library. That approach is useful when you want a clean namespace and only need a focused subsystem such as graphs, statistics, or cryptography.
