# Relaciones_totales.py
# Relaciones totales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 11-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    total : (Rel[A]) -> bool
# tal que total(r) se verifica si la relación r es total; es decir, si
# para cualquier par x, y de elementos del universo de r, se tiene que
# x está relacionado con y o y está relacionado con x. Por ejemplo,
#    total (([1,3],[(1,1),(3,1),(3,3)]))  ==  True
#    total (([1,3],[(1,1),(3,1)]))        ==  False
#    total (([1,3],[(1,1),(3,3)]))        ==  False
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Relaciones_binarias import Rel, relacionArbitraria

A = TypeVar('A')

# 1ª solución
# ===========

def total(r: Rel[A]) -> bool:
    (u, g) = r
    return all(((x, y) in g or (y, x) in g for x in u for y in u))

# 2ª solución
# ===========

# producto(xs, ys) es el producto cartesiano de xs e ys. Por ejemplo,
#    >>> producto([2, 5], [1, 4, 6])
#    [(2, 1), (2, 4), (2, 6), (5, 1), (5, 4), (5, 6)]
def producto(xs: list[A], ys: list[A]) -> list[tuple[A,A]]:
    return [(x, y) for x in xs for y in ys]

# relacionados(g, (x, y)) se verifica si los elementos x e y están
# relacionados por la relación de grafo g. Por ejemplo,
#    relacionados([(2, 3), (3, 1)], (2, 3))  ==  True
#    relacionados([(2, 3), (3, 1)], (3, 2))  ==  True
#    relacionados([(2, 3), (3, 1)], (1, 2))  ==  False
def relacionados(g: list[tuple[A,A]], p: tuple[A,A]) -> bool:
    (x, y) = p
    return (x, y) in g or (y, x) in g

def total2(r: Rel[A]) -> bool:
    (u, g) = r
    return all(relacionados(g, p) for p in producto(u, u))

# 3ª solución
# ===========

def total3(r: Rel[A]) -> bool:
    u, g = r
    return all(relacionados(g, (x, y)) for x in u for y in u)

# 4ª solución
# ===========

def total4(r: Rel[A]) -> bool:
    (u, g) = r
    def aux2(x: A, ys: list[A]) -> bool:
        if not ys:
            return True
        return relacionados(g, (x, ys[0])) and aux2(x, ys[1:])

    def aux1(xs: list[A]) -> bool:
        if not xs:
            return True
        return aux2(xs[0], u) and aux1(xs[1:])

    return aux1(u)

# 5ª solución
# ===========

def total5(r: Rel[A]) -> bool:
    (u, g) = r
    for x in u:
        for y in u:
            if not relacionados(g, (x, y)):
                return False
    return True

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_total(n: int) -> None:
    r = relacionArbitraria(n)
    res = total(r)
    assert total2(r) == res
    assert total3(r) == res
    assert total4(r) == res
    assert total5(r) == res

# La comprobación es
#    > poetry run pytest -q Relaciones_totales.py
#    1 passed in 0.11s
