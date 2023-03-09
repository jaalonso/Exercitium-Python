# Relaciones_reflexivas.py
# Relaciones reflexivas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    reflexiva : (Rel) -> bool
# tal que reflexiva(r) se verifica si la relación r es reflexiva. Por
# ejemplo,
#    >>> reflexiva(([1, 3], [(1, 1),(1, 3),(3, 3)]))
#    True
#    >>> reflexiva(([1, 2, 3], [(1, 1),(1, 3),(3, 3)]))
#    False
# ---------------------------------------------------------------------

from random import choice, randint, sample
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Relaciones_binarias import Rel, relacionArbitraria

A = TypeVar('A')

# 1ª solución
# ===========

def reflexiva(r: Rel[A]) -> bool:
    (us, ps) = r
    if not us:
        return True
    return (us[0], us[0]) in ps and reflexiva((us[1:], ps))

# 2ª solución
# ===========

def reflexiva2(r: Rel[A]) -> bool:
    (us, ps) = r
    return all(((x,x) in ps for x in us))

# 3ª solución
# ===========

def reflexiva3(r: Rel[A]) -> bool:
    (us, ps) = r
    for x in us:
        if (x, x) not in ps:
            return False
    return True

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_reflexiva(n: int) -> None:
    r = relacionArbitraria(n)
    res = reflexiva(r)
    assert reflexiva2(r) == res
    assert reflexiva3(r) == res

# La comprobación es
#    > poetry run pytest -q Relaciones_reflexivas.py
#    1 passed in 0.41s
