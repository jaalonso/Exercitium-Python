# Relaciones_binarias.py
# Relaciones binarias.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 28-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Una relación binaria R sobre un conjunto A se puede representar
# mediante un par (u,g) donde u es la lista de los elementos de tipo A
# (el universo de R) y g es la lista de pares de elementos de u (el
# grafo de R).
#
# Definir el tipo de dato (Rel a), para representar las relaciones
# binarias sobre a, y la función
#    esRelacionBinaria : (Rel[A]) -> bool
# tal que esRelacionBinaria(r) se verifica si r es una relación
# binaria. Por ejemplo,
#    >>> esRelacionBinaria(([1, 3], [(3, 1), (3, 3)]))
#    True
#    >>> esRelacionBinaria(([1, 3], [(3, 1), (3, 2)]))
#    False
# Además, definir un generador de relaciones binarias y comprobar que
# las relaciones que genera son relaciones binarias.
# ---------------------------------------------------------------------

from random import randint, sample
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A')

Rel = tuple[list[A], list[tuple[A, A]]]

# 1ª solución
# ===========

def esRelacionBinaria(r: Rel[A]) -> bool:
    (u, g) = r
    return all((x in u and y in u for (x, y) in g))

# 2ª solución
# ===========

def esRelacionBinaria2(r: Rel[A]) -> bool:
    (u, g) = r
    if not g:
        return True
    (x, y) = g[0]
    return x in u and y in u and esRelacionBinaria2((u, g[1:]))

# 3ª solución
# ===========

def esRelacionBinaria3(r: Rel[A]) -> bool:
    (u, g) = r
    for (x, y) in g:
        if x not in u or y not in u:
            return False
    return True

# Generador de relaciones binarias
# ================================

# conjuntoArbitrario(n) es un conjunto arbitrario cuyos elementos están
# entre 0 y n-1. Por ejemplo,
#    >>> conjuntoArbitrario(10)
#    [8, 9, 4, 5]
#    >>> conjuntoArbitrario(10)
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    >>> conjuntoArbitrario(10)
#    [0, 1, 2, 3, 6, 7, 9]
#    >>> conjuntoArbitrario(10)
#    [8, 2, 3, 7]
def conjuntoArbitrario(n: int) -> list[int]:
    xs = sample(range(n), randint(0, n))
    return list(set(xs))

# productoCartesiano(xs, ys) es el producto cartesiano de xs e ys. Por
# ejemplo,
#    >>> productoCartesiano([2, 3], [1, 7, 5])
#    [(2, 1), (2, 7), (2, 5), (3, 1), (3, 7), (3, 5)]
def productoCartesiano(xs: list[int], ys: list[int]) -> list[tuple[int, int]]:
    return [(x, y) for x in xs for y in ys]

# sublistaArbitraria(xs) es una sublista arbitraria de xs. Por ejemplo,
#    >>> sublistaArbitraria(range(10))
#    [3, 7]
#    >>> sublistaArbitraria(range(10))
#    []
#    >>> sublistaArbitraria(range(10))
#    [4, 1, 0, 9, 8, 7, 5, 6, 2, 3]
def sublistaArbitraria(xs: list[A]) -> list[A]:
    n = len(xs)
    k = randint(0, n)
    return sample(xs, k)

# relacionArbitraria(n) es una relación arbitraria tal que los elementos
# de su universo están entre 0 y n-1. Por ejemplo,
#    >>> relacionArbitraria(3)
#    ([0, 1], [(1, 0), (1, 1)])
#    >>> relacionArbitraria(3)
#    ([], [])
#    >>> relacionArbitraria(5)
#    ([0, 2, 3, 4], [(2, 0), (3, 3), (2, 3), (4, 0), (3, 4), (4, 2)])
def relacionArbitraria(n: int) -> Rel[int]:
    u = conjuntoArbitrario(n)
    g = sublistaArbitraria(productoCartesiano(u, u))
    return (u, g)

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_esRelacionBinaria(n: int) -> None:
    r = relacionArbitraria(n)
    assert esRelacionBinaria(r)
    assert esRelacionBinaria2(r)
    assert esRelacionBinaria3(r)

# La comprobación es
#    > poetry run pytest -q Relaciones_binarias.py
#    1 passed in 0.14s
