# divisores_primos.py
# Divisores primos
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    divisoresPrimos : (int) -> list[int]
# tal que divisoresPrimos(x) es la lista de los divisores primos de x.
# Por ejemplo,
#    divisoresPrimos(40) == [2, 5]
#    divisoresPrimos(70) == [2, 5, 7]
#    len(divisoresPrimos4(producto(list(range(1, 20001))))) == 2262
# ------------------------------------------------------------------------

from math import sqrt
from operator import mul
from functools import reduce
from timeit import Timer, default_timer
from sys import setrecursionlimit
from sympy import divisors, isprime, primefactors
from hypothesis import given, strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

# divisores(n) es la lista de los divisores del número n. Por ejemplo,
#    divisores(30)  ==  [1,2,3,5,6,10,15,30]
def divisores1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

# primo(n) se verifica si n es primo. Por ejemplo,
#    primo(30)  == False
#    primo(31)  == True
def primo1(n: int) -> bool:
    return divisores1(n) == [1, n]

def divisoresPrimos1(x: int) -> list[int]:
    return [n for n in divisores1(x) if primo1(n)]

# 2ª solución
# ===========

# primerosDivisores(n) es la lista de los divisores del número n cuyo
# cuadrado es menor o gual que n. Por ejemplo,
#    primerosDivisores(25)  ==  [1,5]
#    primerosDivisores(30)  ==  [1,2,3,5]
def primerosDivisores2(n: int) -> list[int]:
    return [x for x in range(1, 1 + round(sqrt(n))) if n % x == 0]

def divisores2(n: int) -> list[int]:
    xs = primerosDivisores2(n)
    zs = list(reversed(xs))
    if zs[0]**2 == n:
        return xs + [n // a for a in zs[1:]]
    return xs + [n // a for a in zs]

def primo2(n: int) -> bool:
    return divisores2(n) == [1, n]

def divisoresPrimos2(x: int) -> list[int]:
    return [n for n in divisores2(x) if primo2(n)]

# 3ª solución
# ===========

# reducido(m, x) es el resultado de dividir repetidamente m por x,
# mientras sea divisible. Por ejemplo,
#    reducido(36, 2)  ==  9
def reducido(m: int, x: int) -> int:
    if m % x == 0:
        return reducido(m // x, x)
    return m

def divisoresPrimos3(n: int) -> list[int]:
    if n % 2 == 0:
        return [2] + divisoresPrimos3(reducido(n, 2))

    def aux(m, xs):
        if m == 1:
            return []
        if xs == []:
            return []
        if m % xs[0] == 0:
            return [xs[0]] + aux(reducido(m, xs[0]), xs[1:])
        return aux(m, xs[1:])
    return aux(n, range(3, n + 1, 2))

# 4ª solución
# ===========

def divisoresPrimos4(x: int) -> list[int]:
    return [n for n in divisors(x) if isprime(n)]

# 5ª solución
# ===========

def divisoresPrimos5(n):
    return primefactors(n)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_divisoresPrimos(n):
    assert divisoresPrimos1(n) ==\
           divisoresPrimos2(n) ==\
           divisoresPrimos3(n) ==\
           divisoresPrimos4(n) ==\
           divisoresPrimos5(n)

# La comprobación es
#    src> poetry run pytest -q divisores_primos.py
#    1 passed in 0.70s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

def producto(xs: list[int]) -> int:
    return reduce(mul, xs)

# La comparación es
#    >>> tiempo('divisoresPrimos1(producto(list(range(1, 12))))')
#    11.14 segundos
#    >>> tiempo('divisoresPrimos2(producto(list(range(1, 12))))')
#    0.03 segundos
#    >>> tiempo('divisoresPrimos3(producto(list(range(1, 12))))')
#    0.00 segundos
#    >>> tiempo('divisoresPrimos4(producto(list(range(1, 12))))')
#    0.00 segundos
#    >>> tiempo('divisoresPrimos5(producto(list(range(1, 12))))')
#    0.00 segundos
#
#    >>> tiempo('divisoresPrimos2(producto(list(range(1, 17))))')
#    14.21 segundos
#    >>> tiempo('divisoresPrimos3(producto(list(range(1, 17))))')
#    0.00 segundos
#    >>> tiempo('divisoresPrimos4(producto(list(range(1, 17))))')
#    0.01 segundos
#    >>> tiempo('divisoresPrimos5(producto(list(range(1, 17))))')
#    0.00 segundos
#
#    >>> tiempo('divisoresPrimos3(producto(list(range(1, 32))))')
#    0.00 segundos
#    >>> tiempo('divisoresPrimos4(producto(list(range(1, 32))))')
#    4.59 segundos
#    >>> tiempo('divisoresPrimos5(producto(list(range(1, 32))))')
#    0.00 segundos
#
#    >>> tiempo('divisoresPrimos3(producto(list(range(1, 10001))))')
#    3.00 segundos
#    >>> tiempo('divisoresPrimos5(producto(list(range(1, 10001))))')
#    0.24 segundos
