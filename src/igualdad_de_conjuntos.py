# igualdad_de_conjuntos.py
# Igualdad de conjuntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    iguales : (list[Any], list[Any]) -> bool
# tal que iguales(xs, ys) se verifica si xs e ys son iguales. Por
# ejemplo,
#    iguales([3, 2, 3], [2, 3])    == True
#    iguales([3, 2, 3], [2, 3, 2]) == True
#    iguales([3, 2, 3], [2, 3, 4]) == False
#    iguales([2, 3], [4, 5])       == False
# ---------------------------------------------------------------------

from typing import Any
from timeit import Timer, default_timer
from hypothesis import given, strategies as st

# 1ª solución
# ===========

def subconjunto(xs: list[Any],
                ys: list[Any]) -> bool:
    return [x for x in xs if x in ys] == xs

def iguales1(xs: list[Any],
             ys: list[Any]) -> bool:
    return subconjunto(xs, ys) and subconjunto(ys, xs)

# 2ª solución
# ===========

def iguales2(xs: list[Any],
             ys: list[Any]) -> bool:
    return set(xs) == set(ys)

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.lists(st.integers()),
       st.lists(st.integers()))
def test_iguales(xs, ys):
    assert iguales1(xs, ys) == iguales2(xs, ys)

# La comprobación es
#    src> poetry run pytest -q igualdad_de_conjuntos.py
#    1 passed in 0.28s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo medio (en segundos) de 10 evaluaciones de la expresión e.
    """
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> xs = list(range(20000))
#    >>> tiempo('iguales1(xs, xs)')
#    2.71 segundos
#    >>> tiempo('iguales2(xs, xs)')
#    0.01 segundos
