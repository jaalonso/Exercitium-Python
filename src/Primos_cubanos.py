# Primos_cubanos.py
# Primos cubanos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-febrero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un [primo cubano](http://bit.ly/1jPy5QZ) es un número primo que se
# puede escribir como diferencia de dos cubos consecutivos. Por
# ejemplo, el 61 es un primo cubano porque es primo y 61 = 5³-4³.
#
# Definir la sucesión
#    cubanos : () -> Iterator[int]
# tal que sus elementos son los números cubanos. Por ejemplo,
#    >>> list(islice(cubanos(), 15))
#    [7,19,37,61,127,271,331,397,547,631,919,1657,1801,1951,2269]
# ---------------------------------------------------------------------

from itertools import count, islice, tee
from timeit import Timer, default_timer
from typing import Iterator

from sympy import isprime

# 1ª solución
# ===========

# cubos() es la lista de los cubos. Por ejemplo,
#    >>> list(islice(cubos(), 10))
#    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
def cubos() -> Iterator[int]:
    return (x**3 for x in count(1))

# parejasDeCubos() es la lista de las parejas de cubos consecutivos. Por
# ejemplo,
#    >>> list(islice(parejasDeCubos(), 5))
#    [(1, 8), (8, 27), (27, 64), (64, 125), (125, 216)]
def parejasDeCubos() -> Iterator[tuple[int, int]]:
    a, b = tee(cubos())
    next(b, None)
    return zip(a, b)

# diferenciasDeCubos() es la lista de las diferencias de cubos
# consecutivos. Por ejemplo,
#    >>> list(islice(diferenciasDeCubos(), 5))
#    [7, 19, 37, 61, 91]
def diferenciasDeCubos() -> Iterator[int]:
    return (j - i for i, j in parejasDeCubos())

def cubanos1() -> Iterator[int]:
    return (x for x in diferenciasDeCubos() if isprime(x))

# 2ª solución
# ===========

def cubanos2() -> Iterator[int]:
    return ((x+1)**3 - x**3 for x in count(1) if isprime((x+1)**3 - x**3))

# 3ª solución
# ===========

def cubanos3() -> Iterator[int]:
    return (y for x in count(1) if isprime((y := (x+1)**3 - x**3)))

# 4ª solución
# ===========

def cubanos4() -> Iterator[int]:
    return (y for x in count(1) if isprime((y := 3*x**2 + 3*x + 1)))

# Verificación
# ============

def test_cubanos() -> None:
    for cubanos in [cubanos1, cubanos2, cubanos3, cubanos4]:
        assert list(islice(cubanos(), 15)) == \
            [7,19,37,61,127,271,331,397,547,631,919,1657,1801,1951,2269]
    print ("Verificado")

# La verificación es
#    >>> test_cubanos()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
def test_cubanos_equiv(n: int) -> None:
    r = list(islice(cubanos1(), n))
    assert list(islice(cubanos2(), n)) == r
    assert list(islice(cubanos3(), n)) == r
    assert list(islice(cubanos4(), n)) == r
    print("Verificado")

# La comprobación es
#    >>> test_cubanos_equiv(10000)
#    Verificado

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('list(islice(cubanos1(), 30000))')
#    1.54 segundos
#    >>> tiempo('list(islice(cubanos1(), 40000))')
#    2.20 segundos
#    >>> tiempo('list(islice(cubanos2(), 40000))')
#    2.22 segundos
#    >>> tiempo('list(islice(cubanos3(), 40000))')
#    2.19 segundos
#    >>> tiempo('list(islice(cubanos4(), 40000))')
#    2.15 segundos
