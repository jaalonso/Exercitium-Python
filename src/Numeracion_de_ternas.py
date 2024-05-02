# Numeracion_de_ternas.py
# Numeración de las ternas de números naturales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-abril-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las ternas de números naturales se pueden ordenar como sigue
#    (0,0,0),
#    (0,0,1),(0,1,0),(1,0,0),
#    (0,0,2),(0,1,1),(0,2,0),(1,0,1),(1,1,0),(2,0,0),
#    (0,0,3),(0,1,2),(0,2,1),(0,3,0),(1,0,2),(1,1,1),(1,2,0),(2,0,1),...
#    ...
#
# Definir la función
#    posicion :: (Int,Int,Int) -> Int
# tal que (posicion (x,y,z)) es la posición de la terna de números
# naturales (x,y,z) en la ordenación anterior. Por ejemplo,
#    posicion (0,1,0)  ==  2
#    posicion (0,0,2)  ==  4
#    posicion (0,1,1)  ==  5
#
# Comprobar con QuickCheck que
# + la posición de (x,0,0) es x(x²+6x+11)/6
# + la posición de (0,y,0) es y(y²+3y+ 8)/6
# + la posición de (0,0,z) es z(z²+3z+ 2)/6
# + la posición de (x,x,x) es x(9x²+14x+7)/2
# ---------------------------------------------------------------------

from itertools import count, islice, takewhile
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

# ternas es la lista ordenada de las ternas de números naturales. Por ejemplo,
#    >>> list(islice(ternas(), 9))
#    [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,0,2),(0,1,1),(0,2,0),(1,0,1),(1,1,0)]
def ternas() -> Iterator[tuple[int, int, int]]:
    return ((x, y, n-x-y)
            for n in count()
            for x in range(n+1)
            for y in range(n-x+1))

def posicion1(t: tuple[int,int,int]) -> int:
    r = 0
    for t1 in ternas():
        if t == t1:
            return r
        r = r + 1
    return -1

# 2ª solución
# ===========

def posicion2(t: tuple[int,int,int]) -> int:
    for (n,t1) in enumerate(ternas()):
        if t1 == t:
            return n
    return -1

# 3ª solución
# ===========

def posicion3(t: tuple[int,int,int]) -> int:
    return len(list(takewhile(lambda t1 : t1 != t, ternas())))

# Verificación
# ============

def test_posicion() -> None:
    assert list(islice(ternas(), 9)) == \
        [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,0,2),(0,1,1),(0,2,0),(1,0,1),(1,1,0)]
    for posicion in [posicion1, posicion2, posicion3]:
        assert posicion((0,1,0)) == 2
        assert posicion((0,0,2)) == 4
        assert posicion((0,1,1)) == 5
    print("Verificado")

# La verificación es
#    >>> test_posicion()
#    Verificado

# Equivalencia
# ============

@given(st.integers(min_value=1, max_value=10),
       st.integers(min_value=1, max_value=10),
       st.integers(min_value=1, max_value=10))
def test_posicion_equiv(x: int, y: int, z: int) -> None:
    r = posicion1((x, y, z))
    assert posicion2((x, y, z)) == r
    assert posicion3((x, y, z)) == r

# La comprobación es
#    >>> test_posicion_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('posicion1((147,46,116))')
#    0.72 segundos
#    >>> tiempo('posicion2((147,46,116))')
#    0.68 segundos
#    >>> tiempo('posicion3((147,46,116))')
#    0.93 segundos

# Propiedades
# ===========

# La 1ª propiedad es
@given(st.integers(min_value=1, max_value=100))
def prop_posicion1(x: int) -> None:
    assert posicion1((x,0,0)) == x * (x**2 + 6*x + 11) // 6

# Su comprobación es
#    >>> prop_posicion1()
#    >>>

# La 2ª propiedad es
@given(st.integers(min_value=1, max_value=100))
def prop_posicion2(y: int) -> None:
    assert posicion1((0,y,0)) == y * (y**2 + 3*y + 8) // 6

# Su comprobación es
#    >>> prop_posicion2()
#    >>>

# La 3ª propiedad es
@given(st.integers(min_value=1, max_value=100))
def prop_posicion3(z: int) -> None:
    assert posicion1((0,0,z)) == z * (z**2 + 3*z + 2) // 6

# Su comprobación es
#    >>> prop_posicion3()
#    >>>

# La 4ª propiedad es
@given(st.integers(min_value=1, max_value=10))
def prop_posicion4(x: int) -> None:
    assert posicion1((x,x,x)) == x * (9 * x**2 + 14 * x + 7) // 2

# Su comprobación es
#    >>> prop_posicion4()
#    >>>
