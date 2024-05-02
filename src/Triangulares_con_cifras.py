# Triangulares_con_cifras.py
# Números triangulares con n cifras distintas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-mayo-2024
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
#    triangularesConCifras :: Int -> [Integer]
# tal que (triangularesConCifras n) es la lista de los números
# triangulares con n cifras distintas. Por  ejemplo,
#    take 6 (triangularesConCifras 1)   ==  [1,3,6,55,66,666]
#    take 6 (triangularesConCifras 2)   ==  [10,15,21,28,36,45]
#    take 6 (triangularesConCifras 3)   ==  [105,120,136,153,190,210]
#    take 5 (triangularesConCifras 4)   ==  [1035,1275,1326,1378,1485]
#    take 2 (triangularesConCifras 10)  ==  [1062489753,1239845706]
# ---------------------------------------------------------------------

from itertools import count, islice
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator

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
#    >>> list(islice(triangulares1(), 10))
#    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
def triangulares1() -> Iterator[int]:
    return (triangular(n) for n in count(1))

# nCifras(x) es el número de cifras distintas del número x. Por
# ejemplo,
#    nCifras(325275)  ==  4
def nCifras(x: int) -> int:
    return len(set(str(x)))

def triangularesConCifras1(n: int) -> Iterator[int]:
    return (x for x in triangulares1() if nCifras(x) == n)

# 2ª solución
# ===========

def triangulares2() -> Iterator[int]:
    return ((n*(n+1)) // 2 for n in count(1))

def triangularesConCifras2(n: int) -> Iterator[int]:
    return (x for x in triangulares2() if nCifras(x) == n)

# 3ª solución
# ===========

def triangulares3() -> Iterator[int]:
    x = 0
    for n in count(1):
        x += n
        yield x

def triangularesConCifras3(n: int) -> Iterator[int]:
    return (x for x in triangulares3() if nCifras(x) == n)

# Verificación
# ============

def test_triangularesConCifras() -> None:
    for triangularesConCifras in [triangularesConCifras1,
                                  triangularesConCifras2,
                                  triangularesConCifras3]:
        assert list(islice(triangularesConCifras(1), 6)) == \
            [1,3,6,55,66,666]
        assert list(islice(triangularesConCifras(2), 6)) == \
            [10,15,21,28,36,45]
        assert list(islice(triangularesConCifras(3), 6)) == \
            [105,120,136,153,190,210]
        assert list(islice(triangularesConCifras(4), 5)) == \
            [1035,1275,1326,1378,1485]
    print("Verificado")

# La verificación es
#    >>> test_triangularesConCifras()
#    Verificado

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('list(islice(triangularesConCifras1(3), 300))')
#    11.18 segundos
#    >>> tiempo('list(islice(triangularesConCifras2(3), 300))')
#    0.03 segundos
#    >>> tiempo('list(islice(triangularesConCifras3(3), 300))')
#    0.03 segundos
#
#    >>> tiempo('list(islice(triangularesConCifras2(3), 700))')
#    2.19 segundos
#    >>> tiempo('list(islice(triangularesConCifras3(3), 700))')
#    2.01 segundos
