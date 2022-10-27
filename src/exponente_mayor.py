# exponente_mayor.py
# Exponente_de la mayor potencia de x que divide a y.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    mayorExponente : (int, int) -> int
# tal que mayorExponente(a, b) es el exponente de la mayor potencia de
# a que divide b. Por ejemplo,
#    mayorExponente(2, 8)    ==  3
#    mayorExponente(2, 9)    ==  0
#    mayorExponente(5, 100)  ==  2
#    mayorExponente(2, 60)   ==  2
#
# Nota: Se supone que a > 1 y b > 0.
# ---------------------------------------------------------------------

from itertools import islice
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def mayorExponente1(a: int, b: int) -> int:
    if b % a != 0:
        return 0
    return 1 + mayorExponente1(a, b // a)

# 2ª solución
# ===========

def mayorExponente2(a: int, b: int) -> int:
    def aux(c: int, r: int) -> int:
        if c % a != 0:
            return r
        return aux(c // a, r + 1)
    return aux(b, 0)

# 3ª solución
# ===========

# naturales es el generador de los números naturales, Por ejemplo,
#    >>> list(islice(naturales(), 5))
#    [0, 1, 2, 3, 4]
def naturales() -> Iterator[int]:
    i = 0
    while True:
        yield i
        i += 1

def mayorExponente3(a: int, b: int) -> int:
    return list(islice((x - 1 for x in naturales() if b % (a**x) != 0), 1))[0]

# 4ª solución
# ===========

def mayorExponente4(a: int, b: int) -> int:
    r = 0
    while b % a == 0:
        b = b // a
        r = r + 1
    return r

# Comprobación de equivalencia
# ============================

def prueba1() -> None:
    for x in range(2, 11):
        for y in range(1, 11):
            print(x, y, mayorExponente4(x, y))


# La propiedad es
@given(st.integers(min_value=2, max_value=10),
       st.integers(min_value=1, max_value=10))
def test_mayorExponente(a: int, b: int) -> None:
    r = mayorExponente1(a, b)
    assert mayorExponente2(a, b) == r
    assert mayorExponente3(a, b) == r
    assert mayorExponente4(a, b) == r

# La comprobación es
#    src> poetry run pytest -q exponente_mayor.py
#    1 passed in 0.16s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('mayorExponente1(2, 2**(2*10**4))')
#    0.13 segundos
#    >>> tiempo('mayorExponente2(2, 2**(2*10**4))')
#    0.13 segundos
#    >>> tiempo('mayorExponente3(2, 2**(2*10**4))')
#    1.81 segundos
#    >>> tiempo('mayorExponente4(2, 2**(2*10**4))')
#    0.12 segundos
#
#    >>> tiempo('mayorExponente4(2, 2**(2*10**5))')
#    12.19 segundos
