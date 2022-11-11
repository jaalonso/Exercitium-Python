# posiciones_de_un_caracter_en_una_cadena.py
# Posiciones de un carácter en una cadena.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 11-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    posiciones : (str, str) -> list[int]
# tal que (posiciones x ys) es la lista de la posiciones del carácter x
# en la cadena ys. Por ejemplo,
#    posiciones('a', "Salamamca")   ==  [1,3,5,8]
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# -- 1ª solución
# -- ===========

def posiciones1(x: str, ys: str) -> list[int]:
    return [n for (n, y) in enumerate(ys) if y == x]

# -- 2ª solución
# -- ===========

def posiciones2(x: str, ys: str) -> list[int]:
    def aux(a: str, bs: str, n: int) -> list[int]:
        if bs:
            if a == bs[0]:
                return [n] + aux(a, bs[1:], n + 1)
            return aux(a, bs[1:], n + 1)
        return []
    return aux(x, ys, 0)

# -- 3ª solución
# -- ===========

def posiciones3(x: str, ys: str) -> list[int]:
    r = []
    for n, y in enumerate(ys):
        if x == y:
            r.append(n)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.text(), st.text())
def test_posiciones(x: str, ys: str) -> None:
    r = posiciones1(x, ys)
    assert posiciones2(x, ys) == r
    assert posiciones3(x, ys) == r

# La comprobación es
#    src> poetry run pytest -q posiciones_de_un_caracter_en_una_cadena.py
#    1 passed in 0.29s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('posiciones1("a", "abc"*6000)')
#    0.00 segundos
#    >>> tiempo('posiciones2("a", "abc"*6000)')
#    0.06 segundos
#    >>> tiempo('posiciones3("a", "abc"*6000)')
#    0.00 segundos
#
#    >>> tiempo('posiciones1("a", "abc"*(2*10**7))')
#    3.02 segundos
#    >>> tiempo('posiciones3("a", "abc"*(2*10**7))')
#    3.47 segundos
