# Reconocimiento_de_subconjunto.py
# Reconocimiento de subconjunto.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 04-abr-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    subconjunto : (list[A], list[A]) -> bool
# tal que (subconjunto xs ys) se verifica si xs es un subconjunto de
# ys. por ejemplo,
#    subconjunto([3, 2, 3], [2, 5, 3, 5])  ==  True
#    subconjunto([3, 2, 3], [2, 5, 6, 5])  ==  False
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

def subconjunto1(xs: list[A], ys: list[A]) -> bool:
    return [x for x in xs if x in ys] == xs

# 2ª solución
# ===========

def subconjunto2(xs: list[A], ys: list[A]) -> bool:
    if not xs:
        return True
    return xs[0] in ys and subconjunto2(xs[1:], ys)

# 3ª solución
# ===========

def subconjunto3(xs: list[A], ys: list[A]) -> bool:
    return all(elem in ys for elem in xs)

# 4ª solución
# ===========

def subconjunto4(xs: list[A], ys: list[A]) -> bool:
    return set(xs) <= set(ys)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_filtraAplica(xs: list[int], ys: list[int]) -> None:
    r = subconjunto1(xs, ys)
    assert subconjunto2(xs, ys) == r
    assert subconjunto3(xs, ys) == r
    assert subconjunto4(xs, ys) == r

# La comprobación es
#    src> poetry run pytest -q Reconocimiento_de_subconjunto.py
#    1 passed in 0.31s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> xs = list(range(2*10**4))
#    >>> tiempo("subconjunto1(xs, xs)")
#    1.15 segundos
#    >>> tiempo("subconjunto2(xs, xs)")
#    2.27 segundos
#    >>> tiempo("subconjunto3(xs, xs)")
#    1.14 segundos
#    >>> tiempo("subconjunto4(xs, xs)")
#    0.00 segundos

# En lo sucesivo usaremos la cuarta definición
subconjunto = subconjunto4
