# suma_de_cuadrados_menos_cuadrado_de_la_suma.py
# Suma de cuadrados menos cuadrado de la suma
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    euler6 : (int) -> int
# tal que euler6(n) es la diferencia entre el cuadrado de la suma
# de los n primeros números y la suma de los cuadrados de los n
# primeros números. Por ejemplo,
#    euler6(10)       ==  2640
#    euler6(10^10)  ==  2500000000166666666641666666665000000000
#
# Nota: Este ejercicio está basado en el problema 6 del proyecto Euler
# https://www.projecteuler.net/problem=6
# ---------------------------------------------------------------------

from functools import reduce
from operator import add
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def euler6a(n: int) -> int:
    return suma1(n)**2 - sumaDeCuadrados1(n)

# suma(n) es la suma de los n primeros números. Por ejemplo,
#    suma(3)  ==  6
def suma1(n: int) -> int:
    return sum(range(1, n + 1))

# sumaDeCuadrados(n) es la suma de los cuadrados de los
# primeros n números; es decir, 1^2 + 2^2 + ... + n^2. Por ejemplo,
#    sumaDeCuadrados(3)    ==  14
#    sumaDeCuadrados(100)  ==  338350
def sumaDeCuadrados1(n: int) -> int:
    return sum(x**2 for x in range(1, n + 1))

# 2ª solución
# ===========

def euler6b(n: int) -> int:
    return suma2(n)**2 - sumaDeCuadrados2(n)

def suma2(n: int) -> int:
    return (1 + n) * n // 2

def sumaDeCuadrados2(n: int) -> int:
    return n * (n + 1) * (2 * n + 1) // 6

# 3ª solución
# ===========

def euler6c(n: int) -> int:
    return suma3(n)**2 - sumaDeCuadrados3(n)

def suma3(n: int) -> int:
    if n == 1:
        return 1
    return n + suma3(n - 1)

def sumaDeCuadrados3(n: int) -> int:
    if n == 1:
        return 1
    return n**2 + sumaDeCuadrados3(n - 1)

# 4ª solución
# ===========

def euler6d(n: int) -> int:
    return suma4(n)**2 - sumaDeCuadrados4(n)

def suma4(n: int) -> int:
    return reduce(add, range(1, n + 1))

def sumaDeCuadrados4(n: int) -> int:
    return reduce(add, (x**2 for x in range(1, n + 1)))

# 5ª solución
# ===========

def euler6e(n: int) -> int:
    return suma5(n)**2 - sumaDeCuadrados5(n)

def suma5(n: int) -> int:
    x, r = 1, 0
    while x <= n:
        r = r + x
        x = x + 1
    return r

def sumaDeCuadrados5(n: int) -> int:
    x, r = 1, 0
    while x <= n:
        r = r + x**2
        x = x + 1
    return r

# 6ª solución
# ===========

def euler6f(n: int) -> int:
    return suma6(n)**2 - sumaDeCuadrados6(n)

def suma6(n: int) -> int:
    r = 0
    for x in range(1, n + 1):
        r = r + x
    return r

def sumaDeCuadrados6(n: int) -> int:
    r = 0
    for x in range(1, n + 1):
        r = r + x**2
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_euler6(n):
    r = euler6a(n)
    assert euler6b(n) == r
    assert euler6c(n) == r
    assert euler6d(n) == r
    assert euler6e(n) == r
    assert euler6f(n) == r

# La comprobación es
#    src> poetry run pytest -q suma_de_cuadrados_menos_cuadrado_de_la_suma.py
#    1 passed in 0.21s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('euler6a(20000)')
#    0.02 segundos
#    >>> tiempo('euler6b(20000)')
#    0.00 segundos
#    >>> tiempo('euler6c(20000)')
#    0.02 segundos
#    >>> tiempo('euler6d(20000)')
#    0.01 segundos
#    >>> tiempo('euler6e(20000)')
#    0.01 segundos
#    >>> tiempo('euler6f(20000)')
#    0.01 segundos
#
#    >>> tiempo('euler6a(10**7)')
#    2.26 segundos
#    >>> tiempo('euler6b(10**7)')
#    0.00 segundos
#    >>> tiempo('euler6d(10**7)')
#    2.58 segundos
#    >>> tiempo('euler6e(10**7)')
#    2.89 segundos
#    >>> tiempo('euler6f(10**7)')
#    2.45 segundos
