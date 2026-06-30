from .power import sqrt, cbrt, pow_, exp, expm1, log1p, log, log2, log10
from .basics import isnan, isinf, isfinite, copysign, fabs, trunc, floor, ceil, fmod, remainder, modf
from .linalg import Vector, Matrix, Complex, vector_projection, vector_reflection, matrix_power, matrix_from_function, rotation_matrix_2d, rotation_matrix_x, rotation_matrix_y, rotation_matrix_z, scaling_matrix, translation_apply


def euclidean_norm(v):
    return sqrt(sum(c * c for c in v))



def manhattan_distance(p1, p2):
    return sum(fabs(a - b) for a, b in zip(p1, p2))



def chebyshev_distance(p1, p2):
    return max(fabs(a - b) for a, b in zip(p1, p2))



def minkowski_distance(p1, p2, p):
    return sum(fabs(a - b) ** p for a, b in zip(p1, p2)) ** (1.0 / p)



def cosine_similarity(a, b):
    av = Vector(a)
    bv = Vector(b)
    denom = av.norm() * bv.norm()
    if denom == 0:
        return 0.0
    return av.dot(bv) / denom

