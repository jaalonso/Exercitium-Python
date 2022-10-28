# producto_cartesiano_de_dos_conjuntos.py
# Producto cartesiano de dos conjuntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 2-noviembre-2022
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# Definir la función
#    producto : (list[A], list[B]) -> list[tuple[(A, B)]]
# tal que producto(xs, ys) es el producto cartesiano de xs e ys. Por
# ejemplo,
#    producto([1, 3], [2, 4]) == [(1, 2), (1, 4), (3, 2), (3, 4)]
#
# Comprobar con QuickCheck que el número de elementos de (producto xs
# ys) es el producto del número de elementos de xs y de ys.
# -------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

A = TypeVar('A')
B = TypeVar('B')

# 1ª solución
# ===========

def producto1(xs: list[A], ys: list[B]) -> list[tuple[A, B]]:
    return [(x, y) for x in xs for y in ys]

# 2ª solución
# ===========

def producto2(xs: list[A], ys: list[B]) -> list[tuple[A, B]]:
    if xs:
        return [(xs[0], y) for y in ys] + producto2(xs[1:], ys)
    return []

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_producto(xs: list[int], ys: list[int]) -> None:
    assert sorted(producto1(xs, ys)) == sorted(producto2(xs, ys))

# La comprobación es
#    src> poetry run pytest -q producto_cartesiano_de_dos_conjuntos.py
#    1 passed in 0.31s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('len(producto1(range(0, 1000), range(0, 500)))')
#    0.03 segundos
#    >>> tiempo('len(producto2(range(0, 1000), range(0, 500)))')
#    2.58 segundos

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_elementos_producto(xs: list[int], ys: list[int]) -> None:
    assert len(producto1(xs, ys)) == len(xs) * len(ys)

# La comprobación es
#    src> poetry run pytest -q producto_cartesiano_de_dos_conjuntos.py
#    2 passed in 0.48s
