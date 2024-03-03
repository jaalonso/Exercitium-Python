# Reiteracion_de_suma_de_consecutivos.py
# Reiteración de suma de consecutivos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-marzo-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# La reiteración de la suma de los elementos consecutivos de la lista
# [1,5,3] es 14 como se explica en el siguiente diagrama
#    1 + 5 = 6
#              \
#               ==> 14
#              /
#    5 + 3 = 8
# y la de la lista [1,5,3,4] es 29 como se explica en el siguiente
# diagrama
#    1 + 5 = 6
#              \
#               ==> 14
#              /       \
#    5 + 3 = 8          ==> 29
#              \       /
#               ==> 15
#              /
#    3 + 4 = 7
#
# Definir la función
#    sumaReiterada : (list[int]) -> int
# tal que sumaReiterada(xs) es la suma reiterada de los elementos
# consecutivos de la lista no vacía xs. Por ejemplo,
#    sumaReiterada([1,5,3])    ==  14
#    sumaReiterada([1,5,3,4])  ==  29
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A')
setrecursionlimit(10**6)

# 1ª solución
# ===========

# consecutivos(xs) es la lista de pares de elementos consecutivos de
# xs. Por ejemplo,
#    consecutivos([1,5,3,4])  ==  [(1,5),(5,3),(3,4)]
def consecutivos(xs: list[A]) -> list[tuple[A, A]]:
    return list(zip(xs, xs[1:]))

def sumaReiterada1(xs: list[int]) -> int:
    if len(xs) == 1:
        return xs[0]
    return sumaReiterada1([x + y for (x, y) in consecutivos(xs)])

# 2ª solución
# ===========

# sumaConsecutivos(xs) es la suma de los de pares de elementos
# consecutivos de xs. Por ejemplo,
#    sumaConsecutivos([1,5,3,4])   ==  [6,8,7]
def sumaConsecutivos(xs : list[int]) -> list[int]:
    return [x + y for (x, y) in list(zip(xs, xs[1:]))]

def sumaReiterada2(xs: list[int]) -> int:
    if len(xs) == 1:
        return xs[0]
    return sumaReiterada2(sumaConsecutivos(xs))

# 3ª solución
# ===========

def sumaReiterada3(xs: list[int]) -> int:
    if len(xs) == 1:
        return xs[0]
    return sumaReiterada3([x + y for (x, y) in list(zip(xs, xs[1:]))])

# Verificación
# ============

def test_sumaReiterada() -> None:
    for sumaReiterada in [sumaReiterada1, sumaReiterada2,
                          sumaReiterada3]:
        assert sumaReiterada([1,5,3]) == 14
        assert sumaReiterada([1,5,3,4]) == 29
    print("Verificado")

# La verificación es
#    >>> test_sumaReiterada()
#    Verificado

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.lists(st.integers(), min_size=1))
def test_sumaReiterada_equiv(xs: list[int]) -> None:
    r = sumaReiterada1(xs)
    assert sumaReiterada2(xs) == r
    assert sumaReiterada3(xs) == r

# La comprobación es
#    >>> test_sumaReiterada_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('sumaReiterada1(range(4000))')
#    2.18 segundos
#    >>> tiempo('sumaReiterada2(range(4000))')
#    1.90 segundos
#    >>> tiempo('sumaReiterada3(range(4000))')
#    1.97 segundos
