# Cuadrado_mas_cercano.py
# Cuadrado más cercano.
# José A. Alonso Jiménez
# Sevilla, 9-febrero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    cuadradoCercano : (int) -> int
# tal que cuadradoCercano(n) es el número cuadrado más cercano a n,
# donde n es un entero positivo. Por ejemplo,
#    cuadradoCercano(2)     == 1
#    cuadradoCercano(6)     == 4
#    cuadradoCercano(8)     == 9
#    cuadradoCercano(10^46) == 10000000000000000000000000000000000000000000000
# ---------------------------------------------------------------------

from itertools import count, takewhile
from math import sqrt
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

# raizEntera(x) es el mayor entero cuyo cuadrado no es mayor que
# x. Por ejemplo,
#    raizEntera(8)   ==  2
#    raizEntera(9)   ==  3
#    raizEntera(10)  ==  3
def raizEntera1(x: int) -> int:
    return list(takewhile(lambda n: n**2 <= x, count(1)))[-1]

def cuadradoCercano1(n: int) -> int:
    a = raizEntera1(n)
    b = a**2
    c = (a+1)**2
    if n - b < c - n:
        return b
    return c

# 2ª solución
# ===========

def raizEntera2(x: int) -> int:
    def aux(a: int, b: int) -> int:
        c = (a+b) // 2
        d = c**2
        if d == x:
            return c
        if c == a:
            return c
        if x <= d:
            return aux(a,c)
        return aux(c,b)
    return aux(1,x)

def cuadradoCercano2(n: int) -> int:
    a = raizEntera2(n)
    b = a**2
    c = (a+1)**2
    if n - b < c - n:
        return b
    return c

# 3ª solución
# ===========

def raizEntera3(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = n
    while x * x > n:
        x = (x + n // x) // 2
    return x

def cuadradoCercano3(n: int) -> int:
    a = raizEntera3(n)
    b = a**2
    c = (a+1)**2
    if n - b < c - n:
        return b
    return c

# 4ª solución
# ===========

def cuadradoCercano4(n: int) -> int:
    return round(sqrt(n)) ** 2

# La 4ª solución es incorrecta. Por ejemplo,
#    >>> cuadradoCercano4(10**46)
#    9999999999999998322278400000000070368744177664
#    >>> cuadradoCercano3(10**46)
#    10000000000000000000000000000000000000000000000

# Verificación
# ============

def test_cuadradoCercano() -> None:
    for cuadradoCercano in [cuadradoCercano1, cuadradoCercano2,
                            cuadradoCercano3, cuadradoCercano4]:
        assert cuadradoCercano(2) == 1
        assert cuadradoCercano(6) == 4
        assert cuadradoCercano(8) == 9
    print("Verificado")

# La verificación es
#    >>> test_cuadradoCercano()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_cuadradoCercano_equiv(x: int) -> None:
    r = cuadradoCercano1(x)
    assert cuadradoCercano2(x) == r
    assert cuadradoCercano3(x) == r
    assert cuadradoCercano4(x) == r

# La comprobación es
#    >>> test_cuadradoCercano_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('cuadradoCercano1(10**14)')
#    2.88 segundos
#    >>> tiempo('cuadradoCercano2(10**14)')
#    0.00 segundos
#    >>> tiempo('cuadradoCercano3(10**14)')
#    0.00 segundos
#
#    >>> tiempo('cuadradoCercano2(10**6000)')
#    1.21 segundos
#    >>> tiempo('cuadradoCercano3(10**6000)')
#    2.08 segundos
