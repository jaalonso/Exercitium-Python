# aplica_segun_propiedad.py
# Aplica según propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 21-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    filtraAplica : (Callable[[A], B], Callable[[A], bool], list[A])
#                   -> list[B]
# tal que filtraAplica(f, p, xs) es la lista obtenida aplicándole a los
# elementos de xs que cumplen el predicado p la función f. Por ejemplo,
#    >>> filtraAplica(lambda x: x + 4, lambda x: x < 3, range(1, 7))
#    [5, 6]
# ---------------------------------------------------------------------

from functools import reduce
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Callable, TypeVar

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

A = TypeVar('A')
B = TypeVar('B')

# 1ª solución
# ===========

def filtraAplica1(f: Callable[[A], B],
                  p: Callable[[A], bool],
                  xs: list[A]) -> list[B]:
    return [f(x) for x in xs if p(x)]

# 2ª solución
# ===========

def filtraAplica2(f: Callable[[A], B],
                  p: Callable[[A], bool],
                  xs: list[A]) -> list[B]:
    return list(map(f, filter(p, xs)))

# 3ª solución
# ===========

def filtraAplica3(f: Callable[[A], B],
                  p: Callable[[A], bool],
                  xs: list[A]) -> list[B]:
    if not xs:
        return []
    if p(xs[0]):
        return [f(xs[0])] + filtraAplica3(f, p, xs[1:])
    return filtraAplica3(f, p, xs[1:])

# 4ª solución
# ===========

def filtraAplica4(f: Callable[[A], B],
                  p: Callable[[A], bool],
                  xs: list[A]) -> list[B]:
    def g(ys: list[B], x: A) -> list[B]:
        if p(x):
            return ys + [f(x)]
        return ys

    return reduce(g, xs, [])

# 5ª solución
# ===========

def filtraAplica5(f: Callable[[A], B],
                  p: Callable[[A], bool],
                  xs: list[A]) -> list[B]:
    r = []
    for x in xs:
        if p(x):
            r.append(f(x))
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers()))
def test_filtraAplica(xs: list[int]) -> None:
    def f(x: int) -> int:
        return x + 4
    def p(x: int) -> bool:
        return x < 3
    r = filtraAplica1(f, p, xs)
    assert filtraAplica2(f, p, xs) == r
    assert filtraAplica3(f, p, xs) == r
    assert filtraAplica4(f, p, xs) == r
    assert filtraAplica5(f, p, xs) == r

# La comprobación es
#    src> poetry run pytest -q aplica_segun_propiedad.py
#    1 passed in 0.25s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('filtraAplica1(lambda x: x, lambda x: x % 2 == 0, range(10**5))')
#    0.02 segundos
#    >>> tiempo('filtraAplica2(lambda x: x, lambda x: x % 2 == 0, range(10**5))')
#    0.01 segundos
#    >>> tiempo('filtraAplica3(lambda x: x, lambda x: x % 2 == 0, range(10**5))')
#    Process Python violación de segmento (core dumped)
#    >>> tiempo('filtraAplica4(lambda x: x, lambda x: x % 2 == 0, range(10**5))')
#    4.07 segundos
#    >>> tiempo('filtraAplica5(lambda x: x, lambda x: x % 2 == 0, range(10**5))')
#    0.01 segundos
#
#    >>> tiempo('filtraAplica1(lambda x: x, lambda x: x % 2 == 0, range(10**7))')
#    1.66 segundos
#    >>> tiempo('filtraAplica2(lambda x: x, lambda x: x % 2 == 0, range(10**7))')
#    1.00 segundos
#    >>> tiempo('filtraAplica5(lambda x: x, lambda x: x % 2 == 0, range(10**7))')
#    1.21 segundos
