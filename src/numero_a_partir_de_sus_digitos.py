# numero_a_partir_de_sus_digitos.py
# Número a partir de sus dígitos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 31-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    listaNumero : (list[int]) -> int
# tal que listaNumero(xs) es el número formado por los dígitos xs. Por
# ejemplo,
#    listaNumero([5])           == 5
#    listaNumero([1, 3, 4, 7])  == 1347
#    listaNumero([0, 0, 1])     == 1
# ---------------------------------------------------------------------

from functools import reduce
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def listaNumero1(xs: list[int]) -> int:
    def aux(ys: list[int]) -> int:
        if ys:
            return ys[0] + 10 * aux(ys[1:])
        return 0
    return aux(list(reversed(xs)))

# 2ª solución
# ===========

def listaNumero2(xs: list[int]) -> int:
    def aux(r: int, ys: list[int]) -> int:
        if ys:
            return aux(ys[0] + 10 * r, ys[1:])
        return r
    return aux(0, xs)

# 3ª solución
# ===========

def listaNumero3(xs: list[int]) -> int:
    return reduce((lambda r, x: x + 10 * r), xs)

# 4ª solución
# ===========

def listaNumero4(xs: list[int]) -> int:
    r = 0
    for x in xs:
        r = x + 10 * r
    return r

# 5ª solución
# ===========

def listaNumero5(xs: list[int]) -> int:
    return sum((y * 10**n
                for (y, n) in zip(list(reversed(xs)), range(0, len(xs)))))

# 6ª solución
# ===========

def listaNumero6(xs: list[int]) -> int:
    return int("".join(list(map(str, xs))))

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers(min_value=0, max_value=9), min_size=1))
def test_listaNumero(xs: list[int]) -> None:
    r = listaNumero1(xs)
    assert listaNumero2(xs) == r
    assert listaNumero3(xs) == r
    assert listaNumero4(xs) == r
    assert listaNumero5(xs) == r
    assert listaNumero6(xs) == r

# La comprobación es
#    src> poetry run pytest -q numero_a_partir_de_sus_digitos.py
#    1 passed in 0.27s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('listaNumero1([9]*(10**4))')
#    0.28 segundos
#    >>> tiempo('listaNumero2([9]*(10**4))')
#    0.16 segundos
#    >>> tiempo('listaNumero3([9]*(10**4))')
#    0.01 segundos
#    >>> tiempo('listaNumero4([9]*(10**4))')
#    0.01 segundos
#    >>> tiempo('listaNumero5([9]*(10**4))')
#    0.41 segundos
#    >>> tiempo('listaNumero6([9]*(10**4))')
#    0.00 segundos
#
#    >>> tiempo('listaNumero3([9]*(2*10**5))')
#    3.45 segundos
#    >>> tiempo('listaNumero4([9]*(2*10**5))')
#    3.29 segundos
#    >>> tiempo('listaNumero6([9]*(2*10**5))')
#    0.19 segundos
