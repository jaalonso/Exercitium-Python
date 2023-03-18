# Relaciones_irreflexivas.py
# Relaciones irreflexivas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 07-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    irreflexiva : (Rel[A]) -> bool
# tal que irreflexiva(r) se verifica si la relación r es irreflexiva;
# es decir, si ningún elemento de su universo está relacionado con
# él mismo. Por ejemplo,
#    irreflexiva(([1, 2, 3], [(1, 2), (2, 1), (2, 3)]))  ==  True
#    irreflexiva(([1, 2, 3], [(1, 2), (2, 1), (3, 3)]))  ==  False
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Relaciones_binarias import Rel, relacionArbitraria

A = TypeVar('A')

# 1ª solución
# ===========

def irreflexiva(r: Rel[A]) -> bool:
    (u, g) = r
    return all(((x, x) not in g for x in u))

# 2ª solución
# ===========

def irreflexiva2(r: Rel[A]) -> bool:
    (u, g) = r
    def aux(xs: list[A]) -> bool:
        if not xs:
            return True
        return (xs[0], xs[0]) not in g and aux(xs[1:])

    return aux(u)

# 3ª solución
# ===========

def irreflexiva3(r: Rel[A]) -> bool:
    (u, g) = r
    for x in u:
        if (x, x) in g:
            return False
    return True

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_irreflexiva(n: int) -> None:
    r = relacionArbitraria(n)
    res = irreflexiva(r)
    assert irreflexiva2(r) == res
    assert irreflexiva3(r) == res

# La comprobación es
#    > poetry run pytest -q Relaciones_irreflexivas.py
#    1 passed in 0.12s
