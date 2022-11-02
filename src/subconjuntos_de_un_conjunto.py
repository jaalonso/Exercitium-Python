# subconjuntos_de_un_conjunto.py
# Subconjuntos_de_un_conjunto.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    subconjuntos : (list[A]) -> list[list[A]]
# tal que subconjuntos(xs) es la lista de las subconjuntos de la lista
# xs. Por ejemplo,
#    >>> subconjuntos([2, 3, 4])
#    [[2,3,4], [2,3], [2,4], [2], [3,4], [3], [4], []]
#    >>> subconjuntos([1, 2, 3, 4])
#    [[1,2,3,4], [1,2,3], [1,2,4], [1,2], [1,3,4], [1,3], [1,4], [1],
#       [2,3,4],   [2,3],   [2,4],   [2],   [3,4],   [3],   [4], []]
#
# Comprobar con Hypothesis que el número de elementos de
# (subconjuntos xs) es 2 elevado al número de elementos de xs.
# ---------------------------------------------------------------------

from itertools import combinations
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st
from sympy import FiniteSet

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

def subconjuntos1(xs: list[A]) -> list[list[A]]:
    if xs:
        sub = subconjuntos1(xs[1:])
        return [[xs[0]] + ys for ys in sub] + sub
    return [[]]

# 2ª solución
# ===========

def subconjuntos2(xs: list[A]) -> list[list[A]]:
    if xs:
        sub = subconjuntos1(xs[1:])
        return list(map((lambda ys: [xs[0]] + ys), sub)) + sub
    return [[]]

# 3ª solución
# ===========

def subconjuntos3(xs: list[A]) -> list[list[A]]:
    c = FiniteSet(*xs)
    return list(map(list, c.powerset()))

# 4ª solución
# ===========

def subconjuntos4(xs: list[A]) -> list[list[A]]:
    return [list(ys)
            for r in range(len(xs)+1)
            for ys in combinations(xs, r)]

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers(), max_size=5))
def test_subconjuntos(xs: list[int]) -> None:
    ys = list(set(xs))
    r = sorted([sorted(zs) for zs in subconjuntos1(ys)])
    assert sorted([sorted(zs) for zs in subconjuntos2(ys)]) == r
    assert sorted([sorted(zs) for zs in subconjuntos3(ys)]) == r
    assert sorted([sorted(zs) for zs in subconjuntos4(ys)]) == r

# La comprobación es
#    src> poetry run pytest -q subconjuntos_de_un_conjunto.py
#    1 passed in 0.89s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('subconjuntos1(range(14))')
#    0.00 segundos
#    >>> tiempo('subconjuntos2(range(14))')
#    0.00 segundos
#    >>> tiempo('subconjuntos3(range(14))')
#    6.01 segundos
#    >>> tiempo('subconjuntos4(range(14))')
#    0.00 segundos
#
#    >>> tiempo('subconjuntos1(range(23))')
#    1.95 segundos
#    >>> tiempo('subconjuntos2(range(23))')
#    2.27 segundos
#    >>> tiempo('subconjuntos4(range(23))')
#    1.62 segundos

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.lists(st.integers(), max_size=7))
def test_length_subconjuntos(xs: list[int]) -> None:
    assert len(subconjuntos1(xs)) == 2 ** len(xs)

# La comprobación es
#    src> poetry run pytest -q subconjuntos_de_un_conjunto.py
#    2 passed in 0.95s
