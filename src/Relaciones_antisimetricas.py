# Relaciones_antisimetricas.py
# Relaciones antisimétricas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    antisimetrica : (Rel[A]) -> bool
# tal que antisimetrica(r) se verifica si la relación r es
# antisimétrica; es decir, si (x,y) e (y,x) están relacionado, entonces
# x=y. Por ejemplo,
#    >>> antisimetrica(([1,2],[(1,2)]))
#    True
#    >>> antisimetrica(([1,2],[(1,2),(2,1)]))
#    False
#    >>> antisimetrica(([1,2],[(1,1),(2,1)]))
#    True
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Relaciones_binarias import Rel, relacionArbitraria

A = TypeVar('A')

# 1ª solución
# ===========

def antisimetrica(r: Rel[A]) -> bool:
    (_, g) = r
    return [(x, y) for (x, y) in g if x != y and (y, x) in g] == []

# 2ª solución
# ===========

def antisimetrica2(r: Rel[A]) -> bool:
    (_, g) = r
    return all(((y, x) not in g for (x, y) in g if x != y))

# 3ª solución
# ===========

def antisimetrica3(r: Rel[A]) -> bool:
    (u, g) = r
    return all ((not ((x, y) in g and (y, x) in g) or x == y
                 for x in u for y in u))

# 4ª solución
# ===========

def antisimetrica4(r: Rel[A]) -> bool:
    (_, g) = r
    def aux(xys: list[tuple[A, A]]) -> bool:
        if not xys:
            return True
        (x, y) = xys[0]
        return ((y, x) not in g or x == y) and aux(xys[1:])

    return aux(g)

# 5ª solución
# ===========

def antisimetrica5(r: Rel[A]) -> bool:
    (_, g) = r
    for (x, y) in g:
        if (y, x) in g and x != y:
            return False
    return True

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_antisimetrica(n: int) -> None:
    r = relacionArbitraria(n)
    res = antisimetrica(r)
    assert antisimetrica2(r) == res
    assert antisimetrica3(r) == res
    assert antisimetrica4(r) == res
    assert antisimetrica5(r) == res

# La comprobación es
#    > poetry run pytest -q Relaciones_antisimetricas.py
#    1 passed in 0.13s
