# Iguales_al_siguiente.py
# Iguales al siguiente.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 21-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    igualesAlSiguiente : (list[A]) -> list[A]
# tal que igualesAlSiguiente(xs) es la lista de los elementos de xs
# que son iguales a su siguiente. Por ejemplo,
#    >>> igualesAlSiguiente([1, 2, 2, 2, 3, 3, 4])
#    [2, 2, 3]
#    >>> igualesAlSiguiente(list(range(10)))
#    []
# ---------------------------------------------------------------------

from itertools import chain, groupby
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**9)
A = TypeVar('A')

# 1ª solución
# ===========

# consecutivos1(xs) es la lista de pares de elementos consecutivos en
# xs. Por ejemplo,
#    >>> consecutivos1([3,5,2,7])
#    [(3, 5), (5, 2), (2, 7)]
def consecutivos1(xs: list[A]) -> list[tuple[A, A]]:
    return list(zip(xs, xs[1:]))

def igualesAlSiguiente1(xs: list[A]) -> list[A]:
    return [x for x, y in consecutivos1(xs) if x == y]

# 2ª solución
# ===========

# consecutivos2(xs) es la lista de pares de elementos consecutivos en
# xs. Por ejemplo,
#    >>> consecutivos2([3, 5, 2, 7])
#    [(3, 5), (5, 2), (2, 7)]
def consecutivos2(xs: list[A]) -> list[tuple[A, A]]:
    ys = []
    for i in range(len(xs) - 1):
        ys.append((xs[i], xs[i+1]))
    return ys

def igualesAlSiguiente2(xs: list[A]) -> list[A]:
    return [x for x, y in consecutivos2(xs) if x == y]

# 3ª solución
# ===========

def igualesAlSiguiente3(xs: list[A]) -> list[A]:
    ys = []
    i = 0
    while i < len(xs) - 1:
        if xs[i] == xs[i+1]:
            ys.append(xs[i])
        i += 1
    return ys

# 4ª solución
# ===========

def igualesAlSiguiente4(xs: list[A]) -> list[A]:
    return list(chain.from_iterable(list(ys)[1:] for _, ys in groupby(xs)))

# 5ª solución
# ===========

def igualesAlSiguiente5(xs: list[A]) -> list[A]:
    def aux(us: list[A], vs: list[A]) -> list[A]:
        if us and vs:
            if us[0] == vs[0]:
                return [us[0]] + aux(us[1:], vs[1:])
            return aux(us[1:], vs[1:])
        return []
    return aux(xs, xs[1:])

# Verificación
# ============

def test_igualesAlSiguiente() -> None:
    for igualesAlSiguiente in [igualesAlSiguiente1, igualesAlSiguiente2,
                               igualesAlSiguiente3, igualesAlSiguiente4,
                               igualesAlSiguiente5]:
        assert igualesAlSiguiente([1, 2, 2, 2, 3, 3, 4]) == [2, 2, 3]
        assert igualesAlSiguiente(list(range(10))) == []
        print(f"Verificado {igualesAlSiguiente.__name__}")

# La verificación es
#    >>> test_igualesAlSiguiente()
#    Verificado igualesAlSiguiente1
#    Verificado igualesAlSiguiente2
#    Verificado igualesAlSiguiente3
#    Verificado igualesAlSiguiente4
#    Verificado igualesAlSiguiente5

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.lists(st.integers()))
def test_igualesAlSiguiente_equiv(xs: list[int]) -> None:
    r = igualesAlSiguiente1(xs)
    assert igualesAlSiguiente2(xs) == r
    assert igualesAlSiguiente3(xs) == r
    assert igualesAlSiguiente4(xs) == r
    assert igualesAlSiguiente5(xs) == r

# La comprobación es
#    >>> test_igualesAlSiguiente_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    > ej = ''.join(map(str, range(10**6)))
#    >>> ej = ''.join(map(str, range(10**6)))
#    >>> tiempo('igualesAlSiguiente1(ej)')
#    0.69 segundos
#    >>> tiempo('igualesAlSiguiente2(ej)')
#    1.23 segundos
#    >>> tiempo('igualesAlSiguiente3(ej)')
#    1.09 segundos
#    >>> tiempo('igualesAlSiguiente4(ej)')
#    1.49 segundos
