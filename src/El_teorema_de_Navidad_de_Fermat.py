# El_teorema_de_Navidad_de_Fermat.py
# El teorema de Navidad de Fermat.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-diciembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El 25 de diciembre de 1640, en una carta a Mersenne, Fermat demostró
# la conjetura de Girard: todo primo de la forma 4n+1 puede expresarse
# de manera única como suma de dos cuadrados. Por eso es conocido como
# el [teorema de Navidad de Fermat](http://bit.ly/2Roso1o).
#
# Definir las funciones
#    representaciones : (int) -> list[tuple[int, int]]
#    primosImparesConRepresentacionUnica : () -> Iterator[int]
#    primos4nM1 : () -> Iterator[int]
# tales que
# + representaciones(n) es la lista de pares de números naturales
#   (x,y) tales que n = x^2 + y^2 con x <= y. Por ejemplo.
#      representaciones(20)           ==  [(2,4)]
#      representaciones(25)           ==  [(0,5),(3,4)]
#      representaciones(325)          ==  [(1,18),(6,17),(10,15)]
#      representaciones(100000147984) ==  [(0,316228)]
#      length (representaciones (10^10))    ==  6
#      length (representaciones (4*10^12))  ==  7
# + primosImparesConRepresentacionUnica() genera los números primos
#   impares que se pueden escribir exactamente de una manera como suma
#   de cuadrados de pares de números naturales (x,y) con x <= y. Por
#   ejemplo,
#      >>> list(islice(primosImparesConRepresentacionUnica(), 20))
#      [5,13,17,29,37,41,53,61,73,89,97,101,109,113,137,149,157,173,181,193]
# + primos4nM1() genera los números primos que se pueden escribir  como
#   uno más un múltiplo de 4 (es decir, que son congruentes con 1 módulo
#   4). Por ejemplo,
#      >>> list(islice(primos4nM1(), 20))
#      [5,13,17,29,37,41,53,61,73,89,97,101,109,113,137,149,157,173,181,193]
#
# El teorema de Navidad de Fermat afirma que un número primo impar p se
# puede escribir exactamente de una manera como suma de dos cuadrados de
# números naturales p = x² + y² (con x <= y) si, y sólo si, p se puede
# escribir como uno más un múltiplo de 4 (es decir, que es congruente
# con 1 módulo 4).
#
# Comprobar con Hypothesis el teorema de Navidad de Fermat; es decir,
# que para todo número n, los n-ésimos elementos de
# primosImparesConRepresentacionUnica y de primos4nM1 son iguales.
# ----------------------------------------------------------------------

from itertools import count, islice
from math import floor, sqrt
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st
from sympy import isprime

# 1ª definición de representaciones
# =================================

def representaciones(n: int) -> list[tuple[int, int]]:
    return [(x,y) for x in range(n+1) for y in range(x,n+1) if n == x*x + y*y]

# 2ª definición de representaciones
# =================================

# raiz(x) es la raíz cuadrada entera de x. Por ejemplo,
#    raiz(25)     ==  5
#    raiz(24)     ==  4
#    raiz(26)     ==  5
#    raiz(10**46) == 100000000000000000000000
def raiz(x: int) -> int:
    def aux(a: int, b: int) -> int:
        c = (a+b) // 2
        d = c**2
        if d == x:
            return c
        if c == a:
            return a
        if d < x:
            return aux (c,b)
        return aux (a,c)
    if x == 0:
        return 0
    if x == 1:
        return 1
    return aux(0, x)

# Nota. La siguiente definición de raíz cuadrada entera falla para
# números grandes. Por ejemplo,
#    >>> raiz2(10**46)
#    99999999999999991611392
def raiz2(x: int) -> int:
    return floor(sqrt(x))

# esCuadrado(x) se verifica si x es un número al cuadrado. Por
# ejemplo,
#    esCuadrado(25)     == True
#    esCuadrado(26)     == False
#    esCuadrado(10**46) == True
#    esCuadrado(10**47) == False
def esCuadrado(x: int) -> bool:
    y = raiz(x)
    return x == y * y

def representaciones2(n: int) -> list[tuple[int, int]]:
    r: list[tuple[int, int]] = []
    for x in range(1 + raiz(n // 2)):
        z = n - x*x
        if esCuadrado(z):
            r.append((x, raiz(z)))
    return r

# 3ª definición de representaciones
# =================================

def representaciones3(n: int) -> list[tuple[int, int]]:
    r: list[tuple[int, int]] = []
    for x in range(1 + raiz(n // 2)):
        y = n - x*x
        z = raiz(y)
        if y == z * z:
            r.append((x, z))
    return r

# Verificación
# ============

def test_representaciones() -> None:
    assert representaciones(20) == [(2,4)]
    assert representaciones(25) == [(0,5),(3,4)]
    assert representaciones(325) == [(1,18),(6,17),(10,15)]
    assert representaciones2(20) == [(2,4)]
    assert representaciones2(25) == [(0,5),(3,4)]
    assert representaciones2(325) == [(1,18),(6,17),(10,15)]
    assert representaciones3(20) == [(2,4)]
    assert representaciones3(25) == [(0,5),(3,4)]
    assert representaciones3(325) == [(1,18),(6,17),(10,15)]
    print("Verificado")

# La comprobación es
#    >>> test_representaciones()
#    Verificado

# Equivalencia de las definiciones de representaciones
# ====================================================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_representaciones_equiv(x: int) -> None:
    xs = representaciones(x)
    assert representaciones2(x) == xs
    assert representaciones3(x) == xs

# La comprobación es
#    >>> test_representaciones_equiv()
#    >>>

# Comparación de eficiencia de las definiciones de representaciones
# =================================================================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('representaciones(5000)')
#    1.27 segundos
#    >>> tiempo('representaciones2(5000)')
#    0.00 segundos
#    >>> tiempo('representaciones3(5000)')
#    0.00 segundos
#
#    >>> tiempo('len(representaciones2(10**12))')
#    11.54 segundos
#    >>> tiempo('len(representaciones3(10**12))')
#    12.08 segundos

# Definición de primosImparesConRepresentacionUnica
# =================================================

# primos() genera la lista de los primos. Por ejemplo,
#    >>> list(islice(primos(), 10))
#    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def primos() -> Iterator[int]:
    return (n for n in count() if isprime(n))

def primosImparesConRepresentacionUnica() -> Iterator[int]:
    return (x for x in islice(primos(), 1, None)
            if len(representaciones2(x)) == 1)

# Verificación de primosImparesConRepresentacionUnica
# ===================================================

def test_primosImparesConRepresentacionUnica() -> None:
    assert list(islice(primosImparesConRepresentacionUnica(), 20)) == \
        [5,13,17,29,37,41,53,61,73,89,97,101,109,113,137,149,157,173,181,193]
    print("Verificado")

# La comprobación es
#    >>> test_primosImparesConRepresentacionUnica()
#    Verificado

# Definición de primos4nM1
# ========================

def primos4nM1() -> Iterator[int]:
    return (x for x in primos() if x % 4 == 1)

# La comprobación es
#    >>> test_primos4nM1()
#    Verificado

# Verificación de primos4nM1
# ==========================

def test_primos4nM1() -> None:
    assert list(islice(primos4nM1(), 20)) == \
        [5,13,17,29,37,41,53,61,73,89,97,101,109,113,137,149,157,173,181,193]
    print("Verificado")

# Teorema de Navidad de Fermat
# ============================

# nth(i, n) es el n-ésimo elemento del iterador i. Por ejemplo,
#    nth(primos(), 4) == 11
def nth(i: Iterator[int], n: int) -> int:
    return list(islice(i, n, n+1))[0]

# La propiedad es
@given(st.integers(min_value=1, max_value=300))
def test_teoremaDeNavidadDeFermat(n: int) -> None:
    assert nth(primosImparesConRepresentacionUnica(), n) == nth(primos4nM1(), n)

# La comprobación es
#    >>> test_teoremaDeNavidadDeFermat()
#    >>>
