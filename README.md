# taha-math-shiraz

A pure-Python library that reimplements Python's built-in `math` module
(and the `statistics` module) completely from scratch, without relying on
`math` or `cmath` internally, plus a large collection of extra utilities:
number theory, linear algebra, geometry, calculus, interpolation,
probability distributions, base conversions, and more.

## Installation

```bash
pip install .
```

or simply copy the `taha_math_shiraz/` folder next to your project.

## Usage

```python
import taha_math_shiraz as tms

print(tms.PI)
print(tms.sqrt(2))
print(tms.sin(tms.PI / 2))
print(tms.factorial(10))
print(tms.is_prime(97))
print(tms.mean([1, 2, 3, 4, 5]))

m = tms.Matrix([[1, 2], [3, 4]])
print(m.determinant())
```

You can also import only what you need from a specific submodule:

```python
from taha_math_shiraz.trigonometry import sin, cos
from taha_math_shiraz.linalg import Vector, Matrix
from taha_math_shiraz.numbertheory import is_prime, fibonacci
```

## Package layout

```
taha_math_shiraz/
    __init__.py        re-exports the full public API
    constants.py        PI, E, TAU, INF, NAN, ...
    basics.py            fabs, floor, ceil, fmod, isnan, isinf, ...
    numtheory_core.py    factorial, gcd, lcm, isqrt
    power.py             sqrt, cbrt, pow_, exp, log, log2, log10, ...
    trigonometry.py      sin, cos, tan, asin, acos, atan, sinh, cosh, ...
    aggregates.py        fsum, prod, isclose, comb, perm
    special.py           gamma, lgamma, erf, erfc, frexp, ldexp, ...
    numbertheory.py      primes, divisors, totient, fibonacci, polygonal numbers, ...
    statistics_mod.py    mean, median, mode, variance, stdev, correlation, ...
    probability.py       binomial/normal/poisson/exponential distributions
    linalg.py            Vector, Matrix, Complex and related helpers
    combinatorics.py     permutations, combinations, partitions, bell numbers
    geometry.py          areas, volumes, distances, line intersection, ...
    calculus.py          derivative, integral, root-finding methods
    conversions.py       unit conversions (temperature, distance, mass)
    interpolation.py     Lagrange/Newton interpolation, continued fractions
    randomutil.py        a simple linear congruential generator
    baseconv.py          base conversion, Roman numerals
    series.py            arithmetic/geometric series sums
    activations.py       sigmoid, relu, clamp, lerp, smoothstep
    metrics.py           distance metrics, cosine similarity
```

## Tests

Tests live in the `tests/` folder and are split by topic, mirroring the
package layout. Run all of them with:

```bash
python -m unittest discover -s tests -v
```
