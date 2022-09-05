# diferencia_conjuntista_de_listas.py
# Diferencia conjuntista de listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    diferencia : (list[A], list[A]) -> list[A]
# tal que diferencia(xs, ys) es la diferencia de las listas sin
# elementos repetidos xs e ys. Por ejemplo,
#    diferencia([3, 2, 5, 6], [5, 7, 3, 4]) == [2, 6]
#    diferencia([3, 2, 5], [5, 7, 3, 2])    == []
# ---------------------------------------------------------------------

from typing import TypeVar
from timeit import Timer, default_timer
from sys import setrecursionlimit
from hypothesis import given, strategies as st

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

def diferencia1(xs: list[A], ys: list[A]) -> list[A]:
    return [x for x in xs if x not in ys]

# 2ª solución
# ===========

def diferencia2(xs: list[A], ys: list[A]) -> list[A]:
    if not xs:
        return []
    if xs[0] in ys:
        return diferencia2(xs[1:], ys)
    return [xs[0]] + diferencia2(xs[1:], ys)

# 3ª solución
# ===========

def diferencia3(xs: list[A], ys: list[A]) -> list[A]:
    zs = []
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs

# 4ª solución
# ===========

def diferencia4(xs: list[A], ys: list[A]) -> list[A]:
    return list(set(xs) - set(ys))

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_diferencia(xs, ys):
    xs1 = list(set(xs))
    ys1 = list(set(ys))
    assert sorted(diferencia1(xs1, ys1)) ==\
           sorted(diferencia2(xs1, ys1)) ==\
           sorted(diferencia3(xs1, ys1)) ==\
           sorted(diferencia4(xs1, ys1))

# La comprobación es
#    src> poetry run pytest -q diferencia_conjuntista_de_listas.py
#    1 passed in 0.39s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('diferencia1(list(range(0,20000)), list(range(1,20000,2)))')
#    0.89 segundos
#    >>> tiempo('diferencia2(list(range(0,20000)), list(range(1,20000,2)))')
#    2.11 segundos
#    >>> tiempo('diferencia3(list(range(0,20000)), list(range(1,20000,2)))')
#    1.06 segundos
#    >>> tiempo('diferencia4(list(range(0,20000)), list(range(1,20000,2)))')
#    0.01 segundos
