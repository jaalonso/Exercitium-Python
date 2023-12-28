# Sumas_de_dos_primos.py
# Sumas de dos primos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-julio-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la sucesión
#    sumasDeDosPrimos :: [Integer]
# cuyos elementos son los números que se pueden escribir como suma de
# dos números primos. Por ejemplo,
#    >>> list(islice(sumasDeDosPrimos1(), 23))
#    [4,5,6,7,8,9,10,12,13,14,15,16,18,19,20,21,22,24,25,26,28,30,31]
#    λ> sumasDeDosPrimos !! (5*10^5)
#    862878
# ---------------------------------------------------------------------

from itertools import count, islice, takewhile
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st
from sympy import isprime

# 1ª solución
# ===========

# primos() genera la lista de los primos. Por ejemplo,
#    >>> list(islice(primos(), 10))
#    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def primos() -> Iterator[int]:
    return (n for n in count() if isprime(n))

# sumaDeDosPrimos1(n) es la lista de pares de primos cuya suma es
# n. Por ejemplo,
#    sumaDeDosPrimos1(9)   ==  [(2,7),(7,2)]
#    sumaDeDosPrimos1(16)  ==  [(3,13),(5,11),(11,5),(13,3)]
#    sumaDeDosPrimos1(17)  ==  []
def sumaDeDosPrimos1(n: int) -> list[tuple[int, int]]:
    primosN = takewhile(lambda x: x< n, primos())
    return [(x,n-x) for x in primosN if isprime(n-x)]

def sumasDeDosPrimos1() -> Iterator[int]:
    return (n for n in count(1) if sumaDeDosPrimos1(n))

# 2ª solución
# ===========

# sumasDeDosPrimos2(n) es la lista de pares (x,y) de primos cuya suma
# es n y tales que x <= y. Por ejemplo,
#    sumaDeDosPrimos2(9)   ==  [(2,7)]
#    sumaDeDosPrimos2(16)  ==  [(3,13),(5,11)]
#    sumaDeDosPrimos2(17)  ==  []
def sumaDeDosPrimos2(n: int) -> list[tuple[int, int]]:
    primosN = takewhile(lambda x : x <= n // 2, primos())
    return [(x,n-x) for x in primosN if isprime(n-x)]

def sumasDeDosPrimos2() -> Iterator[int]:
    return (n for n in count(1) if sumaDeDosPrimos2(n))

# 3ª solución
# ===========

# esSumaDeDosPrimos3(n) se verifica si n es suma de dos primos. Por
# ejemplo,
#    esSumaDeDosPrimos3(9)   ==  True
#    esSumaDeDosPrimos3(16)  ==  True
#    esSumaDeDosPrimos3(17)  ==  False
def esSumaDeDosPrimos3(n: int) -> bool:
    if n % 2 == 1:
        return isprime(n-2)
    return any(isprime(n-x)
               for x in takewhile(lambda x : x <= n // 2, primos()))

def sumasDeDosPrimos3() -> Iterator[int]:
    return filter(esSumaDeDosPrimos3, count(4))

# 4ª solución
# ===========

# Usando la conjetura de Goldbach que dice que "Todo número par mayor
# que 2 puede escribirse como suma de dos números primos" .

# esSumaDeDosPrimos4(n) se verifica si n es suma de dos primos. Por
# ejemplo,
#    esSumaDeDosPrimos4(9)   ==  True
#    esSumaDeDosPrimos4(16)  ==  True
#    esSumaDeDosPrimos4(17)  ==  False
def esSumaDeDosPrimos4(n: int) -> bool:
    return n % 2 == 0 or isprime(n-2)

def sumasDeDosPrimos4() -> Iterator[int]:
    return filter(esSumaDeDosPrimos4, count(4))

# Verificación                                                     --
# ============

# La propiedad es
def test_sumasDeDosPrimos() -> None:
    r = [4,5,6,7,8,9,10,12,13,14,15,16,18,19,20,21,22,24,25,26,28,30,31]
    assert list(islice(sumasDeDosPrimos1(), 23)) == r
    assert list(islice(sumasDeDosPrimos2(), 23)) == r
    assert list(islice(sumasDeDosPrimos3(), 23)) == r
    assert list(islice(sumasDeDosPrimos4(), 23)) == r
    print("Verificado")

# La comprobación es
#    >>> test_sumasDeDosPrimos()
#    Verificado

# Comprobación de equivalencia
# ============================

# nth(i, n) es el n-ésimo elemento del iterador i. Por ejemplo,
#    nth(primos(), 4) == 11
def nth(i: Iterator[int], n: int) -> int:
    return list(islice(i, n, n+1))[0]

# La propiedad es
@given(st.integers(min_value=1, max_value=200))
def test_sumasDeDosPrimos_equiv(n: int) -> None:
    r = nth(sumasDeDosPrimos1(), n)
    assert nth(sumasDeDosPrimos2(), n) == r
    assert nth(sumasDeDosPrimos3(), n) == r
    assert nth(sumasDeDosPrimos4(), n) == r

# La comprobación es
#    >>> test_sumasDeDosPrimos_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('nth(sumasDeDosPrimos1(), 1000)')
#    3.02 segundos
#    >>> tiempo('nth(sumasDeDosPrimos2(), 1000)')
#    1.53 segundos
#    >>> tiempo('nth(sumasDeDosPrimos3(), 1000)')
#    0.03 segundos
#    >>> tiempo('nth(sumasDeDosPrimos4(), 1000)')
#    0.00 segundos
#
#    >>> tiempo('nth(sumasDeDosPrimos3(), 5*10**4)')
#    3.76 segundos
#    >>> tiempo('nth(sumasDeDosPrimos4(), 5*10**4)')
#    0.33 segundos

# ---------------------------------------------------------------------
# § Referencia                                                       --
# ---------------------------------------------------------------------

# N.J.A. Sloane, "Sucesión A014091" en OEIS http://oeis.org/A014091
