# segmento_de_una_lista.py
# Segmento de una lista.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    segmento : (int, int, list[A]) -> list[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
#    segmento(3, 4, [3, 4, 1, 2, 7, 9, 0])  ==  [1, 2]
#    segmento(3, 5, [3, 4, 1, 2, 7, 9, 0])  ==  [1, 2, 7]
#    segmento(5, 3, [3, 4, 1, 2, 7, 9, 0])  ==  []
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A')

# 1ª definición
def segmento1(m: int, n: int, xs: list[A]) -> list[A]:
    ys = xs[:n]
    if m == 0:
        return ys
    return ys[m - 1:]

# 2ª definición
def segmento2(m: int, n: int, xs: list[A]) -> list[A]:
    if m == 0:
        return xs[:n]
    return xs[m-1:n]

# La propiedad de equivalencia es
@given(st.integers(min_value=0),
       st.integers(min_value=0),
       st.lists(st.integers()))
def test_equiv_segmento(m: int, n: int, xs: list[int]) -> None:
    assert segmento1(m, n, xs) == segmento2(m, n, xs)

# La comprobación es
#    src> poetry run pytest -q segmento_de_una_lista.py
#    1 passed in 0.19s
