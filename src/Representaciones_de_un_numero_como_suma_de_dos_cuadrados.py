# Representaciones_de_un_numero_como_suma_de_dos_cuadrados.py
# Representaciones de un número como suma de dos cuadrados.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-enero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    representaciones : (int) -> list[tuple[int, int]]
# tal que representaciones(n) es la lista de pares de números
# naturales (x,y) tales que n = x^2 + y^2. Por ejemplo.
#    representaciones(20)          ==  [(2,4)]
#    representaciones(25)          ==  [(0,5),(3,4)]
#    representaciones(325)         ==  [(1,18),(6,17),(10,15)]
#    len(representaciones(10**14)) == 8
#
# Comprobar con Hypothesis que un número natural n se puede representar
# como suma de dos cuadrados si, y sólo si, en la factorización prima
# de n todos los exponentes de sus factores primos congruentes con 3
# módulo 4 son pares.
# ---------------------------------------------------------------------

from math import floor, sqrt
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy import factorint

# 1ª solución
# ===========

def representaciones1(n: int) -> list[tuple[int, int]]:
    return [(x,y) for x in range(n+1) for y in range(x,n+1) if n == x*x + y*y]

# 2ª solución
# ===========

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

# 3ª solución
# ===========

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
    assert representaciones1(20) == [(2,4)]
    assert representaciones1(25) == [(0,5),(3,4)]
    assert representaciones1(325) == [(1,18),(6,17),(10,15)]
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
    xs = representaciones1(x)
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
#    >>> tiempo('representaciones1(5000)')
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

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_representaciones_prop(n: int) -> None:
    factores = factorint(n)
    assert (len(representaciones2(n)) > 0) == \
        all(p % 4 != 3 or e % 2 == 0 for p, e in factores.items())

# La comprobación es
#    >>> test_representaciones_prop()
#    >>>
