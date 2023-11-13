# Raices_enteras.py
# Raíces enteras.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-noviembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    raizEnt :: Integer -> Integer -> Integer
# tal que (raizEnt x n) es la raíz entera n-ésima de x; es decir, el
# mayor número entero y tal que y^n <= x. Por ejemplo,
#    raizEnt(8, 3)      ==  2
#    raizEnt(9, 3)      ==  2
#    raizEnt(26, 3)     ==  2
#    raizEnt(27, 3)     ==  3
#    raizEnt(10**50, 2) ==  10000000000000000000000000
#
# Comprobar con QuickCheck que para todo número natural n,
#     raizEnt (10^(2*n)) 2 == 10^n
# ---------------------------------------------------------------------

from itertools import count, takewhile
from math import floor
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def raizEnt(x: int, n: int) -> int:
    return list(takewhile(lambda y : y ** n <= x, count(0)))[-1]

# 2ª solución
# ===========

def raizEnt2(x: int, n: int) -> int:
    return floor(x ** (1 / n))

# Nota. La solución anterior falla para números grandes. Por ejemplo,
#    >>> raizEnt2(10**50, 2) == 10 **25
#    False

# 3ª solución
# ===========

def raizEnt3(x: int, n: int) -> int:
    def aux(a: int, b: int) -> int:
        c = (a + b) // 2
        d = c ** n
        if d == x:
            return c
        if c == a:
            return c
        if d < x:
            return aux(c, b)
        return aux(a, c)
    return aux(1, x)

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('raizEnt(10**14, 2)')
#    2.71 segundos
#    >>> tiempo('raizEnt2(10**14, 2)')
#    0.00 segundos
#    >>> tiempo('raizEnt3(10**14, 2)')
#    0.00 segundos
#
#    >>> raizEnt2(10**50, 2)
#    10000000000000000905969664
#    >>> raizEnt3(10**50, 2)
#    10000000000000000000000000

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=1000))
def test_raizEntP(n: int) -> None:
    assert raizEnt3(10**(2*n), 2) == 10**n

# La comprobación es
#    >>> test_raizEnt)()
#    >>>

# Verificación
# ============

def test_raizEnt() -> None:
    assert raizEnt(8, 3) == 2
    assert raizEnt(9, 3) == 2
    assert raizEnt(26, 3) == 2
    assert raizEnt(27, 3) == 3
    assert raizEnt2(8, 3) == 2
    assert raizEnt2(9, 3) == 2
    assert raizEnt2(26, 3) == 2
    assert raizEnt2(27, 3) == 3
    assert raizEnt3(8, 3) == 2
    assert raizEnt3(9, 3) == 2
    assert raizEnt3(26, 3) == 2
    assert raizEnt3(27, 3) == 3
    print("Verificado")

# La comprobación es
#    >>> test_raizEnt()
#    Verificado
