# digitos_de_un_numero.py
# Dígitos de un número.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 27-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    digitos : (int) -> list[int]
# tal que digitos(n) es la lista de los dígitos del número n. Por
# ejemplo,
#    digitos(320274)  ==  [3, 2, 0, 2, 7, 4]
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from math import factorial
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy.ntheory.digits import digits

setrecursionlimit(10**6)

# 1ª solución
# ===========

def digitos1(n: int) -> list[int]:
    if n < 10:
        return [n]
    return digitos1(n // 10) + [n % 10]

# 2ª solución
# ===========

def digitos2(n: int) -> list[int]:
    return [int(x) for x in str(n)]

# 3ª solución
# ===========

def digitos3(n: int) -> list[int]:
    r: list[int] = []
    for x in str(n):
        r.append(int(x))
    return r

# 4ª solución
# ===========

def digitos4(n: int) -> list[int]:
    return list(map(int, list(str(n))))

# 5ª solución
# ===========

def digitos5(n: int) -> list[int]:
    r: list[int] = []
    while n > 0:
        r = [n % 10] + r
        n = n // 10
    return r

# 6ª solución
# ===========

def digitos6(n: int) -> list[int]:
    r: list[int] = []
    while n > 0:
        r.append(n % 10)
        n = n // 10
    return list(reversed(r))

# 7ª solución
# ===========

def digitos7(n: int) -> list[int]:
    return digits(n)[1:]

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1))
def test_digitos(n: int) -> None:
    r = digitos1(n)
    assert digitos2(n) == r
    assert digitos3(n) == r
    assert digitos4(n) == r
    assert digitos5(n) == r
    assert digitos6(n) == r
    assert digitos7(n) == r

# La comprobación es
#    src> poetry run pytest -q digitos_de_un_numero.py
#    1 passed in 0.49s

# Comparación de eficiencia
# =========================

def tiempo(ex: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(ex, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('digitos1(factorial(6000))')
#    0.58 segundos
#    >>> tiempo('digitos2(factorial(6000))')
#    0.01 segundos
#    >>> tiempo('digitos3(factorial(6000))')
#    0.01 segundos
#    >>> tiempo('digitos4(factorial(6000))')
#    0.01 segundos
#    >>> tiempo('digitos5(factorial(6000))')
#    0.60 segundos
#    >>> tiempo('digitos6(factorial(6000))')
#    0.17 segundos
#    >>> tiempo('digitos7(factorial(6000))')
#    0.10 segundos
#
#    >>> tiempo('digitos2(factorial(2*10**4))')
#    0.10 segundos
#    >>> tiempo('digitos3(factorial(2*10**4))')
#    0.10 segundos
#    >>> tiempo('digitos4(factorial(2*10**4))')
#    0.09 segundos
#    >>> tiempo('digitos6(factorial(2*10**4))')
#    2.33 segundos
#    >>> tiempo('digitos7(factorial(2*10**4))')
#    1.18 segundos
#
#    >>> tiempo('digitos2(factorial(10**5))')
#    3.53 segundos
#    >>> tiempo('digitos3(factorial(10**5))')
#    3.22 segundos
#    >>> tiempo('digitos4(factorial(10**5))')
#    3.02 segundos
