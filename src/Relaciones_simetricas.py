# Relaciones_simetricas.py
# Relaciones simétricas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 31-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    simetrica : (Rel[A]) -> bool
# tal que simetrica(r) se verifica si la relación r es simétrica. Por
# ejemplo,
#    >>> simetrica(([1, 3], [(1, 1), (1, 3), (3, 1)]))
#    True
#    >>> simetrica(([1, 3], [(1, 1), (1, 3), (3, 2)]))
#    False
#    >>> simetrica(([1, 3], []))
#    True
# ---------------------------------------------------------------------

from random import choice, randint, sample
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Relaciones_binarias import Rel, relacionArbitraria

A = TypeVar('A')

# 1ª solución
# ===========

def simetrica(r: Rel[A]) -> bool:
    (_, g) = r
    return all(((y, x) in g for (x, y) in g))

# 2ª solución
# ===========

def simetrica2(r: Rel[A]) -> bool:
    (_, g) = r
    def aux(ps: list[tuple[A, A]]) -> bool:
        if not ps:
            return True
        (x, y) = ps[0]
        return (y, x) in g and aux(ps[1:])

    return aux(g)

# 3ª solución
# ===========

def simetrica3(r: Rel[A]) -> bool:
    (_, g) = r
    for (x, y) in g:
        if (y, x) not in g:
            return False
    return True

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_simetrica(n: int) -> None:
    r = relacionArbitraria(n)
    res = simetrica(r)
    assert simetrica2(r) == res
    assert simetrica3(r) == res

# La comprobación es
#    > poetry run pytest -q Relaciones_simetricas.py
#    1 passed in 0.11s
