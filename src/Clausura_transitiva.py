# Clausura_transitiva.py
# Clausura transitiva.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    clausuraTransitiva :: Eq a => Rel a -> Rel a
# tal que (clausuraTransitiva r) es la clausura transitiva de r; es
# decir, la menor relación transitiva que contiene a r. Por ejemplo,
#    >>> clausuraTransitiva (([1, 2, 3, 4, 5, 6], [(1, 2), (2, 5), (5, 6)]))
#    ([1, 2, 3, 4, 5, 6], [(1, 2), (2, 5), (5, 6), (2, 6), (1, 5), (1, 6)])
#
# Comprobar con QuickCheck que clausuraTransitiva es transitiva.
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Relaciones_binarias import Rel, relacionArbitraria
from src.Relaciones_transitivas import transitiva

A = TypeVar('A')

# 1ª solución
# ===========

def clausuraTransitiva(r: Rel[A]) -> Rel[A]:
    (u, g) = r

    def subconjunto(xs: list[tuple[A, A]], ys: list[tuple[A, A]]) -> bool:
        return set(xs) <= set(ys)

    def comp(r: list[tuple[A, A]], s: list[tuple[A, A]]) -> list[tuple[A, A]]:
        return list({(x, z) for (x, y) in r for (y1, z) in s if y == y1})

    def cerradoTr(r: list[tuple[A, A]]) -> bool:
        return subconjunto(comp(r, r), r)

    def union(xs: list[tuple[A, A]], ys: list[tuple[A, A]]) -> list[tuple[A, A]]:
        return xs + [y for y in ys if y not in xs]

    def aux(u1: list[tuple[A, A]]) -> list[tuple[A, A]]:
        if cerradoTr(u1):
            return u1
        return aux(union(u1, comp(u1, u1)))

    return (u, aux(g))

# 2ª solución
# ===========

def clausuraTransitiva2(r: Rel[A]) -> Rel[A]:
    (u, g) = r

    def subconjunto(xs: list[tuple[A, A]], ys: list[tuple[A, A]]) -> bool:
        return set(xs) <= set(ys)

    def comp(r: list[tuple[A, A]], s: list[tuple[A, A]]) -> list[tuple[A, A]]:
        return list({(x, z) for (x, y) in r for (y1, z) in s if y == y1})

    def cerradoTr(r: list[tuple[A, A]]) -> bool:
        return subconjunto(comp(r, r), r)

    def union(xs: list[tuple[A, A]], ys: list[tuple[A, A]]) -> list[tuple[A, A]]:
        return xs + [y for y in ys if y not in xs]

    def aux(u1: list[tuple[A, A]]) -> list[tuple[A, A]]:
        if cerradoTr(u1):
            return u1
        return aux(union(u1, comp(u1, u1)))

    g1: list[tuple[A, A]] = g
    while not cerradoTr(g1):
        g1 = union(g1, comp(g1, g1))
    return (u, g1)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_clausuraTransitiva(n: int) -> None:
    r = relacionArbitraria(n)
    assert clausuraTransitiva(r) == clausuraTransitiva2(r)

# Propiedad
# =========

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_cla(n: int) -> None:
    r = relacionArbitraria(n)
    assert transitiva(clausuraTransitiva(r))

# La función transitiva está definida en el ejercicio
# "Relaciones transitivas" que se encuentra en
# https://bit.ly/42WRPJv

# La comprobación es
#    > poetry run pytest -q Clausura_transitiva.py
#    2 passed in 0.16s
