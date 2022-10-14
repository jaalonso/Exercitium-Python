# suma_elementos_consecutivos.py
# Suma elementos consecutivos
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    sumaConsecutivos :: [Integer] -> [Integer]
# tal que (sumaConsecutivos xs) es la suma de los pares de elementos
# consecutivos de la lista xs. Por ejemplo,
#    sumaConsecutivos([3, 1, 5, 2])      ==  [4, 6, 7]
#    sumaConsecutivos([3])               ==  []
#    last (sumaConsecutivos [1..10^8])  ==  199999999
# ---------------------------------------------------------------------

from operator import add
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def sumaConsecutivos1(xs: list[int]) -> list[int]:
    return [x + y for (x, y) in zip(xs, xs[1:])]

# 2ª solución
# ===========

def sumaConsecutivos2(xs: list[int]) -> list[int]:
    return list(map(add, xs, xs[1:]))

# 3ª solución
# ===========

def sumaConsecutivos3(xs: list[int]) -> list[int]:
    if len(xs) >= 2:
        return [xs[0] + xs[1]] + sumaConsecutivos3(xs[1:])
    return []

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers(min_value=1, max_value=100)))
def test_sumaConsecutivos(xs: list[int]) -> None:
    r = sumaConsecutivos1(xs)
    assert sumaConsecutivos2(xs) == r
    assert sumaConsecutivos3(xs) == r

# La comprobación es
#    src> poetry run pytest -q suma_elementos_consecutivos.py
#    1 passed in 0.26s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('sumaConsecutivos1(range(1, 10**4))')
#    0.00 segundos
#    >>> tiempo('sumaConsecutivos2(range(1, 10**4))')
#    0.00 segundos
#    >>> tiempo('sumaConsecutivos3(range(1, 10**4))')
#    0.18 segundos
#
#    >>> tiempo('sumaConsecutivos1(range(1, 10**8))')
#    8.34 segundos
#    >>> tiempo('sumaConsecutivos2(range(1, 10**8))')
#    6.28 segundos
