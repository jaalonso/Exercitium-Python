# maximo_de_una_lista.py
# Máximo de una lista
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    maximo : (list[A]) -> A:
# tal que maximo(xs) es el máximo de la lista xs. Por ejemplo,
#    maximo([3,7,2,5])                  ==  7
#    maximo(["todo","es","falso"])      ==  "todo"
#    maximo(["menos","alguna","cosa"])  ==  "menos"
# ---------------------------------------------------------------------

from abc import abstractmethod
from functools import reduce
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Any, TypeVar, Protocol

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

A = TypeVar('A', bound="Comparable")

class Comparable(Protocol):
    """Para comparar"""
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self: A, other: A) -> bool:
        pass

    def __gt__(self: A, other: A) -> bool:
        return (not self < other) and self != other

    def __le__(self: A, other: A) -> bool:
        return self < other or self == other

    def __ge__(self: A, other: A) -> bool:
        return not self < other

# 1ª solución
# ===========

def maximo1(xs: list[A]) -> A:
    if len(xs) == 1:
        return xs[0]
    return max(xs[0], maximo1(xs[1:]))

# 2ª solución
# ===========

def maximo2(xs: list[A]) -> A:
    return reduce(max, xs)

# 3ª solución
# ===========

def maximo3(xs: list[A]) -> A:
    return max(xs)

# ============================

# La propiedad es
@given(st.lists(st.integers(), min_size=2))
def test_maximo(xs: list[int]) -> None:
    r = maximo1(xs)
    assert maximo2(xs) == r
    assert maximo3(xs) == r

# La comprobación es
#    src> poetry run pytest -q maximo_de_una_lista.py
#    1 passed in 0.33s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('maximo1(range(2*10**4))')
#    0.03 segundos
#    >>> tiempo('maximo2(range(2*10**4))')
#    0.00 segundos
#    >>> tiempo('maximo3(range(2*10**4))')
#    0.00 segundos
#
#    >>> tiempo('maximo2(range(5*10**6))')
#    0.38 segundos
#    >>> tiempo('maximo3(range(5*10**6))')
#    0.21 segundos
