# suma_de_los_primeros_numeros_naturales.py
# Suma de los primeros números naturales
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 27-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    suma : (int) -> int
# tal suma(n) es la suma de los n primeros números. Por ejemplo,
#    suma(3)  ==  6
#    len(str(suma2(10**100)))  ==  200
# ---------------------------------------------------------------------

from functools import reduce
from operator import add
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**8)

# 1ª solución
# ===========

def suma1(n: int) -> int:
    return sum(range(1, n + 1))

# 2ª solución
# ===========

def suma2(n: int) -> int:
    return (1 + n) * n // 2

# 3ª solución
# ===========

def suma3(n: int) -> int:
    if n == 1:
        return 1
    return n + suma3(n - 1)

# 4ª solución
# ===========

def suma4(n: int) -> int:
    return reduce(add, range(1, n + 1))

# 5ª solución
# ===========

def suma5(n: int) -> int:
    x, r = 1, 0
    while x <= n:
        r = r + x
        x = x + 1
    return r

# 6ª solución
# ===========

def suma6(n: int) -> int:
    r = 0
    for x in range(1, n + 1):
        r = r + x
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_suma(n: int) -> None:
    r = suma1(n)
    assert suma2(n) == r
    assert suma3(n) == r
    assert suma4(n) == r
    assert suma5(n) == r
    assert suma6(n) == r

# La comprobación es
#    src> poetry run pytest -q suma_de_los_primeros_numeros_naturales.py
#    1 passed in 0.16s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('suma1(20000)')
#    0.00 segundos
#    >>> tiempo('suma2(20000)')
#    0.00 segundos
#    >>> tiempo('suma3(20000)')
#    0.02 segundos
#    >>> tiempo('suma4(20000)')
#    0.00 segundos
#    >>> tiempo('suma5(20000)')
#    0.01 segundos
#    >>> tiempo('suma6(20000)')
#    0.00 segundos
#
#    >>> tiempo('suma1(10**8)')
#    1.55 segundos
#    >>> tiempo('suma2(10**8)')
#    0.00 segundos
#    >>> tiempo('suma4(10**8)')
#    3.69 segundos
#    >>> tiempo('suma5(10**8)')
#    7.04 segundos
#    >>> tiempo('suma6(10**8)')
#    4.23 segundos
