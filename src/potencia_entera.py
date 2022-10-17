# potencia_entera.py
# Potencia entera.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 25-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    potencia : (int, int) -> int
# tal que potencia(x, n) es x elevado al número natural n. Por ejemplo,
#    potencia(2, 3)  ==  8
# ---------------------------------------------------------------------

from functools import reduce
from operator import mul
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def potencia1(m: int, n: int) -> int:
    if n == 0:
        return 1
    return m * potencia1(m, n-1)

# 2ª solución
# ===========

def potencia2(m: int, n: int) -> int:
    def aux(k: int) -> int:
        if k == 0:
            return 1
        return m * aux(k-1)
    return aux(n)

# 3ª solución
# ===========

def potencia3(m: int, n: int) -> int:
    def aux(r: int, k: int) -> int:
        if k == 0:
            return r
        return aux(r*m, k-1)
    return aux(1, n)

# 4ª solución
# ===========

# producto(xs) es el producto de los elementos de xs. Por ejemplo,
#    producto([2, 3, 5])  ==  30
def producto(xs: list[int]) -> int:
    return reduce(mul, xs, 1)

def potencia4(m: int, n: int) -> int:
    return producto([m]*n)

# 5ª solución
# ===========

def potencia5(m: int, n: int) -> int:
    r = 1
    for _ in range(0, n):
        r = r * m
    return r

# 6ª solución
# ===========

def potencia6(m: int, n: int) -> int:
    return m**n

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(),
       st.integers(min_value=0, max_value=100))
def test_potencia(m: int, n: int) -> None:
    r = potencia1(m, n)
    assert potencia2(m, n) == r
    assert potencia3(m, n) == r
    assert potencia4(m, n) == r
    assert potencia5(m, n) == r
    assert potencia6(m, n) == r

# La comprobación es
#    src> poetry run pytest -q potencia_entera.py
#    1 passed in 0.17s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('potencia1(2, 2*10**4)')
#    0.01 segundos
#    >>> tiempo('potencia2(2, 2*10**4)')
#    0.01 segundos
#    >>> tiempo('potencia3(2, 2*10**4)')
#    0.02 segundos
#    >>> tiempo('potencia4(2, 2*10**4)')
#    0.01 segundos
#    >>> tiempo('potencia5(2, 2*10**4)')
#    0.01 segundos
#    >>> tiempo('potencia6(2, 2*10**4)')
#    0.00 segundos
#
#    >>> tiempo('potencia4(2, 5*10**5)')
#    2.87 segundos
#    >>> tiempo('potencia4(2, 5*10**5)')
#    2.87 segundos
#    >>> tiempo('potencia5(2, 5*10**5)')
#    3.17 segundos
#    >>> tiempo('potencia6(2, 5*10**5)')
#    0.00 segundos
