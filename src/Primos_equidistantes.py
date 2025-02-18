# Primos_equidistantes.py
# Primos equidistantes.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-febrero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    primosEquidistantes : (int) -> list[tuple[int,int]]
# tal que primosEquidistantes(k) es la lista de los pares de primos
# cuya diferencia es k. Por ejemplo,
#    >>> list(islice(primosEquidistantes(2), 3))
#    [(3, 5), (5, 7), (11, 13)]
#    >>> list(islice(primosEquidistantes(4), 3))
#    [(7, 11), (13, 17), (19, 23)]
#    >>> list(islice(primosEquidistantes(6), 3))
#    [(23, 29), (31, 37), (47, 53)]
#    >>> list(islice(primosEquidistantes(8), 3))
#    [(89, 97), (359, 367), (389, 397)]
# ---------------------------------------------------------------------

from itertools import chain, count, islice, tee
from timeit import Timer, default_timer
from typing import Iterator

from sympy import isprime

# 1ª solución
# ===========

# primo(x) se verifica si x es primo. Por ejemplo,
#    primo(7)  ==  True
#    primo(8)  ==  False
def primo(x: int) -> bool:
    return [y for y in range(1,x+1) if x % y == 0] == [1,x]

# primos() es la lista de los números primos. Por ejemplo,
#    >>> list(islice(primos(), 10))
#    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def primos() -> Iterator[int]:
    return chain([2], (x for x in count(3, 2) if primo(x)))

def primosEquidistantes1(k: int) -> Iterator[tuple[int,int]]:
    a, b = tee(primos())
    next(b, None)
    return ((x,y) for (x,y) in zip(a, b) if y - x == k)

# 2ª solución
# ===========

def primos2() -> Iterator[int]:
    return (n for n in count() if isprime(n))

def primosEquidistantes2(k: int) -> Iterator[tuple[int,int]]:
    a, b = tee(primos2())
    next(b, None)
    return ((x,y) for (x,y) in zip(a, b) if y - x == k)

# Verificación
# ============

def test_primosEquidestantes() -> None:
    for primosEquidistantes in [primosEquidistantes1,
                                primosEquidistantes2]:
        assert list(islice(primosEquidistantes(2), 3)) == \
            [(3, 5), (5, 7), (11, 13)]
        assert list(islice(primosEquidistantes(4), 3)) == \
            [(7, 11), (13, 17), (19, 23)]
        assert list(islice(primosEquidistantes(6), 3)) == \
            [(23, 29), (31, 37), (47, 53)]
        assert list(islice(primosEquidistantes(8), 3)) == \
            [(89, 97), (359, 367), (389, 397)]
    print("Verificado")

# La verificación es
#    >>> test_primosEquidestantes()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
def primosEquidistantes_equiv(n: int, k: int) -> bool:
    return list(islice(primosEquidistantes1(k), n)) == \
           list(islice(primosEquidistantes2(k), n))

# La comprobación es
#    >>> primosEquidistantes_equiv(100, 4)
#    True

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('list(islice(primosEquidistantes1(4), 300))')
#    3.19 segundos
#    >>> tiempo('list(islice(primosEquidistantes2(4), 300))')
#    0.01 segundos
