# Conjunto_de_divisores.py
# Conjunto de divisores.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-junio-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    divisores : (int) -> list[int]
# tal que divisores(x) es el conjunto de divisores de los x. Por
# ejemplo,
#    divisores(30) ==  [1,2,3,5,6,10,15,30]
#    len(divisores5(producto(range(1, 11))))  ==  270
#    len(divisores5(producto(range(1, 26)))) == 340032
# ---------------------------------------------------------------------

from functools import reduce
from itertools import combinations, groupby
from itertools import product as cartesian_product
from operator import mul
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy import divisors, factorint

# 1ª solución
# ===========

def divisores1(n: int) -> list[int]:
    return [x for x in range(1, n+1) if n % x == 0]

# 2ª solución
# ===========

def divisores2(n: int) -> list[int]:
    return list(filter(lambda i: n % i == 0, range(1, n + 1)))

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

# producto(xs) es el producto de los elementos de xs. Por ejemplo,
#    producto([2, 3, 5])  ==  30
def producto(xs: list[int]) -> int:
    return reduce(mul, xs, 1)

def divisores3(n: int) -> list[int]:
    return sorted(set(map(producto,
                          subsequences(primeFactors(n)))))

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

def divisores4(n: int) -> list[int]:
    factores = primeFactors(n)
    factoresAgrupados = [list(g) for k, g in groupby(factores)]
    return sorted({producto(concat(xss))
                   for xss in productoCartesiano(list(map(inits,
                                                          factoresAgrupados)))})

# 5ª solución
# ===========

def divisores5(n: int) -> list[int]:
    return divisors(n)

# Verificación
# ============

def test_divisores() -> None:
    for divisores in [divisores1,
                      divisores2,
                      divisores3,
                      divisores4,
                      divisores5]:
        assert divisores(30) == [1,2,3,5,6,10,15,30]
    print("Verificado")

# La verificación es
#    >>> test_divisores()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_divisores_equiv(n: int) -> None:
    r = divisores1(n)
    assert divisores2(n) == r
    assert divisores3(n) == r
    assert divisores4(n) == r
    assert divisores5(n) == r

# La comprobación es
#    >>> test_divisores_equiv()
#    >>>

# Comparación de la eficiencia
# ============================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('len(divisores1(producto(range(1, 12))))')
#    1.95 segundos
#    >>> tiempo('len(divisores2(producto(range(1, 12))))')
#    3.20 segundos
#    >>> tiempo('len(divisores3(producto(range(1, 12))))')
#    0.04 segundos
#    >>> tiempo('len(divisores4(producto(range(1, 12))))')
#    0.00 segundos
#    >>> tiempo('len(divisores5(producto(range(1, 12))))')
#    0.00 segundos
#
#    >>> tiempo('len(divisores3(producto(range(1, 15))))')
#    2.50 segundos
#    >>> tiempo('len(divisores4(producto(range(1, 15))))')
#    0.00 segundos
#    >>> tiempo('len(divisores5(producto(range(1, 15))))')
#    0.00 segundos
#
#    >>> tiempo('len(divisores4(producto(range(1, 30))))')
#    5.10 segundos
#    >>> tiempo('len(divisores5(producto(range(1, 30))))')
#    0.91 segundos
