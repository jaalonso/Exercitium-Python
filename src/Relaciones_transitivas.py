# Relaciones_transitivas.py
# Relaciones transitivas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 05-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    transitiva : (Rel[A]) -> bool
# tal que transitiva(r) se verifica si la relación r es transitiva.
# Por ejemplo,
#    >>> transitiva(([1, 3, 5], [(1, 1), (1, 3), (3, 1), (3, 3), (5, 5)]))
#    True
#    >>> transitiva(([1, 3, 5], [(1, 1), (1, 3), (3, 1), (5, 5)]))
#    False
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Composicion_de_relaciones_binarias_v2 import composicion
from src.Reconocimiento_de_subconjunto import subconjunto
from src.Relaciones_binarias import Rel, relacionArbitraria
from src.Universo_y_grafo_de_una_relacion_binaria import grafo

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

def transitiva1(r: Rel[A]) -> bool:
    g = grafo(r)
    return subconjunto(grafo(composicion(r, r)), g)

# La función subconjunto está definida en el ejercicio
# "Reconocimiento de subconjunto" que se encuentra en
# https://bit.ly/427Tyeq
#
# La función grafo está definida en el ejercicio
# "Universo y grafo de una relación binaria" que se encuentra en
# https://bit.ly/3J35mpC
#
# La función composición está definida en el ejercicio
# "Composición de relaciones binarias" que se encuentra en
# https://bit.ly/3JyJrs7

# 2ª solución
# ===========

def transitiva2(r: Rel[A]) -> bool:
    g = grafo(r)
    def aux(g1: list[tuple[A,A]]) -> bool:
        if not g1:
            return True
        (x, y) = g1[0]
        return all(((x, z) in g for (u,z) in g if u == y)) and aux(g1[1:])

    return aux(g)

# 3ª solución
# ===========

def transitiva3(r: Rel[A]) -> bool:
    g = grafo(r)
    g1 = list(g)
    for (x, y) in g1:
        if not all(((x, z) in g for (u,z) in g if u == y)):
            return False
    return True


# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_simetrica(n: int) -> None:
    r = relacionArbitraria(n)
    res = transitiva1(r)
    assert transitiva2(r) == res
    assert transitiva3(r) == res

# La comprobación es
#    > poetry run pytest -q Relaciones_transitivas.py
#    1 passed in 0.12s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> u1 = range(6001)
#    >>> g1 = [(x, x+1) for x in range(6000)]
#    >>> tiempo("transitiva1((u1, g1))")
#    1.04 segundos
#    >>> tiempo("transitiva2((u1, g1))")
#    0.00 segundos
#    >>> tiempo("transitiva3((u1, g1))")
#    0.00 segundos
#
#    >>> u2 = range(60)
#    >>> g2 = [(x, y) for x in u2 for y in u2]
#    >>> tiempo("transitiva1((u2, g2))")
#    0.42 segundos
#    >>> tiempo("transitiva2((u2, g2))")
#    5.24 segundos
#    >>> tiempo("transitiva3((u2, g2))")
#    4.83 segundos

# En lo sucesivo usaremos la 1ª definición
transitiva = transitiva1
