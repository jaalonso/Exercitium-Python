# mayuscula_inicial.py
# Poner en mayúscula la primera letra y las restantes en minúsculas
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    mayusculaInicial : (str) -> str
# tal que mayusculaInicial(xs) es la palabra xs con la letra inicial
# en mayúscula y las restantes en minúsculas. Por ejemplo,
#    mayusculaInicial("sEviLLa")  ==  "Sevilla"
#    mayusculaInicial("")         ==  ""
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def mayusculaInicial1(xs: str) -> str:
    if xs:
        return "".join([xs[0].upper()] + [y.lower() for y in xs[1:]])
    return ""

# 2ª solución
# ===========

def mayusculaInicial2(xs: str) -> str:
    def aux(ys: str) -> str:
        if ys:
            return ys[0].lower() + aux(ys[1:])
        return ""
    if xs:
        return "".join(xs[0].upper() + aux(xs[1:]))
    return ""

# 3ª solución
# ===========

def mayusculaInicial3(xs: str) -> str:
    if xs:
        return "".join([xs[0].upper()] + list(map(str.lower, xs[1:])))
    return ""

# 4ª solución
# ===========

def mayusculaInicial4(xs: str) -> str:
    return xs.capitalize()

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.text())
def test_mayusculaInicial(xs: str) -> None:
    r = mayusculaInicial1(xs)
    assert mayusculaInicial2(xs) == r
    assert mayusculaInicial3(xs) == r

# La comprobación es
#    src> poetry run pytest -q mayuscula_inicial.py
#    1 passed in 0.26s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('len(mayusculaInicial1("aB"*(10**7)))')
#    1.92 segundos
#    >>> tiempo('len(mayusculaInicial2("aB"*(10**7)))')
#    Process Python terminado (killed)
#    >>> tiempo('len(mayusculaInicial3("aB"*(10**7)))')
#    1.59 segundos
#    >>> tiempo('len(mayusculaInicial4("aB"*(10**7)))')
#    0.13 segundos
