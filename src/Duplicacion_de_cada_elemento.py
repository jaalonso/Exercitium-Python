# Duplicacion_de_cada_elemento.py
# Duplicación de cada elemento.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-febrero-2024
# ======================================================================

# ---------------------------------------------------------------------
# Definir la función
#    duplicaElementos : (list[A]) -> list[A]
# tal que duplicaElementos(xs) es la lista obtenida duplicando cada
# elemento de xs. Por ejemplo,
#    >>> duplicaElementos([3,2,5])
#    [3, 3, 2, 2, 5, 5]
#    >>> "".join(duplicaElementos("Haskell"))
#    'HHaasskkeellll'
# ---------------------------------------------------------------------

from functools import reduce
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A')

# 1ª solución
# ===========

def duplicaElementos1(ys: list[A]) -> list[A]:
    if not ys:
        return []
    x, *xs = ys
    return [x, x] + duplicaElementos1(xs)

# 2 solución
# ===========

def duplicaElementos2(xs: list[A]) -> list[A]:
    return reduce(lambda ys, x: ys + [x, x], xs, [])

# 3ª solución
# ===========

def duplicaElementos3(xs: list[A]) -> list[A]:
    return [x for x in xs for _ in range(2)]

# 4ª solución
# ===========

def duplicaElementos4(xs: list[A]) -> list[A]:
    ys = []
    for x in xs:
        ys.append(x)
        ys.append(x)
    return ys

# Verificación
# ============

def test_duplicaElementos() -> None:
    for duplicaElementos in [duplicaElementos1, duplicaElementos2,
                             duplicaElementos3, duplicaElementos4]:
        assert duplicaElementos([3,2,5]) == [3,3,2,2,5,5]
    print("Verificado")

# La verificación es
#    >>> test_duplicaElementos()
#    Verificado

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.lists(st.integers()))
def test_duplicaElementos_equiv(xs: list[int]) -> None:
    r = duplicaElementos1(xs)
    assert duplicaElementos2(xs) == r
    assert duplicaElementos3(xs) == r
    assert duplicaElementos4(xs) == r

# La comprobación es
#    >>> test_duplicaElementos_equiv()
#    >>>
