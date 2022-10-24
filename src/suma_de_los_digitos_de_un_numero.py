# suma_de_los_digitos_de_un_numero.py
# Suma de los digitos de un número.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 28-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    sumaDigitos : (int) -> int
# tal que sumaDigitos(n) es la suma de los dígitos de n. Por ejemplo,
#    sumaDigitos(3)     ==  3
#    sumaDigitos(2454)  == 15
#    sumaDigitos(20045) == 11
# ---------------------------------------------------------------------

from functools import reduce
from math import factorial
from operator import add
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

# digitos(n) es la lista de los dígitos del número n. Por ejemplo,
#    digitos(320274)  ==  [3, 2, 0, 2, 7, 4]
def digitos(n: int) -> list[int]:
    return list(map(int, list(str(n))))

def sumaDigitos1(n: int) -> int:
    return sum(digitos(n))

# Nota. En lugar de la definición anterior de digitos se puede usar
# cualquiera del ejercicio "Dígitos de un número" https://bit.ly/3Tkhc2T

# 2ª solución
# ===========

def sumaDigitos2(n: int) -> int:
    return reduce(add, digitos(n))

# 3ª solución
# ===========

def sumaDigitos3(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + sumaDigitos3(n // 10)

# 4ª solución
# ===========

def sumaDigitos4(n: int) -> int:
    def aux(r: int, m: int) -> int:
        if m < 10:
            return r + m
        return aux(r + m % 10, m // 10)
    return aux(0, n)

# 5ª solución
# ===========

def sumaDigitos5(n: int) -> int:
    r = 0
    for x in digitos(n):
        r = r + x
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=1000))
def test_sumaDigitos(n: int) -> None:
    r = sumaDigitos1(n)
    assert sumaDigitos2(n) == r
    assert sumaDigitos3(n) == r
    assert sumaDigitos4(n) == r
    assert sumaDigitos5(n) == r

# La comprobación es
#    src> poetry run pytest -q suma_de_los_digitos_de_un_numero.py
#    1 passed in 0.35s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('sumaDigitos1(factorial(6*10**3))')
#    0.01 segundos
#    >>> tiempo('sumaDigitos2(factorial(6*10**3))')
#    0.01 segundos
#    >>> tiempo('sumaDigitos3(factorial(6*10**3))')
#    0.13 segundos
#    >>> tiempo('sumaDigitos4(factorial(6*10**3))')
#    0.13 segundos
#    >>> tiempo('sumaDigitos5(factorial(6*10**3))')
#    0.01 segundos
#
#    >>> tiempo('sumaDigitos1(factorial(10**5))')
#    2.20 segundos
#    >>> tiempo('sumaDigitos2(factorial(10**5))')
#    2.22 segundos
#    >>> tiempo('sumaDigitos5(factorial(10**5))')
#    2.19 segundos
