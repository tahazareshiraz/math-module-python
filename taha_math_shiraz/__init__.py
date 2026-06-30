__version__ = "1.0.0"
__author__ = "Taha"

from .constants import *
from .core import *
from .power import *
from .trigonometry import *
from .hyperbolic import *
from .number_theory import *
from .combinatorics import *
from .statistics import *
from .special_functions import *
from .geometry import *
from .sequences import *
from .utils import *
from .numerical import *
from .probability import *
from .conversions import *
from .financial import *
from .logic_sets import *
from .random_gen import (
    TahaRandom,
    random,
    randint,
    uniform,
    choice,
    shuffle,
    gauss,
)

from .matrix import Matrix, matrix_from_vectors, hadamard_product, kronecker_product
from .vector import (
    Vector,
    zero_vector,
    unit_vector,
    sum_vectors,
    average_vector,
    triple_product,
)
from .complex_math import (
    ComplexNumber,
    complex_from_polar,
    complex_add,
    complex_sub,
    complex_mul,
    complex_div,
    complex_roots_of_unity,
    complex_distance,
    complex_sum,
)
from .polynomial import (
    Polynomial,
    polynomial_from_roots,
    quadratic_roots,
    cubic_real_root_count,
    synthetic_division,
)
from .graph_theory import Graph, complete_graph, path_graph, cycle_graph
from .calendar_math import *

pow = pow_
exp_ = exp
