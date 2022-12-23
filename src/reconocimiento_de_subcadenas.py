# reconocimiento_de_subcadenas.py
# Reconocimiento de subcadenas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    esSubcadena : (str, str) -> bool
# tal que esSubcadena(xs ys) se verifica si xs es una subcadena de ys.
# Por ejemplo,
#    esSubcadena("casa", "escasamente")   ==  True
#    esSubcadena("cante", "escasamente")  ==  False
#    esSubcadena("", "")                  ==  True
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def esSubcadena1(xs: str, ys: str) -> bool:
    if not xs:
        return True
    if not ys:
        return False
    return ys.startswith(xs) or esSubcadena1(xs, ys[1:])

# 2ª solución
# ===========

# sufijos(xs) es la lista de sufijos de xs. Por ejemplo,
#    sufijos("abc")  ==  ['abc', 'bc', 'c', '']
def sufijos(xs: str) -> list[str]:
    return [xs[i:] for i in range(len(xs) + 1)]

def esSubcadena2(xs: str, ys: str) -> bool:
    return any(zs.startswith(xs) for zs in sufijos(ys))

# 3ª solución
# ===========

def esSubcadena3(xs: str, ys: str) -> bool:
    return xs in ys

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.text(), st.text())
def test_esSubcadena(xs: str, ys: str) -> None:
    r = esSubcadena1(xs, ys)
    assert esSubcadena2(xs, ys) == r
    assert esSubcadena3(xs, ys) == r

# La comprobación es
#    src> poetry run pytest -q reconocimiento_de_subcadenas.py
#    1 passed in 0.35s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('esSubcadena1("abc", "d"*(10**4) + "abc")')
#    0.02 segundos
#    >>> tiempo('esSubcadena2("abc", "d"*(10**4) + "abc")')
#    0.01 segundos
#    >>> tiempo('esSubcadena3("abc", "d"*(10**4) + "abc")')
#    0.00 segundos
#
#    >>> tiempo('esSubcadena2("abc", "d"*(10**5) + "abc")')
#    1.74 segundos
#    >>> tiempo('esSubcadena3("abc", "d"*(10**5) + "abc")')
#    0.00 segundos
