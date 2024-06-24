# Numeros_con_digitos_primos.py
# Números con todos sus dígitos primos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-junio-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la lista
#    numerosConDigitosPrimos : () -> Iterator[int]
# cuyos elementos son los números con todos sus dígitos primos. Por
# ejemplo,
#    >>> list(islice(numerosConDigitosPrimos1(), 22))
#    [2,3,5,7,22,23,25,27,32,33,35,37,52,53,55,57,72,73,75,77,222,223]
#    >>> nth(numerosConDigitosPrimos(), 10**7)
#    322732232572
# ---------------------------------------------------------------------

from itertools import chain, count, islice
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

# digitos(n) es la lista de las digitos de n. Por ejemplo,
#    digitos(325)  ==  [3,2,5]
def digitos(n: int) -> list[int]:
    return [int(x) for x in str(n)]

# subconjunto(xs, ys) se verifica si xs es un subconjunto de ys. Por
# ejemplo,
#    subconjunto([3,2,5,2], [2,7,3,5])  ==  True
#    subconjunto([3,2,5,2], [2,7,2,5])  ==  False
def subconjunto(xs: list[int],
                ys: list[int]) -> bool:
    return all(x in ys for x in xs)

# digitosPrimos(n) se verifica si todos los dígitos de n son
# primos. Por ejemplo,
#    digitosPrimos(352)  ==  True
#    digitosPrimos(362)  ==  False
def digitosPrimos(n: int) -> bool:
    return subconjunto(digitos(n), [2,3,5,7])

def numerosConDigitosPrimos1() -> Iterator[int]:
    return (n for n in count(2) if digitosPrimos(n))

# 2ª solución
# ===========

def numerosConDigitosPrimos2() -> Iterator[int]:
    return filter(lambda n: all(d in '2357' for d in str(n)), count(2))

# 3ª solución
# ===========

#    >>> list(islice(numerosConDigitosPrimos2(), 60))
#    [  2,  3,  5,  7,
#      22, 23, 25, 27,
#      32, 33, 35, 37,
#      52, 53, 55, 57,
#      72, 73, 75, 77,
#     222,223,225,227,
#     232,233,235,237,
#     252,253,255,257,
#     272,273,275,277,
#     322,323,325,327,
#     332,333,335,337,
#     352,353,355,357,
#     372,373,375,377,
#     522,523,525,527,
#     532,533,535,537]

def numerosConDigitosPrimos3() -> Iterator[int]:
    base = [2, 3, 5, 7]
    numeros = base.copy()
    while True:
        yield from numeros
        numeros = [10*n + d for n in numeros for d in base]

# 4ª solución
# ===========

#    >>> list(islice(numerosConDigitosPrimos2(), 60))
#    [ 2, 3, 5, 7,
#     22,23,25,27,
#     32,33,35,37,
#     52,53,55,57,
#     72,73,75,77,
#     222,223,225,227, 232,233,235,237, 252,253,255,257, 272,273,275,277,
#     322,323,325,327, 332,333,335,337, 352,353,355,357, 372,373,375,377,
#     522,523,525,527, 532,533,535,537]

# pega(d, n) es el número obtenido añadiendo el dígito d delante del
# número n. Por ejemplo,
#    pega(3, 35)  ==  335
def pega(d: int, n: int) -> int:
    return int(str(d) + str(n))

# siguiente(xs) es la lista obtenida añadiendo delante de cada
# elemento de xs los dígitos 2, 3, 5 y 7. Por ejemplo,
#    >>> siguiente([5,6,8])
#    [25,26,28,
#     35,36,38,
#     55,56,58,
#     75,76,78]
def siguiente(xs: list[int]) -> list[int]:
    return [pega(d, x) for d in [2, 3, 5, 7] for x in xs]

def numerosConDigitosPrimos4() -> Iterator[int]:
    base = [2, 3, 5, 7]
    yield from base
    numeros = base
    while True:
        numeros = siguiente(numeros)
        yield from numeros


# numerosConDigitosPrimos4 :: [Integer]
# numerosConDigitosPrimos4 = concat (iterate siguiente [2,3,5,7])

# Verificación
# ============

def test_numerosConDigitosPrimos() -> None:
    for numerosConDigitosPrimos in [numerosConDigitosPrimos1,
                                    numerosConDigitosPrimos2,
                                    numerosConDigitosPrimos3,
                                    numerosConDigitosPrimos4]:
        assert list(islice(numerosConDigitosPrimos(), 22)) ==\
            [2,3,5,7,22,23,25,27,32,33,35,37,52,53,55,57,72,73,75,77,222,223]
    print("Verificado")

# La verificación es
#    >>> test_numerosConDigitosPrimos()
#    Verificado

# Comprobación de equivalencia
# ============================

# nth(i, n) es el n-ésimo elemento del iterador i. Por ejemplo,
#    nth(primos(), 4) == 11
def nth(i: Iterator[int], n: int) -> int:
    return list(islice(i, n, n+1))[0]

# La propiedad es
@given(st.integers(min_value=1, max_value=100))
def test_numerosConDigitosPrimos_equiv(n: int) -> None:
    r = nth(numerosConDigitosPrimos1(), n)
    assert nth(numerosConDigitosPrimos2(), n) == r
    assert nth(numerosConDigitosPrimos3(), n) == r
    assert nth(numerosConDigitosPrimos4(), n) == r

# La comprobación es
#    >>> test_numerosConDigitosPrimos_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('nth(numerosConDigitosPrimos1(), 5000)')
#    1.05 segundos
#    >>> tiempo('nth(numerosConDigitosPrimos2(), 5000)')
#    0.33 segundos
#    >>> tiempo('nth(numerosConDigitosPrimos3(), 5000)')
#    0.00 segundos
#    >>> tiempo('nth(numerosConDigitosPrimos4(), 5000)')
#    0.01 segundos
#
#    >>> tiempo('nth(numerosConDigitosPrimos3(), 10**7)')
#    2.67 segundos
#    >>> tiempo('nth(numerosConDigitosPrimos4(), 10**7)')
#    8.56 segundos
