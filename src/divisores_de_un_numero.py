# divisores_de_un_numero.py
# Divisores de un número.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-septiembre-2022
# ---------------------------------------------------------------------

#  ---------------------------------------------------------------------
#  Definir la función
#     divisores : (int) -> list[int]
#  tal que divisores(n) es el conjunto de divisores de n. Por
#  ejemplo,
#    divisores(30)  ==  [1, 2, 3, 5, 6, 10, 15, 30]
#    len(divisores1(factorial(10)))  ==  270
#    len(divisores1(factorial(25)))  ==  340032
#  ---------------------------------------------------------------------

from math import factorial, sqrt
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy import divisors

setrecursionlimit(10**6)

# 1ª solución
# ===========

def divisores1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

# 2ª solución
# ===========

# esDivisorDe(x, n) se verifica si x es un divisor de n. Por ejemplo,
#    esDivisorDe(2, 6)  ==  True
#    esDivisorDe(4, 6)  ==  False
def esDivisorDe(x: int, n: int) -> bool:
    return n % x == 0

def divisores2(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if esDivisorDe(x, n)]

# 3ª solución
# ===========

def divisores3(n: int) -> list[int]:
    return list(filter(lambda x: esDivisorDe(x, n), range(1, n + 1)))

# 4ª solución
# ===========

# primerosDivisores(n) es la lista de los divisores del número n cuyo
# cuadrado es menor o gual que n. Por ejemplo,
#    primerosDivisores(25)  ==  [1,5]
#    primerosDivisores(30)  ==  [1,2,3,5]
def primerosDivisores(n: int) -> list[int]:
    return [x for x in range(1, 1 + round(sqrt(n))) if n % x == 0]

def divisores4(n: int) -> list[int]:
    xs = primerosDivisores(n)
    zs = list(reversed(xs))
    if zs[0]**2 == n:
        return xs + [n // a for a in zs[1:]]
    return xs + [n // a for a in zs]

# 5ª solución
# ===========

def divisores5(n: int) -> list[int]:
    def aux(xs: list[int]) -> list[int]:
        if xs:
            if esDivisorDe(xs[0], n):
                return [xs[0]] + aux(xs[1:])
            return aux(xs[1:])
        return xs

    return aux(list(range(1, n + 1)))

# 6ª solución
# ============

def divisores6(n: int) -> list[int]:
    xs = []
    for x in range(1, n+1):
        if n % x == 0:
            xs.append(x)
    return xs

# 7ª solución
# ===========

def divisores7(n: int) -> list[int]:
    x = 1
    xs = []
    ys = []
    while x * x < n:
        if n % x == 0:
            xs.append(x)
            ys.append(n // x)
        x = x + 1
    if x * x == n:
        xs.append(x)
    return xs + list(reversed(ys))

# 8ª solución
# ============

def divisores8(n: int) -> list[int]:
    return divisors(n)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_divisores(n):
    assert divisores1(n) ==\
           divisores2(n) ==\
           divisores3(n) ==\
           divisores4(n) ==\
           divisores5(n) ==\
           divisores6(n) ==\
           divisores7(n) ==\
           divisores8(n)

# La comprobación es
#    src> poetry run pytest -q divisores_de_un_numero.py
#    1 passed in 0.84s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('divisores5(4*factorial(7))')
#    1.40 segundos
#
#    >>> tiempo('divisores1(factorial(11))')
#    1.79 segundos
#    >>> tiempo('divisores2(factorial(11))')
#    3.80 segundos
#    >>> tiempo('divisores3(factorial(11))')
#    5.22 segundos
#    >>> tiempo('divisores4(factorial(11))')
#    0.00 segundos
#    >>> tiempo('divisores6(factorial(11))')
#    3.51 segundos
#    >>> tiempo('divisores7(factorial(11))')
#    0.00 segundos
#    >>> tiempo('divisores8(factorial(11))')
#    0.00 segundos
#
#    >>> tiempo('divisores4(factorial(17))')
#    2.23 segundos
#    >>> tiempo('divisores7(factorial(17))')
#    3.22 segundos
#    >>> tiempo('divisores8(factorial(17))')
#    0.00 segundos
#
#    >>> tiempo('divisores8(factorial(27))')
#    0.28 segundos
