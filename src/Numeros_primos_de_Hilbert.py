# Numeros_primos_de_Hilbert.py
# Números primos de Hilbert.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-diciembre-23
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un [número de Hilbert](http://bit.ly/204SW1p) es un entero positivo
# de la forma 4n+1. Los primeros números de Hilbert son 1, 5, 9, 13,
# 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81,
# 85, 89, 93, 97, ...
#
# Un primo de Hilbert es un número de Hilbert n que no es divisible
# por ningún número de Hilbert menor que n (salvo el 1). Los primeros
# primos de Hilbert son 5, 9, 13, 17, 21, 29, 33, 37, 41, 49, 53, 57,
# 61, 69, 73, 77, 89, 93, 97, 101, 109, 113, 121, 129, 133, 137, 141,
# 149, 157, 161, 173, 177, 181, 193, 197, ...
#
# Definir la sucesión
#    primosH :: [Integer]
# tal que sus elementos son los primos de Hilbert. Por ejemplo,
#    >>> list(islice(primosH1(), 15))
#    [5, 9, 13, 17, 21, 29, 33, 37, 41, 49, 53, 57, 61, 69, 73]
#    >>> nth(primosH1(), 5000)
#    45761
# ---------------------------------------------------------------------

from itertools import count, islice, takewhile
from math import ceil, sqrt
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

# numerosH es la sucesión de los números de Hilbert. Por ejemplo,
#    >>> list(islice(numerosH(), 15))
#    [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57]
def numerosH() -> Iterator[int]:
    return count(1, 4)

# (divisoresH n) es la lista de los números de Hilbert que dividen a
# n. Por ejemplo,
#   divisoresH(117)  ==  [1,9,13,117]
#   divisoresH(21)   ==  [1,21]
def divisoresH(n: int) -> list[int]:
    return [x for x in takewhile(lambda x: x <= n, numerosH())
            if n % x == 0]

def primosH1() -> Iterator[int]:
    return (n for n in islice(numerosH(), 1, None)
            if divisoresH(n) == [1, n])

# 2ª solución
# ===========

def primosH2() -> Iterator[int]:
    def esPrimoH(n: int) -> bool:
        m = ceil(sqrt(n))
        def noDivideAn(x: int) -> bool:
            return n % x != 0
        return all(noDivideAn(x) for x in range(5, m+1, 4))
    return filter(esPrimoH, islice(numerosH(), 1, None))

# Verificación                                                     --
# ============

def test_primosH() -> None:
    assert list(islice(primosH1(), 15)) == \
        [5, 9, 13, 17, 21, 29, 33, 37, 41, 49, 53, 57, 61, 69, 73]
    assert list(islice(primosH2(), 15)) == \
        [5, 9, 13, 17, 21, 29, 33, 37, 41, 49, 53, 57, 61, 69, 73]
    print ("Verificado")

# La verificación es
#    >>> test_primosH()
#    Verificado

# Comprobación de equivalencia
# ============================

# nth(i, n) es el n-ésimo elemento del iterador i. Por ejemplo,
#    nth(primos(), 4) == 11
def nth(i: Iterator[int], n: int) -> int:
    return list(islice(i, n, n+1))[0]

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_primosH_equiv(n: int) -> None:
    assert nth(primosH1(), n) == nth(primosH2(), n)

# La comprobación es
#    >>> test_primosH_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('nth(primosH1(), 3000)')
#    2.51 segundos
#    >>> tiempo('nth(primosH2(), 3000)')
#    0.05 segundos
