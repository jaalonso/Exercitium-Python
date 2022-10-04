# aproximacion_del_numero_e.py
# Aproximación del número e.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 12-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El [número e](https://bit.ly/3y17R7l) se define como el límite de la
# sucesión (1+1/n)**n; es decir,
#    e = lim (1+1/n)**n
#
# Definir las funciones
#    aproxE      : (int) -> list[float]
#    errorAproxE : (float) -> int
# tales que
# + aproxE(k) es la lista de los k primeros términos de la sucesión
#   (1+1/n)**m. Por ejemplo,
#      aproxE(4) == [2.0, 2.25, 2.37037037037037, 2.44140625]
#      last (aproxE (7*10^7))  ==  2.7182818287372563
# + errorE(x) es el menor número de términos de la sucesión
#   (1+1/m)**m necesarios para obtener su límite con un error menor que
#   x. Por ejemplo,
#      errorAproxE(0.1)    ==  13
#      errorAproxE(0.01)   ==  135
#      errorAproxE(0.001)  ==  1359
# ---------------------------------------------------------------------

from math import e
from itertools import islice, dropwhile
from timeit import Timer, default_timer
from sys import setrecursionlimit
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª definición de aproxE
# =======================

def aproxE1(k: int) -> list[float]:
    return [(1 + 1/n)**n for n in range(1, k + 1)]

# 2ª definición de aproxE
# =======================

def aproxE2(n: int) -> list[float]:
    if n == 0:
        return []
    return aproxE2(n - 1) + [(1 + 1/n)**n]

# 3ª definición de aproxE
# =======================

def aproxE3(n: int) -> list[float]:
    def aux(n: int) -> list[float]:
        if n == 0:
            return []
        return [(1 + 1/n)**n] + aux(n - 1)

    return list(reversed(aux(n)))

# 4ª definición de aproxE
# =======================

def aproxE4(n: int) -> list[float]:
    def aux(xs: list[float], n: int) -> list[float]:
        if n == 0:
            return xs
        return aux([(1 + 1/n)**n] + xs, n - 1)

    return aux([], n)

# 5ª definición de aproxE
# =======================

def aproxE5(n: int) -> list[float]:
    return list(map((lambda k: (1+1/k)**k), range(1, n+1)))

# 6ª definición de aproxE
# =======================

def aproxE6(n: int) -> list[float]:
    r = []
    for k in range(1, n+1):
        r.append((1+1/k)**k)
    return r

# Comprobación de equivalencia de aproxE
# ======================================

# La propiedad es
@given(st.integers(min_value=1, max_value=100))
def test_aproxE(n: int) -> None:
    r = aproxE1(n)
    assert aproxE2(n) == r
    assert aproxE3(n) == r
    assert aproxE4(n) == r
    assert aproxE5(n) == r
    assert aproxE6(n) == r

# La comprobación es
#    src> poetry run pytest -q aproximacion_del_numero_e.py
#    1 passed in 0.60s

# Comparación de eficiencia de aproxE
# ===================================

def tiempo(ex: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(ex, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('aproxE1(20000)')
#    0.00 segundos
#    >>> tiempo('aproxE2(20000)')
#    0.43 segundos
#    >>> tiempo('aproxE3(20000)')
#    0.60 segundos
#    >>> tiempo('aproxE4(20000)')
#    1.23 segundos
#    >>> tiempo('aproxE5(20000)')
#    0.00 segundos
#    >>> tiempo('aproxE6(20000)')
#    0.00 segundos

#    >>> tiempo('aproxE1(10**7)')
#    1.18 segundos
#    >>> tiempo('aproxE5(10**7)')
#    1.48 segundos
#    >>> tiempo('aproxE6(10**7)')
#    1.43 segundos

# 1ª definición de errorAproxE
# ============================

# naturales es el generador de los números naturales positivos, Por
# ejemplo,
#    >>> list(islice(naturales(), 5))
#    [1, 2, 3, 4, 5]
def naturales() -> Iterator[int]:
    i = 1
    while True:
        yield i
        i += 1

def errorAproxE1(x: float) -> int:
    return list(islice((n for n in naturales()
                        if abs(e - (1 + 1/n)**n) < x), 1))[0]

# # 2ª definición de errorAproxE
# # ============================

def errorAproxE2(x: float) -> int:
    def aux(n: int) -> int:
        if abs(e - (1 + 1/n)**n) < x:
            return n
        return aux(n + 1)

    return aux(1)

# 3ª definición de errorAproxE
# ============================

def errorAproxE3(x: float) -> int:
    return list(islice(dropwhile(lambda n: abs(e - (1 + 1/n)**n) >= x,
                                 naturales()),
                       1))[0]


# Comprobación de equivalencia de errorAproxE
# ===========================================

@given(st.integers(min_value=1, max_value=100))
def test_errorAproxE(n: int) -> None:
    r = errorAproxE1(n)
    assert errorAproxE2(n) == r
    assert errorAproxE3(n) == r

# La comprobación es
#    src> poetry run pytest -q aproximacion_del_numero_e.py
#    2 passed in 0.60s

# Comparación de eficiencia de aproxE
# ===================================

# La comparación es
#    >>> tiempo('errorAproxE1(0.0001)')
#    0.00 segundos
#    >>> tiempo('errorAproxE2(0.0001)')
#    0.00 segundos
#    >>> tiempo('errorAproxE3(0.0001)')
#    0.00 segundos
#
#    >>> tiempo('errorAproxE1(0.0000001)')
#    2.48 segundos
#    >>> tiempo('errorAproxE3(0.0000001)')
#    2.61 segundos
