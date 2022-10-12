# limite_del_seno.py
# Aproximación al límite de sen(x)/x cuando x tiende a cero
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El limite de sen(x)/x, cuando x tiende a cero, se puede calcular como
# el límite de la sucesión sen(1/n)/(1/n), cuando n tiende a infinito.
#
# Definir las funciones
#    aproxLimSeno : (int) -> list[float]
#    errorLimSeno : (float) -> int
# tales que
# + aproxLimSeno(n) es la lista cuyos elementos son los n primeros
#   términos de la sucesión sen(1/m)/(1/m). Por ejemplo,
#      aproxLimSeno(1) == [0.8414709848078965]
#      aproxLimSeno(2) == [0.8414709848078965,0.958851077208406]
# + errorLimSeno(x) es el menor número de términos de la sucesión
#   sen(1/m)/(1/m) necesarios para obtener su límite con un error menor
#   que x. Por ejemplo,
#      errorLimSeno(0.1)     ==   2
#      errorLimSeno(0.01)    ==   5
#      errorLimSeno(0.001)   ==  13
#      errorLimSeno(0.0001)  ==  41
# ---------------------------------------------------------------------

from itertools import dropwhile, islice
from math import sin
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª definición de aproxLimSeno
# =============================

def aproxLimSeno1(k: int) -> list[float]:
    return [sin(1/n)/(1/n) for n in range(1, k + 1)]

# 2ª definición de aproxLimSeno
# =============================

def aproxLimSeno2(n: int) -> list[float]:
    if n == 0:
        return []
    return aproxLimSeno2(n - 1) + [sin(1/n)/(1/n)]

# 3ª definición de aproxLimSeno
# =============================

def aproxLimSeno3(n: int) -> list[float]:
    def aux(n: int) -> list[float]:
        if n == 0:
            return []
        return [sin(1/n)/(1/n)] + aux(n - 1)

    return list(reversed(aux(n)))

# 4ª definición de aproxLimSeno
# =============================

def aproxLimSeno4(n: int) -> list[float]:
    def aux(xs: list[float], n: int) -> list[float]:
        if n == 0:
            return xs
        return aux([sin(1/n)/(1/n)] + xs, n - 1)

    return aux([], n)

# 5ª definición de aproxLimSeno
# =============================

def aproxLimSeno5(n: int) -> list[float]:
    return list(map((lambda k: sin(1/k)/(1/k)), range(1, n+1)))

# 6ª definición de aproxLimSeno
# =============================

def aproxLimSeno6(n: int) -> list[float]:
    r = []
    for k in range(1, n+1):
        r.append(sin(1/k)/(1/k))
    return r

# Comprobación de equivalencia de aproxLimSeno
# ============================================

# La propiedad es
@given(st.integers(min_value=1, max_value=100))
def test_aproxLimSeno(n: int) -> None:
    r = aproxLimSeno1(n)
    assert aproxLimSeno2(n) == r
    assert aproxLimSeno3(n) == r
    assert aproxLimSeno4(n) == r
    assert aproxLimSeno5(n) == r
    assert aproxLimSeno6(n) == r

# La comprobación es
#    src> poetry run pytest -q limite_del_seno.py
#    1 passed in 0.60s

# Comparación de eficiencia de aproxLimSeno
# =========================================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('aproxLimSeno1(3*10**5)')
#    0.03 segundos
#    >>> tiempo('aproxLimSeno2(3*10**5)')
#    Process Python violación de segmento (core dumped)
#    >>> tiempo('aproxLimSeno3(3*10**5)')
#    Process Python violación de segmento (core dumped)
#    >>> tiempo('aproxLimSeno4(3*10**5)')
#    Process Python violación de segmento (core dumped)
#    >>> tiempo('aproxLimSeno5(3*10**5)')
#    0.04 segundos
#    >>> tiempo('aproxLimSeno6(3*10**5)')
#    0.07 segundos
#
#    >>> tiempo('aproxLimSeno1(10**7)')
#    1.29 segundos
#    >>> tiempo('aproxLimSeno5(10**7)')
#    1.40 segundos
#    >>> tiempo('aproxLimSeno6(10**7)')
#    1.45 segundos

# 1ª definición de errorLimSeno
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

def errorLimSeno1(x: float) -> int:
    return list(islice((n for n in naturales()
                        if abs(1 - sin(1/n)/(1/n)) < x), 1))[0]

# # 2ª definición de errorLimSeno
# # ============================

def errorLimSeno2(x: float) -> int:
    def aux(n: int) -> int:
        if abs(1 - sin(1/n)/(1/n)) < x:
            return n
        return aux(n + 1)

    return aux(1)

# 3ª definición de errorLimSeno
# ============================

def errorLimSeno3(x: float) -> int:
    return list(islice(dropwhile(lambda n: abs(1 - sin(1/n)/(1/n)) >= x,
                                 naturales()),
                       1))[0]


# Comprobación de equivalencia de errorLimSeno
# ============================================

@given(st.integers(min_value=1, max_value=100))
def test_errorLimSeno(n: int) -> None:
    r = errorLimSeno1(n)
    assert errorLimSeno2(n) == r
    assert errorLimSeno3(n) == r

# La comprobación es
#    src> poetry run pytest -q limite_del_seno.py
#    2 passed in 0.60s

# Comparación de eficiencia de errorLimSeno
# =========================================

# La comparación es
#    >>> tiempo('errorLimSeno1(10**(-12))')
#    0.07 segundos
#    >>> tiempo('errorLimSeno2(10**(-12))')
#    Process Python violación de segmento (core dumped)
#    >>> tiempo('errorLimSeno3(10**(-12))')
#    0.10 segundos
