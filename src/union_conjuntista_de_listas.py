# union_conjuntista_de_listas.py
# Unión conjuntista de listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    union : (list[A], list[A]) -> list[A]
# tal que union(xs, ys) es la unión de las listas sin elementos
# repetidos xs e ys. Por ejemplo,
#    union([3, 2, 5], [5, 7, 3, 4])  ==  [3, 2, 5, 7, 4]
#
# Comprobar con Hypothesis que la unión es conmutativa.
# ---------------------------------------------------------------------

from typing import TypeVar
from timeit import Timer, default_timer
from sys import setrecursionlimit
from hypothesis import given, strategies as st

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

def union1(xs: list[A], ys: list[A]) -> list[A]:
    return xs + [y for y in ys if y not in xs]

# 2ª solución
# ===========

def union2(xs: list[A], ys: list[A]) -> list[A]:
    if not xs:
        return ys
    if xs[0] in ys:
        return union2(xs[1:], ys)
    return [xs[0]] + union2(xs[1:], ys)

# 3ª solución
# ===========

def union3(xs: list[A], ys: list[A]) -> list[A]:
    zs = ys[:]
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs

# 4ª solución
# ===========

def union4(xs: list[A], ys: list[A]) -> list[A]:
    return list(set(xs) | set(ys))

# Comprobación de equivalencia
# ============================
#
# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_union(xs, ys):
    xs1 = list(set(xs))
    ys1 = list(set(ys))
    assert sorted(union1(xs1, ys1)) ==\
           sorted(union2(xs1, ys1)) ==\
           sorted(union3(xs1, ys1)) ==\
           sorted(union4(xs1, ys1))

# La comprobación es
#    src> poetry run pytest -q union_conjuntista_de_listas.py
#    1 passed in 0.36s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('union1(list(range(0,30000,2)), list(range(1,30000,2)))')
#    1.30 segundos
#    >>> tiempo('union2(list(range(0,30000,2)), list(range(1,30000,2)))')
#    2.84 segundos
#    >>> tiempo('union3(list(range(0,30000,2)), list(range(1,30000,2)))')
#    1.45 segundos
#    >>> tiempo('union4(list(range(0,30000,2)), list(range(1,30000,2)))')
#    0.00 segundos

# Comprobación de la propiedad
# ============================

# iguales(xs, ys) se verifica si xs e ys son iguales como conjuntos. Por
# ejemplo,
#    iguales([3,2,3], [2,3])    ==  True
#    iguales([3,2,3], [2,3,2])  ==  True
#    iguales([3,2,3], [2,3,4])  ==  False
#    iguales([2,3], [4,5])      ==  False
def iguales(xs: list[A], ys: list[A]) -> bool:
    return set(xs) == set(ys)

# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_union_conmutativa(xs, ys):
    xs1 = list(set(xs))
    ys1 = list(set(ys))
    assert iguales(union1(xs1, ys1), union1(ys1, xs1))

# La comprobación es
#    src> poetry run pytest -q union_conjuntista_de_listas.py
#    2 passed in 0.49s
