# Lista_cuadrada.py
# Lista cuadrada.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-febrero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    listaCuadrada :: Int -> a -> [a] -> [[a]]
# tal que (listaCuadrada n x xs) es una lista de n listas de longitud n
# formadas con los elementos de xs completada con x, si no xs no tiene
# suficientes elementos. Por ejemplo,
#    >>> listaCuadrada(3, 7, [0,3,5,2,4])
#    [[0, 3, 5], [2, 4, 7], [7, 7, 7]]
# ---------------------------------------------------------------------

from itertools import chain, islice, repeat
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st
from more_itertools import chunked

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

# grupos(n, xs) es la lista obtenida agrupando los elementos de xs en
# grupos de n elementos, salvo el último que puede tener menos. Por
# ejemplo,
#    >>> grupos(2, [4,2,5,7,6])
#    [[4, 2], [5, 7], [6]]
def grupos(n: int, xs: list[A]) -> list[list[A]]:
    if not xs:
        return []
    return [list(islice(xs, n))] + grupos(n, xs[n:])

def listaCuadrada1(n: int, x: A, xs: list[A]) -> list[list[A]]:
    return grupos(n, list(islice(chain(xs, repeat(x)), n * n)))

# 2ª solución
# ===========

def grupos2(n: int, xs: list[A]) -> list[list[A]]:
    if not xs:
        return []
    ys, zs = xs[:n], xs[n:]
    return [ys] + grupos(n, zs)

def listaCuadrada2(n: int, x: A, xs: list[A]) -> list[list[A]]:
    return grupos2(n, list(islice(chain(xs, repeat(x)), n * n)))

# 3ª solución
# ===========

def listaCuadrada3(n: int, x: A, xs: list[A]) -> list[list[A]]:
    return list(chunked(list(islice(chain(xs, repeat(x)), n * n)), n))

# listaCuadrada3 :: Int -> a -> [a] -> [[a]]
# listaCuadrada3 n x xs =
#   take n (chunksOf n (xs ++ repeat x))

# Verificación
# ============

def test_listaCuadrada() -> None:
    for listaCuadrada in [listaCuadrada1, listaCuadrada2, listaCuadrada3]:
        assert listaCuadrada(3, 7, [0,3,5,2,4]) == [[0, 3, 5], [2, 4, 7], [7, 7, 7]]
        print(f"Verificado {listaCuadrada.__name__}")

# La verificación es
#    >>> test_listaCuadrada()
#    Verificado listaCuadrada1
#    Verificado listaCuadrada2
#    Verificado listaCuadrada3

# Comprobación de la equivalencia
# ===============================

# La propiedad es
@given(st.integers(min_value=1, max_value=100),
       st.integers(),
       st.lists(st.integers(), max_size=100))
def test_listaCuadrada_equiv(n: int, x: int, xs: list[int]) -> None:
    r = listaCuadrada1(n, x, xs)
    assert listaCuadrada2(n, x, xs) == r
    assert listaCuadrada3(n, x, xs) == r

# La comprobación es
#    >>> test_listaCuadrada_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('listaCuadrada1(10**3, 5, range(100))')
#    3.55 segundos
#    >>> tiempo('listaCuadrada2(10**3, 5, range(100))')
#    3.44 segundos
#    >>> tiempo('listaCuadrada3(10**3, 5, range(100))')
#    0.06 segundos
