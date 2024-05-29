# Conjunto_de_primos_relativos.py
# Conjunto de primos relativos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-marzo-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Dos números enteros positivos son [primos relativos](http://bit.ly/1xgqDTK)
# si no tienen ningún factor primo en común; es decir, si 1 es su único
# divisor común. Por ejemplo, 6 y 35 son primos entre sí, pero 6 y 27
# no lo son porque ambos son divisibles por 3.
#
# Definir la función
#    primosRelativos : (list[int]) -> bool
# tal que primosRelativos(xs) se verifica si los elementos de xs son
# primos relativos dos a dos. Por ejemplo,
#    primosRelativos([6,35])         ==  True
#    primosRelativos([6,27])         ==  False
#    primosRelativos([2,3,4])        ==  False
#    primosRelativos([6,35,11])      ==  True
#    primosRelativos([6,35,11,221])  ==  True
#    primosRelativos([6,35,11,231])  ==  False
# ---------------------------------------------------------------------

from math import gcd
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy.ntheory.generate import primerange

setrecursionlimit(10**6)

# 1ª solución
# ===========

# sonPrimosRelativos(x, y) se verifica si x e y son primos
# relativos. Por ejemplo,
#    sonPrimosRelativos(6, 35)  ==  True
#    sonPrimosRelativos(6, 27)  ==  False
def sonPrimosRelativos(x: int, y: int) -> bool:
    return gcd(x, y) == 1

def primosRelativos1(ys: list[int]) -> bool:
    if not ys:
        return True
    x, *xs = ys
    return all(sonPrimosRelativos(x, z) for z in xs) and primosRelativos1(xs)

# 2ª solución
# ===========

def primosRelativos2(ys: list[int]) -> bool:
    if not ys:
        return True
    for y in ys[1:]:
        if gcd(ys[0], y) != 1:
            return False
    return primosRelativos2(ys[1:])

# Verificación
# ============

def test_primosRelativos() -> None:
    for primosRelativos in [primosRelativos1,
                            primosRelativos2]:
        assert primosRelativos([6,35])
        assert not primosRelativos([6,27])
        assert not primosRelativos([2,3,4])
        assert primosRelativos([6,35,11])
        assert primosRelativos([6,35,11,221])
        assert not primosRelativos([6,35,11,231])
    print("Verificado")

# La verificación es
#    >>> test_primosRelativos()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers(min_value=1, max_value=1000)))
def test_primosRelativos_equiv(xs: list[int]) -> None:
    assert primosRelativos1(xs) == primosRelativos2(xs)

# La comprobación es
#    >>> test_primosRelativos_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('primosRelativos1(list(primerange(40000)))')
#    2.20 segundos
#    >>> tiempo('primosRelativos2(list(primerange(40000)))')
#    1.82 segundos
