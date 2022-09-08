# suma_de_los_cuadrados_de_los_primeros_numeros_naturales.py
# Suma de los xuadrados de los primeros números naturales
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 28-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    sumaDeCuadrados : (int) -> int
# tal sumaDeCuadrados(n) es la suma de los xuadrados de los n primeros
# números naturales. Por ejemplo,
#    suma(3)   ==  14
#    suma(100) ==  338350
#    len(str(suma2(10**100)))  ==  300
# ---------------------------------------------------------------------

from operator import add
from functools import reduce
from sys import setrecursionlimit
from timeit import Timer, default_timer
from hypothesis import given, strategies as st
setrecursionlimit(10**6)

# 1ª solución
# ===========

def sumaDeCuadrados1(n: int) -> int:
    return sum(x**2 for x in range(1, n + 1))

# 2ª solución
# ===========

def sumaDeCuadrados2(n: int) -> int:
    return n * (n + 1) * (2 * n + 1) // 6

# 3ª solución
# ===========

def sumaDeCuadrados3(n: int) -> int:
    if n == 1:
        return 1
    return n**2 + sumaDeCuadrados3(n - 1)

# 4ª solución
# ===========

def sumaDeCuadrados4(n: int) -> int:
    return reduce(add, (x**2 for x in range(1, n + 1)))

# 5ª solución
# ===========

def sumaDeCuadrados5(n: int) -> int:
    x, r = 1, 0
    while x <= n:
        r = r + x**2
        x = x + 1
    return r

# 6ª solución
# ===========

def sumaDeCuadrados6(n: int) -> int:
    r = 0
    for x in range(1, n + 1):
        r = r + x**2
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_sumaDeCuadrados(n):
    r = sumaDeCuadrados1(n)
    assert sumaDeCuadrados2(n) == r
    assert sumaDeCuadrados3(n) == r
    assert sumaDeCuadrados4(n) == r
    assert sumaDeCuadrados5(n) == r
    assert sumaDeCuadrados6(n) == r

# La comprobación es
#    src> poetry run pytest -q suma_de_los_cuadrados_de_los_primeros_numeros_naturales.py
#    1 passed in 0.19s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('sumaDeCuadrados1(20000)')
#    0.01 segundos
#    >>> tiempo('sumaDeCuadrados2(20000)')
#    0.00 segundos
#    >>> tiempo('sumaDeCuadrados3(20000)')
#    0.02 segundos
#    >>> tiempo('sumaDeCuadrados4(20000)')
#    0.02 segundos
#    >>> tiempo('sumaDeCuadrados5(20000)')
#    0.02 segundos
#    >>> tiempo('sumaDeCuadrados6(20000)')
#    0.02 segundos
#
#    >>> tiempo('sumaDeCuadrados1(10**7)')
#    2.19 segundos
#    >>> tiempo('sumaDeCuadrados2(10**7)')
#    0.00 segundos
#    >>> tiempo('sumaDeCuadrados4(10**7)')
#    2.48 segundos
#    >>> tiempo('sumaDeCuadrados5(10**7)')
#    2.53 segundos
#    >>> tiempo('sumaDeCuadrados6(10**7)')
#    2.22 segundos
