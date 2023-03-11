# Composicion_de_relaciones_binarias_v2.py
# Composición de relaciones binarias.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 03-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    composicion : (Rel[A], Rel[A]) -> Rel[A]
# tal que composicion(r, s) es la composición de las relaciones r y
# s. Por ejemplo,
#    >>> composicion(([1,2],[(1,2),(2,2)]), ([1,2],[(2,1)]))
#    ([1, 2], [(1, 1), (2, 1)])
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Relaciones_binarias import Rel, relacionArbitraria

A = TypeVar('A')

# 1ª solución
# ===========

def composicion(r1: Rel[A], r2: Rel[A]) -> Rel[A]:
    (u1, g1) = r1
    (_,  g2) = r2
    return (u1, [(x, z) for (x, y) in g1 for (u, z) in g2 if y == u])

# 2ª solución
# ===========

def composicion2(r1: Rel[A], r2: Rel[A]) -> Rel[A]:
    (u1, g1) = r1
    (_,  g2) = r2
    def aux(g: list[tuple[A, A]]) -> list[tuple[A, A]]:
        if not g:
            return []
        (x, y) = g[0]
        return [(x, z) for (u, z) in g2 if y == u] + aux(g[1:])

    return (u1, aux(g1))

# 2ª solución
# ===========

def composicion3(r1: Rel[A], r2: Rel[A]) -> Rel[A]:
    (u1, g1) = r1
    (_,  g2) = r2
    r: list[tuple[A, A]] = []
    for (x, y) in g1:
        r = r + [(x, z) for (u, z) in g2 if y == u]
    return (u1, r)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10),
       st.integers(min_value=0, max_value=10))
def test_simetrica(n: int, m: int) -> None:
    r1 = relacionArbitraria(n)
    r2 = relacionArbitraria(m)
    res = composicion(r1, r2)
    assert composicion2(r1, r2) == res
    assert composicion2(r1, r2) == res

# La comprobación es
#    > poetry run pytest -q Composicion_de_relaciones_binarias_v2.py
#    1 passed in 0.19s
