# representacion_densa_de_polinomios.py
# Representación densa de polinomios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 21-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los polinomios pueden representarse de forma dispersa o densa. Por
# ejemplo, el polinomio 6x^4-5x^2+4x-7 se puede representar de forma
# dispersa por [6,0,-5,4,-7] y de forma densa por
# [(4,6),(2,-5),(1,4),(0,-7)].
#
# Definir la función
#    densa : (list[int]) -> list[tuple[int, int]]
# tal que densa(xs) es la representación densa del polinomio cuya
# representación dispersa es xs. Por ejemplo,
#   densa([6, 0, -5, 4, -7])  == [(4, 6), (2, -5), (1, 4), (0, -7)]
#   densa([6, 0, 0, 3, 0, 4]) == [(5, 6), (2, 3), (0, 4)]
#   densa([0])                == [(0, 0)]
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def densa1(xs: list[int]) -> list[tuple[int, int]]:
    n = len(xs)
    return [(x, y)
            for (x, y) in zip(range(n-1, 0, -1), xs)
            if y != 0] + [(0, xs[-1])]

# 2ª solución
# ===========

def densa2(xs: list[int]) -> list[tuple[int, int]]:
    n = len(xs)
    return list(filter(lambda p: p[1] != 0,
                       zip(range(n-1, 0, -1), xs))) + [(0, xs[-1])]

# 3ª solución
# ===========

def densa3(xs: list[int]) -> list[tuple[int, int]]:
    def aux(ys: list[int], n: int) -> list[tuple[int, int]]:
        if n == 0:
            return [(0, ys[0])]
        if ys[0] == 0:
            return aux(ys[1:], n-1)
        return [(n, ys[0])] + aux(ys[1:], n-1)

    return aux(xs, len(xs) - 1)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers(), min_size=1))
def test_densa(xs: list[int]) -> None:
    r = densa1(xs)
    assert densa2(xs) == r
    assert densa3(xs) == r

# La comprobación es
#    src> poetry run pytest -q representacion_densa_de_polinomios.py
#    1 passed in 0.27s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('densa1(range(1, 10**4))')
#    0.00 segundos
#    >>> tiempo('densa2(range(1, 10**4))')
#    0.00 segundos
#    >>> tiempo('densa3(range(1, 10**4))')
#    0.25 segundos
#
#    >>> tiempo('densa1(range(1, 10**7))')
#    1.87 segundos
#    >>> tiempo('densa2(range(1, 10**7))')
#    2.15 segundos
