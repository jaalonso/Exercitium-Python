# suma_de_digitos_de_cadena.py
# Suma de los dígitos de una cadena.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 8-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    sumaDigitos : (str) -> int
# tal que sumaDigitos(xs) es la suma de los dígitos de la cadena
# xs. Por ejemplo,
#    sumaDigitos("SE 2431 X")  ==  10
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def sumaDigitos1(xs: str) -> int:
    return sum((int(x) for x in xs if x.isdigit()))

# 2ª solución
# ===========

def sumaDigitos2(xs: str) -> int:
    if xs:
        if xs[0].isdigit():
            return int(xs[0]) + sumaDigitos2(xs[1:])
        return sumaDigitos2(xs[1:])
    return 0

# 3ª solución
# ===========

def sumaDigitos3(xs: str) -> int:
    r = 0
    for x in xs:
        if x.isdigit():
            r = r + int(x)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.text())
def test_sumaDigitos(xs: str) -> None:
    r = sumaDigitos1(xs)
    assert sumaDigitos2(xs) == r
    assert sumaDigitos3(xs) == r

# La comprobación es
#    src> poetry run pytest -q suma_de_digitos_de_cadena.py
#    1 passed in 0.41s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('sumaDigitos1("ab12"*5000)')
#    0.00 segundos
#    >>> tiempo('sumaDigitos2("ab12"*5000)')
#    0.02 segundos
#    >>> tiempo('sumaDigitos3("ab12"*5000)')
#    0.00 segundos
#
#    >>> tiempo('sumaDigitos1("ab12"*(5*10**6))')
#    1.60 segundos
#    >>> tiempo('sumaDigitos3("ab12"*(5*10**6))')
#    1.83 segundos
