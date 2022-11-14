# segmentos_cuyos_elementos_cumple_una_propiedad.py
# Segmentos cuyos elementos cumplen una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    segmentos : (Callable[[A], bool], list[A]) -> list[list[A]]
# tal que segmentos(p, xs) es la lista de los segmentos de xs cuyos
# elementos verifican la propiedad p. Por ejemplo,
#    >>> segmentos1((lambda x: x % 2 == 0), [1,2,0,4,9,6,4,5,7,2])
#    [[2, 0, 4], [6, 4], [2]]
#    >>> segmentos1((lambda x: x % 2 == 1), [1,2,0,4,9,6,4,5,7,2])
#    [[1], [9], [5, 7]]
# ---------------------------------------------------------------------

from itertools import dropwhile, takewhile
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Callable, TypeVar

from more_itertools import split_at

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

def segmentos1(p: Callable[[A], bool], xs: list[A]) -> list[list[A]]:
    if not xs:
        return []
    if p(xs[0]):
        return [list(takewhile(p, xs))] + \
            segmentos1(p, list(dropwhile(p, xs[1:])))
    return segmentos1(p, xs[1:])

# 2ª solución
# ===========

def segmentos2(p: Callable[[A], bool], xs: list[A]) -> list[list[A]]:
    return list(filter((lambda x: x), split_at(xs, lambda x: not p(x))))

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('segmentos1(lambda x: x % 2 == 0, range(10**4))')
#    0.55 segundos
#    >>> tiempo('segmentos2(lambda x: x % 2 == 0, range(10**4))')
#    0.00 segundos
