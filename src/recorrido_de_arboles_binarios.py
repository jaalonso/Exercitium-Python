# recorrido_de_arboles_binarios.py
# Recorrido de árboles binarios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El árbol binario
#         9
#        / \
#       /   \
#      3     7
#     / \
#    2   4
# se puede representar por
#    N 9 (N 3 (H 2) (H 4)) (H 7)
#
# El tipo de los árboles binarios se puede definir por
#    @dataclass
#    class Arbol(Generic[A]):
#        pass
#
#    @dataclass
#    class H(Arbol[A]):
#        x: A
#
#    @dataclass
#    class N(Arbol[A]):
#        x: A
#        i: Arbol[A]
#        d: Arbol[A]
#
# Definir las funciones
#    preorden  : (Arbol[A]) -> list[A]
#    postorden : (Arbol[A]) -> list[A]
# tales que
# + preorden(x) es la lista correspondiente al recorrido preorden del
#   árbol x; es decir, primero visita la raíz del árbol, a continuación
#   recorre el subárbol izquierdo y, finalmente, recorre el subárbol
#   derecho. Por ejemplo,
#      >>> preorden(N(9, N(3, H(2), H(4)), H(7)))
#      [9, 3, 2, 4, 7]
# + (postorden x) es la lista correspondiente al recorrido postorden
#   del árbol x; es decir, primero recorre el subárbol izquierdo, a
#   continuación el subárbol derecho y, finalmente, la raíz del
#   árbol. Por ejemplo,
#      >>> postorden(N(9, N(3, H(2), H(4)), H(7)))
#      [2, 4, 3, 7, 9]
#
# Comprobar con QuickCheck que la longitud de la lista
# obtenida recorriendo un árbol en cualquiera de los sentidos es igual
# al número de nodos del árbol más el número de hojas.
# ---------------------------------------------------------------------

from dataclasses import dataclass
from random import choice, randint
from typing import Generic, TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar("A")

@dataclass
class Arbol(Generic[A]):
    pass

@dataclass
class H(Arbol[A]):
    x: A

@dataclass
class N(Arbol[A]):
    x: A
    i: Arbol[A]
    d: Arbol[A]

def preorden(a: Arbol[A]) -> list[A]:
    match a:
        case H(x):
            return [x]
        case N(x, i, d):
            return [x] + preorden(i) + preorden(d)
    assert False

def postorden(a: Arbol[A]) -> list[A]:
    match a:
        case H(x):
            return [x]
        case N(x, i, d):
            return postorden(i) + postorden(d) + [x]
    assert False

# Comprobación de la propiedad
# ============================

# (arbolArbitrario n) es un árbol aleatorio de orden n. Por ejemplo,
#    >>> arbolArbitrario(4)
#    N(x=2, i=H(x=1), d=H(x=9))
#    >>> arbolArbitrario(4)
#    H(x=10)
#    >>> arbolArbitrario(4)
#    N(x=4, i=N(x=7, i=H(x=4), d=H(x=0)), d=H(x=6))
def arbolArbitrario(n: int) -> Arbol[int]:
    if n <= 1:
        return H(randint(0, 10))
    m = n // 2
    return choice([H(randint(0, 10)),
                   N(randint(0, 10),
                     arbolArbitrario(m),
                     arbolArbitrario(m))])

# nNodos(x) es el número de nodos del árbol x. Por ejemplo,
#    nNodos(N(9, N(3, H(2), H(4)), H(7)))  ==  2
def nNodos(a: Arbol[A]) -> int:
    match a:
        case H(_):
            return 0
        case N(_, i, d):
            return 1 + nNodos(i) + nNodos(d)
    assert False

# (nHojas x) es el número de hojas del árbol x. Por ejemplo,
#    nHojas (N 9 (N 3 (H 2) (H 4)) (H 7))  ==  3
def nHojas(a: Arbol[A]) -> int:
    match a:
        case H(_):
            return 1
        case N(_, i, d):
            return nHojas(i) + nHojas(d)
    assert False

# La propiedad es
@given(st.integers(min_value=1, max_value=10))
def test_recorrido(n: int) -> None:
    a = arbolArbitrario(n)
    m = nNodos(a) + nHojas(a)
    assert len(preorden(a)) == m
    assert len(postorden(a)) == m

# La comprobación es
#    src> poetry run pytest -q recorrido_de_arboles_binarios.py
#    1 passed in 0.16s
