# Representacion_de_Zeckendorf.hs
# Representacion_de_Zeckendorf.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-junio-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los primeros números de Fibonacci son
#    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
# tales que los dos primeros son iguales a 1 y los siguientes se
# obtienen sumando los dos anteriores.
#
# El [teorema de Zeckendorf](https://bit.ly/3k5NNt1) establece que todo
# entero positivo n se puede representar, de manera única, como la suma
# de números de Fibonacci no consecutivos decrecientes. Dicha suma se
# llama la representación de Zeckendorf de n. Por ejemplo, la
# representación de Zeckendorf de 100 es
#    100 = 89 + 8 + 3
# Hay otras formas de representar 100 como sumas de números de
# Fibonacci; por ejemplo,
#    100 = 89 +  8 + 2 + 1
#    100 = 55 + 34 + 8 + 3
# pero no son representaciones de Zeckendorf porque 1 y 2 son números
# de Fibonacci consecutivos, al igual que 34 y 55.
#
# Definir la función
#    zeckendorf : (int) -> list[int]
# tal que zeckendorf(n) es la representación de Zeckendorf de n. Por
# ejemplo,
#    >>> zeckendorf1(100)
#    [89, 8, 3]
#    >>> zeckendorf1(200)
#    [144, 55, 1]
#    >>> zeckendorf1(300)
#    [233, 55, 8, 3, 1]

#    length (zeckendorf (10^50000)) == 66097
# ---------------------------------------------------------------------

from itertools import combinations, dropwhile, islice, takewhile
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

# fibs() es la la sucesión de los números de Fibonacci. Por ejemplo,
#    >>> list(islice(fibs(), 14))
#    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
def fibs() -> Iterator[int]:
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# siguienteFibonacci(n) es el menor número de Fibonacci mayor que
# n. Por ejemplo,
#    siguienteFibonacci(34)  ==  55
def siguienteFibonacci(n: int) -> int:
    return  next(dropwhile(lambda x: x <= n, fibs()))

# sinFibonacciConsecutivos(xs) se verifica si en la sucesión
# decreciente de número de Fibonacci xs no hay dos consecutivos. Por
# ejemplo,
#    sinFibonacciConsecutivos([89, 8, 3])      ==  True
#    sinFibonacciConsecutivos([55, 34, 8, 3])  ==  False
def sinFibonacciConsecutivos(xs: list[int]) -> bool:
    return all(x != siguienteFibonacci(y) for x, y in zip(xs, xs[1:]))

def zeckendorf1Aux(n: int) -> list[list[int]]:
    fs = list(reversed(list(takewhile(lambda x: x <= n,fibs()))))
    return [list(xs)
            for i in range(len(fs) + 1)
            for xs in combinations(fs, i)
            if sum(xs) == n and sinFibonacciConsecutivos(list(xs))]

def zeckendorf1(n: int) -> list[int]:
    return zeckendorf1Aux(n)[0]

# 2ª solución
# ===========

def zeckendorf2(n: int) -> list[int]:
    if n == 0:
        return []
    x = list(takewhile(lambda x: x <= n, fibs()))[-1]
    return [x] + zeckendorf2(n - x)

# 3ª solución
# ===========

def zeckendorf3(n: int) -> list[int]:
    def aux(m: int, ys: list[int]) -> list[int]:
        if m == 0:
            return []
        x, *xs = ys
        return [x] + aux(m - x, list(dropwhile(lambda z: z > m - x, xs)))
    return aux(n, list(reversed(list(takewhile(lambda z: z <= n, fibs())))))

# zeckendorf4 n = aux n (reverse (takeWhile (<= n) fibs))
#   where aux 0 _      = []
#         aux m (x:xs) = x : aux (m-x) (dropWhile (>m-x) xs)

# Verificación
# ============

def test_zeckendorf() -> None:
    for zeckendorf in [zeckendorf1,
                       zeckendorf2,
                       zeckendorf3]:
        assert zeckendorf(100) == [89,8,3]
        assert zeckendorf(200) == [144,55,1]
        assert zeckendorf(300) == [233,55,8,3,1]
    print("Verificado")

# La verificación es
#    >>> test_zeckendorf()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_zeckendorf_equiv(n: int) -> None:
    r = zeckendorf1(n)
    assert zeckendorf2(n) == r
    assert zeckendorf3(n) == r

# La comprobación es
#    >>> test_zeckendorf_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('zeckendorf1(7*10**4)')
#    2.86 segundos
#    >>> tiempo('zeckendorf2(7*10**4)')
#    0.00 segundos
#    >>> tiempo('zeckendorf3(7*10**4)')
#    0.00 segundos
#
#    >>> tiempo('zeckendorf2(10**3000)')
#    6.17 segundos
#    >>> tiempo('zeckendorf3(10**3000)')
#    0.64 segundos

# ---------------------------------------------------------------------
# § Referencias                                                      --
# ---------------------------------------------------------------------

# Este ejercicio se basa en el problema
# [Zeckendorf representation](http://bit.ly/VB4yz6)
# de [Programming Praxis](http://programmingpraxis.com).
#
# La representación de Zeckendorf se describe en el artículo de la
# Wikipedia [Zeckendorf's theorem](http://bit.ly/VB2pU3).
