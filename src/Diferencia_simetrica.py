# Diferencia_simetrica.py
# Diferencia simétrica.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-mayo-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# La [diferencia simétrica](http://bit.ly/1Rdcqxs) de dos conjuntos es
# el conjunto cuyos elementos son aquellos que pertenecen a alguno de
# los conjuntos iniciales, sin pertenecer a ambos a la vez. Por
# ejemplo, la diferencia simétrica de {2,5,3} y {4,2,3,7} es {5,4,7}.
#
# Definir la función
#    diferenciaSimetrica :: Ord a => [a] -> [a] -> [a]
# tal que (diferenciaSimetrica xs ys) es la diferencia simétrica de xs
# e ys. Por ejemplo,
#    diferenciaSimetrica [2,5,3] [4,2,3,7]    ==  [4,5,7]
#    diferenciaSimetrica [2,5,3] [5,2,3]      ==  []
#    diferenciaSimetrica [2,5,2] [4,2,3,7]    ==  [3,4,5,7]
#    diferenciaSimetrica [2,5,2] [4,2,4,7]    ==  [4,5,7]
#    diferenciaSimetrica [2,5,2,4] [4,2,4,7]  ==  [5,7]
# ---------------------------------------------------------------------

from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A')

# 1ª solución
# ===========

def diferenciaSimetrica1(xs: list[A], ys: list[A]) -> list[A]:
    return list(set([x for x in xs if x not in ys] + \
                    [y for y in ys if y not in xs]))

# 2ª solución
# ===========

def diferenciaSimetrica2(xs: list[A], ys: list[A]) -> list[A]:
    return list(set(list(filter(lambda x: x not in ys, xs)) + \
                    list(filter(lambda y: y not in xs, ys))))

# 3ª solución
# ===========

def diferenciaSimetrica3(xs: list[A], ys: list[A]) -> list[A]:
    s1 = set(xs)
    s2 = set(ys)
    return list((s1 | s2) - (s1 & s2))

# 4ª solución
# ===========

def diferenciaSimetrica4(xs: list[A], ys: list[A]) -> list[A]:
    return [x for x in list(set(xs + ys)) if x not in xs or x not in ys]

# 5ª solución
# ===========

def diferenciaSimetrica5(xs: list[A], ys: list[A]) -> list[A]:
    return list(set(xs) ^ set(ys))

# Verificación
# ============

def test_diferenciaSimetrica() -> None:
    for diferenciaSimetrica in [diferenciaSimetrica1,
                                diferenciaSimetrica2,
                                diferenciaSimetrica3,
                                diferenciaSimetrica4,
                                diferenciaSimetrica5]:
        assert diferenciaSimetrica([2,5,3], [4,2,3,7])    ==  [4,5,7]
        assert diferenciaSimetrica([2,5,3], [5,2,3])      ==  []
        assert diferenciaSimetrica([2,5,2], [4,2,3,7])    ==  [3,4,5,7]
        assert diferenciaSimetrica([2,5,2], [4,2,4,7])    ==  [4,5,7]
        assert diferenciaSimetrica([2,5,2,4], [4,2,4,7])  ==  [5,7]
    print("Verificado")

# La verificación es
#    >>> test_diferenciaSimetrica()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_diferenciaSimetrica_equiv(xs: list[int], ys: list[int]) -> None:
    assert set(diferenciaSimetrica1(xs, ys)) ==\
           set(diferenciaSimetrica2(xs, ys)) ==\
           set(diferenciaSimetrica3(xs, ys)) ==\
           set(diferenciaSimetrica4(xs, ys)) ==\
           set(diferenciaSimetrica5(xs, ys))

# La comprobación es
#    >>> test_diferenciaSimetrica_equiv()
#    >>>

# Comparación de eficiencia
# =========================


def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('diferenciaSimetrica1(list(range(1,1+2*10**4)), list(range(2,1+2*10**4,2)))')
#    1.62 segundos
#    >>> tiempo('diferenciaSimetrica2(list(range(1,1+2*10**4)), list(range(2,1+2*10**4,2)))')
#    1.60 segundos
#    >>> tiempo('diferenciaSimetrica3(list(range(1,1+2*10**4)), list(range(2,1+2*10**4,2)))')
#    0.02 segundos
#    >>> tiempo('diferenciaSimetrica4(list(range(1,1+2*10**4)), list(range(2,1+2*10**4,2)))')
#    2.25 segundos
#    >>> tiempo('diferenciaSimetrica5(list(range(1,1+2*10**4)), list(range(2,1+2*10**4,2)))')
#    0.01 segundos
