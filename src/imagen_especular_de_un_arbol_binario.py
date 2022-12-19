# imagen_especular_de_un_arbol_binario.py
# Imagen especular de un árbol binario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-diciembre-2022
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
# Definir la función
#    espejo : (Arbol[A]) -> Arbol[A]
# tal que espejo(x) es la imagen especular del árbol x. Por ejemplo,
#    espejo(N(9, N(3, H(2), H(4)), H(7))) == N(9, H(7), N(3, H(4), H(2)))
#
# Comprobar con Hypothesis las siguientes propiedades, para todo árbol
# x,
#    espejo(espejo(x)) = x
#    list(reversed(preorden(espejo(x)))) == postorden(x)
#    postorden(espejo(x)) == list(reversed(preorden(x)))
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

def espejo(a: Arbol[A]) -> Arbol[A]:
    match a:
        case H(x):
            return H(x)
        case N(x, i, d):
            return N(x, espejo(d), espejo(i))
    assert False

# Generador para las comprobaciones
# =================================

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

# Funciones auxiliares para la comprobación
# =========================================

# preorden(x) es la lista correspondiente al recorrido preorden del
# árbol x; es decir, primero visita la raíz del árbol, a continuación
# recorre el subárbol izquierdo y, finalmente, recorre el subárbol
# derecho. Por ejemplo,
#    >>> preorden(N(9, N(3, H(2), H(4)), H(7)))
#    [9, 3, 2, 4, 7]
def preorden(a: Arbol[A]) -> list[A]:
    match a:
        case H(x):
            return [x]
        case N(x, i, d):
            return [x] + preorden(i) + preorden(d)
    assert False

# (postorden x) es la lista correspondiente al recorrido postorden
# del árbol x; es decir, primero recorre el subárbol izquierdo, a
# continuación el subárbol derecho y, finalmente, la raíz del
# árbol. Por ejemplo,
#    >>> postorden(N(9, N(3, H(2), H(4)), H(7)))
#    [2, 4, 3, 7, 9]
def postorden(a: Arbol[A]) -> list[A]:
    match a:
        case H(x):
            return [x]
        case N(x, i, d):
            return postorden(i) + postorden(d) + [x]
    assert False

# Comprobación de las propiedades
# ===============================

# Las propiedades son
@given(st.integers(min_value=1, max_value=10))
def test_espejo_espejo(n: int) -> None:
    x = arbolArbitrario(n)
    print(x)
    assert espejo(espejo(x)) == x
    assert list(reversed(preorden(espejo(x)))) == postorden(x)
    assert postorden(espejo(x)) == list(reversed(preorden(x)))

# La comprobación es
#    src> poetry run pytest -q imagen_especular_de_un_arbol_binario.py
#    1 passed in 0.16s
