# suma_de_multiplos_de_3_o_5.py
# Suma de múltiplos de 3 ó 5.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    euler1 : (int) -> int
# tal que euler1(n) es la suma de todos los múltiplos de 3 ó 5 menores
# que n. Por ejemplo,
#    euler1(10)     == 23
#    euler1(10**2)  == 2318
#    euler1(10**3)  == 233168
#    euler1(10**4)  == 23331668
#    euler1(10**5)  == 2333316668
#    euler1(10**10) == 23333333331666666668
#    euler1(10**20) == 2333333333333333333316666666666666666668
#
# Nota: Este ejercicio está basado en el problema 1 del Proyecto Euler
# https://projecteuler.net/problem=1
# ---------------------------------------------------------------------

from math import gcd
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

# multiplo(x, y) se verifica si x es un múltiplo de y. Por ejemplo.
#    multiplo(12, 3)  ==  True
#    multiplo(14, 3)  ==  False
def multiplo(x: int, y: int) -> int:
    return x % y == 0

def euler1a(n: int) -> int:
    return sum(x for x in range(1, n)
               if (multiplo(x, 3) or multiplo(x, 5)))

# 2ª solución                                                        --
# ===========

def euler1b(n: int) -> int:
    return sum(x for x in range(1, n)
               if gcd(x, 15) > 1)

# 3ª solución                                                        --
# ===========

def euler1c(n: int) -> int:
    return sum(range(3, n, 3)) + \
           sum(range(5, n, 5)) - \
           sum(range(15, n, 15))

# 4ª solución                                                        --
# ===========

def euler1d(n: int) -> int:
    return sum(set(list(range(3, n, 3)) + list(range(5, n, 5))))

# 5ª solución                                                        --
# ===========

def euler1e(n: int) -> int:
    return sum(set(list(range(3, n, 3))) | set(list(range(5, n, 5))))

# 6ª solución                                                        --
# ===========

# suma(d, x) es la suma de los múltiplos de d menores que x. Por
# ejemplo,
#    suma(3, 20)  ==  63
def suma(d: int, x: int) -> int:
    a = d
    b = d * ((x - 1) // d)
    n = 1 + (b - a) // d
    return (a + b) * n // 2

def euler1f(n: int) -> int:
    return suma(3, n) + suma(5, n) - suma(15, n)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_euler1(n: int) -> None:
    r = euler1a(n)
    assert euler1b(n) == r
    assert euler1c(n) == r
    assert euler1d(n) == r
    assert euler1e(n) == r

# La comprobación es
#    src> poetry run pytest -q suma_de_multiplos_de_3_o_5.py
#    1 passed in 0.16s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('euler1a(10**7)')
#    1.49 segundos
#    >>> tiempo('euler1b(10**7)')
#    0.93 segundos
#    >>> tiempo('euler1c(10**7)')
#    0.07 segundos
#    >>> tiempo('euler1d(10**7)')
#    0.42 segundos
#    >>> tiempo('euler1e(10**7)')
#    0.69 segundos
#    >>> tiempo('euler1f(10**7)')
#    0.00 segundos
#
#    >>> tiempo('euler1c(10**8)')
#    0.72 segundos
#    >>> tiempo('euler1f(10**8)')
#    0.00 segundos
