# arboles_con_la_misma_forma.py
# Árboles con la misma forma.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 8-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El árbol binario
#         ·
#        / \
#       /   \
#      ·     ·
#     / \   / \
#    1   4 6   9
# se puede representar por
#    ejArbol = Nodo(Nodo(Hoja(1), Hoja(4)),
#                   Nodo(Hoja(6), Hoja(9)))
#
#
# El tipo de los árboles binarios se puede definir por
#    @dataclass
#    class Arbol(Generic[A]):
#        pass
#
#    @dataclass
#    class Hoja(Arbol[A]):
#        x: A
#
#    @dataclass
#    class Nodo(Arbol[A]):
#        i: Arbol
#        d: Arbol
#
# Definir la función
#    mismaForma : (Arbol[A], Arbol[B]) -> bool
# tal que mismaForma(t1, t2) se verifica si t1 y t2 tienen la misma
# estructura. Por ejemplo,
#    >>> arbol1 = Hoja(5)
#    >>> arbol2 = Hoja(3)
#    >>> mismaForma(arbol1, arbol2)
#    True
#    >>> arbol3 = Nodo(Hoja(6), Hoja(7))
#    >>> mismaForma(arbol1, arbol3)
#    False
#    >>> arbol4 = Nodo(Hoja(9), Hoja(5))
#    >>> mismaForma(arbol3, arbol4)
#    True
# ---------------------------------------------------------------------

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

A = TypeVar("A")
B = TypeVar("B")

@dataclass
class Arbol(Generic[A]):
    pass

@dataclass
class Hoja(Arbol[A]):
    x: A

@dataclass
class Nodo(Arbol[A]):
    i: Arbol[A]
    d: Arbol[A]

# -- 1ª solución
# -- ===========

def mismaForma1(a: Arbol[A], b: Arbol[B]) -> bool:
    match (a, b):
        case (Hoja(_), Hoja(_)):
            return True
        case (Nodo(i1, d1), Nodo(i2, d2)):
            return mismaForma1(i1, i2) and mismaForma1(d1, d2)
        case (_, _):
            return False
    assert False

# -- 2ª solución
# -- ===========

# mapArbol(f, t) es el árbolo obtenido aplicando la función f a
# los elementos del árbol t. Por ejemplo,
#    >>> mapArbol(lambda x: 1 + x, Nodo(Hoja(2), Hoja(4)))
#    Nodo(i=Hoja(x=3), d=Hoja(x=5))
def mapArbol(f: Callable[[A], B], a: Arbol[A]) -> Arbol[B]:
    match a:
        case Hoja(x):
            return Hoja(f(x))
        case Nodo(i, d):
            return Nodo(mapArbol(f, i), mapArbol(f, d))
    assert False

def mismaForma2(a: Arbol[A], b: Arbol[B]) -> bool:
    return mapArbol(lambda x: 0, a) == mapArbol(lambda x: 0, b)
