# Descomposiciones_triangulares.py
# Descomposiciones triangulares
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-mayo-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los números triangulares se forman como sigue
#
#    *     *      *
#         * *    * *
#               * * *
#    1     3      6
#
# La sucesión de los números triangulares se obtiene sumando los
# números naturales. Así, los 5 primeros números triangulares son
#     1 = 1
#     3 = 1 + 2
#     6 = 1 + 2 + 3
#    10 = 1 + 2 + 3 + 4
#    15 = 1 + 2 + 3 + 4 + 5
#
# Definir la función
#    descomposicionesTriangulares :: Int -> [(Int, Int, Int)]
# tal que (descomposicionesTriangulares n) es la lista de las
# ternas correspondientes a las descomposiciones de n en tres sumandos,
# como máximo, formados por números triangulares. Por ejemplo,
#    >>> descomposicionesTriangulares4(4)
#    []
#    >>> descomposicionesTriangulares4(5)
#    [(1,1,3)]
#    >>> descomposicionesTriangulares4(12)
#    [(1,1,10),(3,3,6)]
#    >>> descomposicionesTriangulares4(30)
#    [(1,1,28),(3,6,21),(10,10,10)]
#    >>> descomposicionesTriangulares4(61)
#    [(1,15,45),(3,3,55),(6,10,45),(10,15,36)]
#    >>> descomposicionesTriangulares4(52)
#    [(1,6,45),(1,15,36),(3,21,28),(6,10,36),(10,21,21)]
#    >>> descomposicionesTriangulares4(82)
#    [(1,3,78),(1,15,66),(1,36,45),(6,10,66),(6,21,55),(10,36,36)]
#    >>> len(descomposicionesTriangulares4(5*10**5))
#    124
# ---------------------------------------------------------------------

from itertools import count, dropwhile, takewhile
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

# triangular(n) es el n-ésimo número triangular. Por ejemplo,
#    triangular(9) == 45
def triangular(n: int) -> int:
    if n == 1:
        return 1
    return triangular(n-1) + n

# triangulares1() es la lista de los números triangulares. Por ejemplo,
#    >>> from itertools import islice
#    >>> list(islice(triangulares1(), 10))
#    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
def triangulares1() -> Iterator[int]:
    return (triangular(n) for n in count(1))

def descomposicionesTriangulares1(n: int) -> list[tuple[int, int, int]]:
    xs = list(takewhile(lambda x : x <= n, triangulares1()))
    return [(x,y,z) for x in xs for y in xs for z in xs if
            x <= y <= z and x + y + z == n]

# 2ª solución
# ===========

def triangulares2() -> Iterator[int]:
    return ((n*(n+1)) // 2 for n in count(1))

def descomposicionesTriangulares2(n: int) -> list[tuple[int, int, int]]:
    xs = list(takewhile(lambda x : x <= n, triangulares2()))
    return [(x,y,z) for x in xs for y in xs for z in xs if
            x <= y <= z and x + y + z == n]

# 3ª solución
# ===========

def descomposicionesTriangulares3(n: int) -> list[tuple[int, int, int]]:
    xs = list(takewhile(lambda x : x <= n, triangulares2()))
    return [(x,y,z)
            for x in xs
            for y in xs
            if x <= y
            for z in xs
            if y <= z
            if x + y + z == n]

# 4ª solución
# ===========

def descomposicionesTriangulares4(n: int) -> list[tuple[int, int, int]]:
    xs = list(takewhile(lambda x : x <= n, triangulares2()))
    ts = []
    for x in xs:
        for y in xs:
            if x <= y:
                z = n - x - y
                if y <= z and z in xs:
                    ts.append((x, y, z))
    return ts

# 5ª solución
# ===========

def descomposicionesTriangulares5(n: int) -> list[tuple[int, int, int]]:
    xs = list(takewhile(lambda a : a <= n, triangulares2()))
    ts = []
    for x in xs:
        ys = list(dropwhile(lambda y: y < x, xs))
        for y in ys:
            z = n - x - y
            if y <= z and z in xs:
                ts.append((x, y, z))
    return ts

# Verificación
# ============

def test_descomposicionesTriangulares() -> None:
    for descomposicionesTriangulares in [descomposicionesTriangulares1,
                                         descomposicionesTriangulares2,
                                         descomposicionesTriangulares3,
                                         descomposicionesTriangulares4,
                                         descomposicionesTriangulares5]:
        assert descomposicionesTriangulares(4) ==\
            []
        assert descomposicionesTriangulares(5) ==\
            [(1,1,3)]
        assert descomposicionesTriangulares(12) ==\
            [(1,1,10),(3,3,6)]
        assert descomposicionesTriangulares(30) ==\
            [(1,1,28),(3,6,21),(10,10,10)]
        assert descomposicionesTriangulares(61) ==\
            [(1,15,45),(3,3,55),(6,10,45),(10,15,36)]
        assert descomposicionesTriangulares(52) ==\
            [(1,6,45),(1,15,36),(3,21,28),(6,10,36),(10,21,21)]
        assert descomposicionesTriangulares(82) ==\
            [(1,3,78),(1,15,66),(1,36,45),(6,10,66),(6,21,55),(10,36,36)]
    print("Verificado")

# La verificación es
#    >>> test_descomposicionesTriangulares()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_descomposicionesTriangulares_equiv(n: int) -> None:
    r = descomposicionesTriangulares1(n)
    assert descomposicionesTriangulares2(n) == r
    assert descomposicionesTriangulares3(n) == r
    assert descomposicionesTriangulares4(n) == r

# La comprobación es
#    >>> test_descomposicionesTriangulares_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('descomposicionesTriangulares1(6*10**4)[-1]')
#    2.16 segundos
#    >>> tiempo('descomposicionesTriangulares2(6*10**4)[-1]')
#    2.05 segundos
#    >>> tiempo('descomposicionesTriangulares3(6*10**4)[-1]')
#    1.04 segundos
#    >>> tiempo('descomposicionesTriangulares4(6*10**4)[-1]')
#    0.10 segundos
