# Bandera_tricolor.py
# La bandera tricolor.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-febrero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El problema de la bandera tricolor consiste en lo siguiente: Dada un
# lista de objetos xs que pueden ser rojos, amarillos o morados, se pide
# devolver una lista ys que contiene los elementos de xs, primero los
# rojos, luego los amarillos y por último los morados.
#
# Definir el tipo de dato Color para representar los colores con los
# constructores R, A y M correspondientes al rojo, azul y morado y la
# función
#    banderaTricolor :: [Color] -> [Color]
# tal que (banderaTricolor xs) es la bandera tricolor formada con los
# elementos de xs. Por ejemplo,
#    banderaTricolor [M,R,A,A,R,R,A,M,M]  ==  [R,R,R,A,A,A,M,M,M]
#    banderaTricolor [M,R,A,R,R,A]        ==  [R,R,R,A,A,M]
# ---------------------------------------------------------------------

# pylint: disable=dangerous-default-value

from enum import IntEnum
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis.strategies import lists, sampled_from

setrecursionlimit(10**6)

class Color(IntEnum):
    R = 0
    A = 1
    M = 2

    def __repr__(self) -> str:
        return self.name

R = Color.R
A = Color.A
M = Color.M

# 1ª solución
# ===========

def banderaTricolor1(xs: list[Color]) -> list[Color]:
    return [x for x in xs if x == R] + \
           [x for x in xs if x == A] + \
           [x for x in xs if x == M]

# 2ª solución
# ===========

def banderaTricolor2(xs: list[Color]) -> list[Color]:
    def colores(c: Color) -> list[Color]:
        return list(filter(lambda x: x == c, xs))
    return colores(R) + colores(A) + colores(M)

# 3ª solución
# ===========

def banderaTricolor3(xs: list[Color]) -> list[Color]:
    return sum([[x for x in xs if x == c] for c in [R, A, M]], [])

# 4ª solución
# ===========

def banderaTricolor4(xs: list[Color]) -> list[Color]:
    def aux(ys: list[Color],
            rs: list[Color] = [],
            as_: list[Color] = [],
            ms: list[Color] = []) -> list[Color]:
        if not ys:
            return rs + as_ + ms
        match ys[0]:
            case Color.R:
                return aux(ys[1:], [ys[0]] + rs, as_, ms)
            case Color.A:
                return aux(ys[1:], rs, [ys[0]] + as_, ms)
            case Color.M:
                return aux(ys[1:], rs, as_, [ys[0]] + ms)
    return aux(xs)

# 5ª solución
# ===========

def banderaTricolor5(xs: list[Color]) -> list[Color]:
    return sorted(xs)

# Verificación
# ============

def test_banderaTricolor() -> None:
    for banderaTricolor in [banderaTricolor1, banderaTricolor2,
                            banderaTricolor3, banderaTricolor4,
                            banderaTricolor5]:
        assert banderaTricolor([M,R,A,A,R,R,A,M,M])  ==  [R,R,R,A,A,A,M,M,M]
        assert banderaTricolor([M,R,A,R,R,A])        ==  [R,R,R,A,A,M]
        print(f"Verificado {banderaTricolor.__name__}")

# La verificación es
#    >>> test_banderaTricolor()
#    Verificado banderaTricolor1
#    Verificado banderaTricolor2
#    Verificado banderaTricolor3
#    Verificado banderaTricolor4
#    Verificado banderaTricolor5

# Comprobación de equivalencia
# ============================

@given(lists(sampled_from([R, A, M]), min_size=1))
def test_banderaTricolor_equiv(xs: list[Color]) -> None:
    r = banderaTricolor1(xs)
    assert r == banderaTricolor3(xs)
    assert r == banderaTricolor4(xs)
    assert r == banderaTricolor5(xs)

# La comprobación es
#    >>> test_banderaTricolor_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

def bandera(n: int) -> list[Color]:
    return [c for c in [M, R, A] for _ in range(n)]

# La comparación es
#    >>> tiempo('banderaTricolor1(bandera(6000))')
#    0.01 segundos
#    >>> tiempo('banderaTricolor2(bandera(6000))')
#    0.02 segundos
#    >>> tiempo('banderaTricolor3(bandera(6000))')
#    0.01 segundos
#    >>> tiempo('banderaTricolor4(bandera(6000))')
#    1.27 segundos
#    >>> tiempo('banderaTricolor5(bandera(6000))')
#    0.00 segundos
#
#    >>> tiempo('banderaTricolor1(bandera(10**7))')
#    3.97 segundos
#    >>> tiempo('banderaTricolor2(bandera(10**7))')
#    5.35 segundos
#    >>> tiempo('banderaTricolor3(bandera(10**7))')
#    3.25 segundos
#    >>> tiempo('banderaTricolor5(bandera(10**7))')
#    1.17 segundos
