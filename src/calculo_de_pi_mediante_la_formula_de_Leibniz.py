# calculo_de_pi_mediante_la_formula_de_Leibniz.py
# Cálculo del número π mediante la fórmula de Leibniz.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El número π puede calcularse con la [fórmula de
# Leibniz](https://bit.ly/3ERCwZd)
#    π/4 = 1 - 1/3 + 1/5 - 1/7 + ...+ (-1)**n/(2*n+1) + ...
#
# Definir las funciones
#    calculaPi : (int) -> float
#    errorPi   : (float) -> int
# tales que
# + calculaPi(n) es la aproximación del número π calculada
#   mediante la expresión
#      4*(1 - 1/3 + 1/5 - 1/7 + ...+ (-1)**n/(2*n+1))
#   Por ejemplo,
#      calculaPi(3)    ==  2.8952380952380956
#      calculaPi(300)  ==  3.1449149035588526
# + errorPi(x) es el menor número de términos de la serie
#   necesarios para obtener pi con un error menor que x. Por ejemplo,
#      errorPi(0.1)    ==    9
#      errorPi(0.01)   ==   99
#      errorPi(0.001)  ==  999
# ---------------------------------------------------------------------

from itertools import islice
from math import pi
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª definición de calculaPi
# ==========================

def calculaPi1(k: int) -> float:
    return 4 * sum(((-1)**n/(2*n+1) for n in range(0, k+1)))

# 2ª definición de calculaPi
# ==========================

def calculaPi2(n: int) -> float:
    if n == 0:
        return 4
    return calculaPi2(n-1) + 4*(-1)**n/(2*n+1)

# 3ª definición de calculaPi
# ==========================

def calculaPi3(n: int) -> float:
    r = 1
    for k in range(1, n+1):
        r = r + (-1)**k/(2*k+1)
    return 4 * r

# Comprobación de equivalencia de calculaPi
# =========================================

# La propiedad es
@given(st.integers(min_value=1, max_value=100))
def test_calculaPi(n: int) -> None:
    r = calculaPi1(n)
    assert calculaPi2(n) == r
    assert calculaPi3(n) == r

# La comprobación es
#    src> poetry run pytest -q calculo_de_pi_mediante_la_formula_de_Leibniz.py
#    1 passed in 0.14s

# Comparación de eficiencia de calculaPi
# ======================================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('calculaPi1(10**6)')
#    0.37 segundos
#    >>> tiempo('calculaPi2(10**6)')
#    Process Python violación de segmento (core dumped)
#    >>> tiempo('calculaPi3(10**6)')
#    0.39 segundos

# 1ª definición de errorPi
# ========================

# naturales es el generador de los números naturales positivos, Por
# ejemplo,
#    >>> list(islice(naturales(), 5))
#    [1, 2, 3, 4, 5]
def naturales() -> Iterator[int]:
    i = 1
    while True:
        yield i
        i += 1

def errorPi1(x: float) -> int:
    return list(islice((n for n in naturales()
                        if abs(pi - calculaPi1(n)) < x), 1))[0]

# 2ª definición de errorPi
# ========================

def errorPi2(x: float) -> int:
    def aux(n: int) -> int:
        if abs(pi - calculaPi1(n)) < x:
            return n
        return aux(n + 1)

    return aux(1)

# Comprobación de equivalencia de errorPi
# =======================================

@given(st.integers(min_value=1, max_value=100))
def test_errorPi(n: int) -> None:
    assert errorPi1(n) == errorPi2(n)

# La comprobación es
#    src> poetry run pytest -q calculo_de_pi_mediante_la_formula_de_Leibniz.py
#    2 passed in 0.60s

# Comparación de eficiencia de errorPi
# ====================================

# La comparación es
#    >>> tiempo('errorPi1(0.0005)')
#    0.63 segundos
#    >>> tiempo('errorPi2(0.0005)')
#    0.58 segundos
