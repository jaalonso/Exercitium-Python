# Numeros_duffinianos.py
# Números duffinianos.
# José A. Alonso Jiménez
# Sevilla, 28 de enero de 2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los números duffinianos https://bit.ly/2X1dMqd, llamados así por
# Richard Duffy, son los números compuestos n que son coprimos con la
# suma de sus divisores; es decir, n y la suma de los divisores de n no
# tienen ningún factor primo común.
#
# Por ejemplo, 35 es un número duffiniano ya que la suma de sus
# divisores es 1 + 5 + 7 + 35 = 48 que es coprimo con 35.
#
# Definir las funciones
#    esDuffiniano : (n) -> bool
#    duffinianos  : Iterator[int]
# tales que
# + esDuffiniano(n) se verifica si n es duffiniano. Por ejemplo,
#      esDuffiniano(35)    ==  True
#      esDuffiniano(2021)  ==  True
#      esDuffiniano(11)    ==  False
#      esDuffiniano(12)    ==  False
#      esDuffiniano(factorial(2*10**4))  ==  False
# + duffinianos() es la sucesión de los números duffinianos. Por ejemplo,
#      list(islice(duffinianos(), 12)) == [4,8,9,16,21,25,27,32,35,36,39,49]
#      len(list(takewhile(lambda x : x < 10**5, duffinianos1()))) == 24434
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from functools import reduce
from itertools import count, islice, takewhile
from math import factorial, gcd
from operator import mul
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st
from sympy import divisor_sigma, divisors, factorint, isprime

setrecursionlimit(10**6)

# 1ª solución
# ===========

# divisores(n) es la lista de los divisores de n. Por ejemplo,
#    divisores(35)  ==  [1,5,7,35]
def divisores(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

# sumaDivisores(n) es la suma de los divisores de n. Por ejemplo.
#    sumaDivisores1(35)  ==  48
def sumaDivisores1(n: int) -> int:
    return sum(divisores(n))

def esDuffiniano1(n: int) -> bool:
    return (n > 1 and
            not isprime(n) and
            gcd(n, sumaDivisores1(n)) == 1)

def duffinianos1() -> Iterator[int]:
    return (n for n in count(2) if esDuffiniano1(n))

# 2ª solución
# ===========

def sumaDivisores2(n: int) -> int:
    return sum(divisors(n))

def esDuffiniano2(n: int) -> bool:
    return (n > 1 and
            not isprime(n) and
            gcd(n, sumaDivisores2(n)) == 1)

def duffinianos2() -> Iterator[int]:
    return (n for n in count(2) if esDuffiniano2(n))

# 3ª solución
# ===========

def sumaDivisores3(n: int) -> int:
    def aux(xs: list[int]) -> int:
        if xs:
            if n % xs[0] == 0:
                return xs[0] + aux(xs[1:])
            return aux(xs[1:])
        return 0
    return aux(list(range(1, n + 1)))

def esDuffiniano3(n: int) -> bool:
    return (n > 1 and
            not isprime(n) and
            gcd(n, sumaDivisores3(n)) == 1)

def duffinianos3() -> Iterator[int]:
    return (n for n in count(2) if esDuffiniano3(n))

# 4ª solución
# ===========

# Si la descomposición de x en factores primos es
#    x = p(1)^e(1) . p(2)^e(2) . .... . p(n)^e(n)
# entonces la suma de los divisores de x es
#    p(1)^(e(1)+1) - 1     p(2)^(e(2)+1) - 1       p(n)^(e(2)+1) - 1
#   ------------------- . ------------------- ... -------------------
#        p(1)-1                p(2)-1                  p(n)-1
# Ver la demostración en http://bit.ly/2zUXZPc

def sumaDivisores4(n: int) -> int:
    return reduce(mul, [(p ** (e + 1) - 1) // (p - 1)
                        for (p, e) in factorint(n).items()])

def esDuffiniano4(n: int) -> bool:
    return (n > 1 and
            not isprime(n) and
            gcd(n, sumaDivisores4(n)) == 1)

def duffinianos4() -> Iterator[int]:
    return (n for n in count(2) if esDuffiniano4(n))

# 5ª solución
# ===========

def sumaDivisores5(n: int) -> int:
    x = 1
    r1 = 0
    r2 = 0
    while x * x < n:
        if n % x == 0:
            r1 += x
            r2 += n // x
        x += 1
    if x * x == n:
        r1 += x
    return r1 + r2

def esDuffiniano5(n: int) -> bool:
    return (n > 1 and
            not isprime(n) and
            gcd(n, sumaDivisores5(n)) == 1)

def duffinianos5() -> Iterator[int]:
    return (n for n in count(2) if esDuffiniano5(n))

# 6ª solución
# ===========

def sumaDivisores6(n: int) -> int:
    return divisor_sigma(n, 1)

def esDuffiniano6(n: int) -> bool:
    return (n > 1 and
            not isprime(n) and
            gcd(n, sumaDivisores6(n)) == 1)

def duffinianos6() -> Iterator[int]:
    return (n for n in count(2) if esDuffiniano6(n))

# Verificación
# ============

def test_esDuffiniano() -> None:
    for esDuffiniano in [esDuffiniano1,
                         esDuffiniano2,
                         esDuffiniano3,
                         esDuffiniano4,
                         esDuffiniano5,
                         esDuffiniano6]:
        assert esDuffiniano(35) is True
        assert esDuffiniano(2021) is True
        assert esDuffiniano(11) is False
        assert esDuffiniano(12) is False
        print(f"Verificado {esDuffiniano.__name__}")

# La verificación es
#    >>> test_esDuffiniano()
#    Verificado esDuffiniano1
#    Verificado esDuffiniano2
#    Verificado esDuffiniano3
#    Verificado esDuffiniano4
#    Verificado esDuffiniano5
#    Verificado esDuffiniano6

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_esDuffiniano_equiv(n: int) -> None:
    r = esDuffiniano1(n)
    assert esDuffiniano2(n) == r
    assert esDuffiniano3(n) == r
    assert esDuffiniano4(n) == r
    assert esDuffiniano5(n) == r
    assert esDuffiniano6(n) == r

# La comprobación es
#    >>> test_esDuffiniano_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('esDuffiniano1(factorial(11))')
#    2.60 segundos
#    >>> tiempo('esDuffiniano2(factorial(11))')
#    0.00 segundos
#    >>> tiempo('esDuffiniano4(factorial(11))')
#    0.00 segundos
#    >>> tiempo('esDuffiniano5(factorial(11))')
#    0.00 segundos
#    >>> tiempo('esDuffiniano6(factorial(11))')
#    0.00 segundos
#
#    >>> tiempo('esDuffiniano2(factorial(30))')
#    1.50 segundos
#    >>> tiempo('esDuffiniano4(factorial(30))')
#    0.00 segundos
#    >>> tiempo('esDuffiniano6(factorial(30))')
#    0.00 segundos
#
#    >>> tiempo('esDuffiniano4(factorial(10000))')
#    0.25 segundos
#    >>> tiempo('esDuffiniano6(factorial(10000))')
#    0.26 segundos
