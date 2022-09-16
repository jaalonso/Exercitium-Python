# numeros_perfectos.py
# Números perfectos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un números entero positivo es [perfecto](https://bit.ly/3BIN0be) si
# es igual a la suma de sus divisores, excluyendo el propio número. Por
# ejemplo, 6 es un número perfecto porque sus divisores propios son 1,
# 2 y 3; y 6 = 1 + 2 + 3.
#
# Definir la función
#    perfectos (int) -> list[int]
# tal que perfectos(n) es la lista de todos los números perfectos
# menores que n. Por ejemplo,
#    perfectos(500)   ==  [6, 28, 496]
#    perfectos(10^5)  ==  [6, 28, 496, 8128]
# ---------------------------------------------------------------------

from math import sqrt
from sympy import divisors
from timeit import Timer, default_timer
from hypothesis import given, strategies as st

# 1ª solución
# ===========

# divisores(n) es la lista de los divisores del número n. Por ejemplo,
#    divisores(30)  ==  [1,2,3,5,6,10,15,30]
def divisores1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

def perfectos1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if sum(divisores1(x)) == 2 * x]

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

def perfectos2(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if sum(divisores2(x)) == 2 * x]

# 3ª solución
# ===========

def perfectos3(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if sum(divisors(x)) == 2 * x]

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_perfectos(n):
    assert perfectos1(n) ==\
           perfectos2(n) ==\
           perfectos3(n)

# La comprobación es
#    src> poetry run pytest -q numeros_perfectos.py
#    1 passed in 1.43s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('perfectos1(10**4)')
#    2.27 segundos
#    >>> tiempo('perfectos2(10**4)')
#    0.07 segundos
#    >>> tiempo('perfectos3(10**4)')
#    0.11 segundos
#
#    >>> tiempo('perfectos2(3 * 10**5)')
#    4.65 segundos
#    >>> tiempo('perfectos3(3 * 10**5)')
#    3.52 segundos
