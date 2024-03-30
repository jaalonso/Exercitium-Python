# Exponente_en_la_factorizacion.py
# Exponente en la factorización.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-marzo-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    exponente : (int, int) -> int
# tal que exponente(x, n) es el exponente de x en la factorización
# prima de n (se supone que x > 1 y n > 0). Por ejemplo,
#    exponente(2, 24)  ==  3
#    exponente(3, 24)  ==  1
#    exponente(6, 24)  ==  0
#    exponente(7, 24)  ==  0
# ---------------------------------------------------------------------

from itertools import takewhile
from typing import Callable, Iterator

from hypothesis import given
from hypothesis import strategies as st
from sympy.ntheory import factorint

# 1ª solución
# ===========

# esPrimo(x) se verifica si x es un número primo. Por ejemplo,
#    esPrimo(7)  ==  True
#    esPrimo(8)  ==  False
def esPrimo(x: int) -> bool:
    return [y for y in range(1, x+1) if x % y == 0] == [1,x]

def exponente1(x: int, n: int) -> int:
    def aux (m: int) -> int:
        if m % x == 0:
            return 1 + aux(m // x)
        return 0
    if esPrimo(x):
        return aux(n)
    return 0

# 2ª solución
# ===========

# iterate(f, x) es el iterador obtenido aplicando f a x y continuando
# aplicando f al resultado anterior. Por ejemplo,
#    >>> list(islice(iterate(lambda x : 4 * x, 1), 5))
#    [1, 4, 16, 64, 256]
def iterate(f: Callable[[int], int], x: int) -> Iterator[int]:
    r = x
    while True:
        yield r
        r = f(r)

# divisible(n, x) se verifica si n es divisible por x. Por ejemplo,
#    divisible(6, 2)  ==  True
#    divisible(7, 2)  ==  False
def divisible(n: int, x: int) -> bool:
    return n % x == 0

def exponente2(x: int, n: int) -> int:
    if esPrimo(x):
        return len(list(takewhile(lambda m : divisible(m, x),
                                  iterate(lambda m : m // x, n))))
    return 0

# 3ª solución
# ===========

def exponente3(x: int, n: int) -> int:
    return factorint(n, multiple = True).count(x)

# Verificación
# ============

def test_exponente() -> None:
    for exponente in [exponente1, exponente2, exponente3]:
        assert exponente(2, 24) == 3
        assert exponente(3, 24) == 1
        assert exponente(6, 24) == 0
        assert exponente(7, 24) == 0
    print("Verificado")

# La verificación es
#    >>> test_exponente()
#    Verificado

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000),
       st.integers(min_value=0, max_value=1000))
def test_exponente_equiv(x: int, n: int) -> None:
    r = exponente1(x, n)
    assert r == exponente2(x, n)
    assert r == exponente3(x, n)

# La comprobación es
#    >>> test_exponente_equiv()
#    >>>
