# mayusculas_iniciales.py
# Mayúsculas iniciales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se consideran las siguientes reglas de mayúsculas iniciales para los
# títulos:
# + la primera palabra comienza en mayúscula y
# + todas las palabras que tienen 4 letras como mínimo empiezan con
#   mayúsculas
#
# Definir la función
#    titulo : (list[str]) -> list[str]
# tal que titulo(ps) es la lista de las palabras de ps con
# las reglas de mayúsculas iniciales de los títulos. Por ejemplo,
#    >>> titulo(["eL", "arTE", "DE", "La", "proGraMacion"])
#    ["El", "Arte", "de", "la", "Programacion"]
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

# (mayusculaInicial xs) es la palabra xs con la letra inicial
# en mayúscula y las restantes en minúsculas. Por ejemplo,
#    mayusculaInicial("sEviLLa")  ==  "Sevilla"
def mayusculaInicial(xs: str) -> str:
    return xs.capitalize()

# (minuscula xs) es la palabra xs en minúscula.
def minuscula(xs: str) -> str:
    return xs.lower()

# (transforma p) es la palabra p con mayúscula inicial si su longitud
# es mayor o igual que 4 y es p en minúscula en caso contrario
def transforma(p: str) -> str:
    if len(p) >= 4:
        return mayusculaInicial(p)
    return minuscula(p)

def titulo1(ps: list[str]) -> list[str]:
    if ps:
        return [mayusculaInicial(ps[0])] + [transforma(q) for q in ps[1:]]
    return []

# 2ª solución
# ===========

def titulo2(ps: list[str]) -> list[str]:
    def aux(qs: list[str]) -> list[str]:
        if qs:
            return [transforma(qs[0])] + aux(qs[1:])
        return []
    if ps:
        return [mayusculaInicial(ps[0])] + aux(ps[1:])
    return []

# 3ª solución
# ===========

def titulo3(ps: list[str]) -> list[str]:
    if ps:
        return [mayusculaInicial(ps[0])] + list(map(transforma, ps[1:]))
    return []

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.text()))
def test_titulo(ps: list[str]) -> None:
    r = titulo1(ps)
    assert titulo2(ps) == r
    assert titulo3(ps) == r

# La comprobación es
#    src> poetry run pytest -q mayusculas_iniciales.py
#    1 passed in 0.55s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('len(mayusculaInicial1("aB"*(10**7)))')
#    >>> tiempo('titulo1(["eL","arTE","DE","La","proGraMacion "]*1900)')
#    0.00 segundos
#    >>> tiempo('titulo2(["eL","arTE","DE","La","proGraMacion "]*1900)')
#    0.30 segundos
#    >>> tiempo('titulo3(["eL","arTE","DE","La","proGraMacion "]*1900)')
#    0.00 segundos
#
#    >>> tiempo('titulo1(["eL","arTE","DE","La","proGraMacion "]*(2*10**6))')
#    2.93 segundos
#    >>> tiempo('titulo3(["eL","arTE","DE","La","proGraMacion "]*(2*10**6))')
#    2.35 segundos
