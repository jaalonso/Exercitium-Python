# reconocimiento_de_subconjunto.py
# Reconocimiento de subconjunto.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    subconjunto : (list[A], list[A]) -> bool
# tal que subconjunto(xs, ys) se verifica si xs es un subconjunto de
# ys. por ejemplo,
#    subconjunto([3, 2, 3], [2, 5, 3, 5])  ==  True
#    subconjunto([3, 2, 3], [2, 5, 6, 5])  ==  False
# ---------------------------------------------------------------------

from typing import TypeVar
from timeit import Timer, default_timer
from sys import setrecursionlimit
from hypothesis import given, strategies as st

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
def subconjunto1(xs: list[A],
                 ys: list[A]) -> bool:
    return [x for x in xs if x in ys] == xs

# 2ª solución
def subconjunto2(xs: list[A],
                 ys: list[A]) -> bool:
    if xs:
        return xs[0] in ys and subconjunto2(xs[1:], ys)
    return True

# 3ª solución
def subconjunto3(xs: list[A],
                 ys: list[A]) -> bool:
    return all(x in ys for x in xs)

# 4ª solución
def subconjunto4(xs: list[A],
                 ys: list[A]) -> bool:
    return set(xs) <= set(ys)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_subconjunto(xs, ys):
    assert subconjunto1(xs, ys)\
           == subconjunto2(xs, ys)\
           == subconjunto3(xs, ys)\
           == subconjunto4(xs, ys)

# La comprobación es
#    src> poetry run pytest -q reconocimiento_de_subconjunto.py
#    1 passed in 0.34s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo medio (en segundos) de 10 evaluaciones de la expresión e.
    """
    return Timer(e, "", default_timer, globals()).timeit(10) / 10

# La comparación es
#    >>> xs = list(range(20000))
#    >>> tiempo('subconjunto1(xs, xs)')
#    1.2694050386000526
#    >>> tiempo('subconjunto2(xs, xs)')
#    1.9486201640998844
#    >>> tiempo('subconjunto3(xs, xs)')
#    1.2683724896000057
#    >>> tiempo('subconjunto4(xs, xs)')
#    0.0030952897999668495
