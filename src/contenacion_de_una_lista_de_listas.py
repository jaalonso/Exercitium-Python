# concatenacion_de_una_lista_de_listas.py
# Concatenación de una lista de listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 18-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir, por recursión, la función
#    conc : (list[list[A]]) -> list[A]
# tal que conc(xss) es la concenación de las listas de xss. Por
# ejemplo,
#    conc([[1,3],[2,4,6],[1,9]])  ==  [1,3,2,4,6,1,9]
#
# Comprobar con hypothesis que la longitud de conc(xss) es la suma de
# las longitudes de los elementos de xss.
# ---------------------------------------------------------------------

from functools import reduce
from operator import concat
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Any, TypeVar

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

def conc1(xss: list[list[A]]) -> list[A]:
    return [x for xs in xss for x in xs]

# 2ª solución
# ===========

def conc2(xss: list[list[A]]) -> list[A]:
    if not xss:
        return []
    return xss[0] + conc2(xss[1:])

# 3ª solución
# ===========

def conc3(xss: Any) -> Any:
    return reduce(concat, xss)

# 4ª solución
# ===========

def conc4(xss: list[list[A]]) -> list[A]:
    r = []
    for xs in xss:
        for x in xs:
            r.append(x)
    return r

# La propiedad es
@given(st.lists(st.lists(st.integers()), min_size=1))
def test_conc(xss: list[list[int]]) -> None:
    r = conc1(xss)
    assert conc2(xss) == r
    assert conc3(xss) == r
    assert conc4(xss) == r

# La comprobación es
#    src> poetry run pytest -q concatenacion_de_una_lista_de_listas.py
#    1 passed in 0.63s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('conc1([list(range(n)) for n in range(1500)])')
#    0.04 segundos
#    >>> tiempo('conc2([list(range(n)) for n in range(1500)])')
#    6.28 segundos
#    >>> tiempo('conc3([list(range(n)) for n in range(1500)])')
#    2.55 segundos
#    >>> tiempo('conc4([list(range(n)) for n in range(1500)])')
#    0.09 segundos
#
#    >>> tiempo('conc1([list(range(n)) for n in range(10000)])')
#    2.01 segundos
#    >>> tiempo('conc4([list(range(n)) for n in range(10000)])')
#    2.90 segundos
#
# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.lists(st.lists(st.integers()), min_size=1))
def test_long_conc(xss: list[list[int]]) -> None:
    assert len(conc1(xss)) == sum(map(len, xss))

# prop_long_conc :: [[Int]] -> Bool
# prop_long_conc xss =
#   length (conc1 xss) == sum (map length xss)
#
# La comprobación es
#    λ> quickCheck prop_long_conc
#    +++ OK, passed 100 tests.
