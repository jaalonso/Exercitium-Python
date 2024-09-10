# Numero_de_divisores.py
# Número de divisores.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-julio-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    numeroDivisores : (int) -> int
# tal que numeroDivisores(x) es el número de divisores de x. Por
# ejemplo,
#    numeroDivisores(12)  ==  6
#    numeroDivisores(25)  ==  3
#    len(str(numeroDivisores(prod(range(1, 1+3*10**4)))))  ==  1948
# ---------------------------------------------------------------------

from itertools import combinations, groupby
from itertools import product as cartesian_product
from math import prod
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy import divisor_count, divisors, factorint

# 1ª solución
# ===========

def numeroDivisores1(x: int) -> int:
    return len([y for y in range(1, x+1) if x % y == 0])

# 2ª solución
# ===========

# raizEntera(x) es el mayor número entero cuyo cuadrado es menor o
# igual que x. Por ejemplo,
#    raizEntera(3)  ==  1
#    raizEntera(4)  ==  2
#    raizEntera(5)  ==  2
#    raizEntera(8)  ==  2
#    raizEntera(9)  ==  3
def raizEntera(x: int) -> int:
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

# esCuadrado(x) se verifica si x es un cuadrado perfecto. Por ejemplo,
#    esCuadrado(9)  ==  True
#    esCuadrado(7)  ==  False
def esCuadrado (x: int) -> bool:
    return x == raizEntera(x) ** 2

def numeroDivisores2(x: int) -> int:
    if x == 1:
        return 1
    if esCuadrado(x):
        return 2 * len([y for y in range(1, 1+raizEntera(x)) if x % y == 0]) - 1
    return 2 * len([y for y in range(1, 1+raizEntera(x)) if x % y == 0])

# 3ª solución
# ===========

# primeFactors(n) es la lista de los factores primos de n. Por ejemplo,
#    >>> primeFactors(12)
#    [2, 2, 3]
def primeFactors(n: int) -> list[int]:
    return [a for a, b in factorint(n).items() for _ in range(b)]

# subsequences(xs) es la lista de las subsecuencias de xs; es decir, de
# las listas obtenidas eliminando algunos elementos de xs sin cambiar el
# orden de los elementos restantes. Por ejemplo,
#    >>> subsequences([1,2,3])
#    [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
def subsequences(xs: list[int]) -> list[list[int]]:
    return [list(ys)
            for i in range(len(xs) + 1)
            for ys in combinations(xs, i)]

# divisores3(n) es el conjunto de los divisores de n. Por ejemplo,
#    divisores3(30) ==  [1,2,3,5,6,10,15,30]
def divisores3(n: int) -> list[int]:
    return sorted(set(map(prod, subsequences(primeFactors(n)))))

def numeroDivisores3(n: int) -> int:
    return len(divisores3(n))

# 4ª solución
# ===========

# inits(xs) es la lista de los segmentos iniciales de xs. Por ejemplo,
#    >>> inits([3,2,5,2])
#    [[], [3], [3, 2], [3, 2, 5], [3, 2, 5, 2]]
def inits(xs: list[int]) -> list[list[int]]:
    return [xs[:i] for i in range(len(xs) + 1)]

# productoCartesiano(xss) es el producto cartesiano de los conjuntos
# xss. Por ejemplo,
#    >>> productoCartesiano([[[2, 2]], [[], [3]], [[], [5]]])
#    [[[2,2],[],[]],[[2,2],[],[5]],[[2,2],[3],[]],[[2,2],[3],[5]]]
def productoCartesiano(xss: list[list[list[int]]]) -> list[list[list[int]]]:
    return [list(t) for t in cartesian_product(*xss)]

# concat(xss) es la lista obtenida concatenando los elementos de
# xss. Por ejemplo,
#    >>> concat([[2], [1,3], [5,2]])
#    [2, 1, 3, 5, 2]
def concat(xss: list[list[int]]) -> list[int]:
    return sum(xss, [])

# divisores4(n) es el conjunto de los divisores de n. Por ejemplo,
#    divisores4(30) ==  [1,2,3,5,6,10,15,30]
def divisores4(n: int) -> list[int]:
    factores = primeFactors(n)
    factoresAgrupados = [list(g) for k, g in groupby(factores)]
    return sorted({prod(concat(xss))
                   for xss in productoCartesiano(list(map(inits,
                                                          factoresAgrupados)))})

def numeroDivisores4(n: int) -> int:
    return len(divisores4(n))

# 5ª solución
# ===========

def numeroDivisores5(n: int) -> int:
    factores = primeFactors(n)
    factoresAgrupados = [list(g) for k, g in groupby(factores)]
    return prod([1 + len(xs) for xs in factoresAgrupados])

# 6ª solución
# ===========

def numeroDivisores6(n: int) -> int:
    return len(divisors(n))

# 7ª solución
# ===========

def numeroDivisores7(n: int) -> int:
    return divisor_count(n)

# Verificación
# ============

def test_numeroDivisores() -> None:
    for numeroDivisores in [numeroDivisores1,
                            numeroDivisores2,
                            numeroDivisores3,
                            numeroDivisores4,
                            numeroDivisores5,
                            numeroDivisores6,
                            numeroDivisores7]:
        assert numeroDivisores(12)  ==  6
        assert numeroDivisores(25)  ==  3
    print("Verificado")

# La verificación es
#    >>> test_numeroDivisores()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_numeroDivisores_equiv(x: int) -> None:
    r = numeroDivisores1(x)
    assert numeroDivisores2(x) == r
    assert numeroDivisores3(x) == r
    assert numeroDivisores4(x) == r
    assert numeroDivisores5(x) == r
    assert numeroDivisores6(x) == r
    assert numeroDivisores7(x) == r

# La comprobación es
#    >>> test_numeroDivisores_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('numeroDivisores1(prod(range(1, 12)))')
#    2.02 segundos
#    >>> tiempo('numeroDivisores2(prod(range(1, 12)))')
#    0.00 segundos
#    >>> tiempo('numeroDivisores3(prod(range(1, 12)))')
#    0.06 segundos
#
#    >>> tiempo('numeroDivisores2(prod(range(1, 15)))')
#    0.06 segundos
#    >>> tiempo('numeroDivisores3(prod(range(1, 15)))')
#    1.52 segundos
#
#    >>> tiempo('numeroDivisores2(prod(range(1, 18)))')
#    1.56 segundos
#    >>> tiempo('numeroDivisores4(prod(range(1, 18)))')
#    0.04 segundos
#
#    >>> tiempo('numeroDivisores4(prod(range(1, 30)))')
#    4.29 segundos
#    >>> tiempo('numeroDivisores5(prod(range(1, 30)))')
#    0.00 segundos
#    >>> tiempo('numeroDivisores6(prod(range(1, 30)))')
#    0.96 segundos
#    >>> tiempo('numeroDivisores7(prod(range(1, 30)))')
#    0.00 segundos
#
#    >>> tiempo('numeroDivisores5(prod(range(1, 32)))')
#    0.00 segundos
#    >>> tiempo('numeroDivisores6(prod(range(1, 32)))')
#    2.79 segundos
#    >>> tiempo('numeroDivisores7(prod(range(1, 32)))')
#    0.00 segundos
#
#    >>> tiempo('numeroDivisores5(prod(range(1, 4*10**4)))')
#    4.91 segundos
#    >>> tiempo('numeroDivisores7(prod(range(1, 4*10**4)))')
#    4.88 segundos
