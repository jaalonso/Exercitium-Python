# altura_de_un_arbol_binario.py
# Altura de un árbol binario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-diciembre-2022
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
#        x: int
#
#    @dataclass
#    class Nodo(Arbol[A]):
#        i: Arbol
#        d: Arbol
#
# Definir la función
#    altura : (Arbol) -> int
# tal que altura(t) es la altura del árbol t. Por ejemplo,
#    >>> altura(Hoja(1))
#    0
#    >>> altura(Nodo(Hoja(1), Hoja(6)))
#    1
#    >>> altura(Nodo(Nodo(Hoja(1), Hoja(6)), Hoja(2)))
#    2
#    >>> altura(Nodo(Nodo(Hoja(1), Hoja(6)), Nodo(Hoja(2), Hoja(7))))
#    2
# ---------------------------------------------------------------------

from dataclasses import dataclass
from typing import Generic, TypeVar

A = TypeVar("A")

@dataclass
class Arbol(Generic[A]):
    pass

@dataclass
class Hoja(Arbol[A]):
    x: int

@dataclass
class Nodo(Arbol[A]):
    i: Arbol[A]
    d: Arbol[A]

def altura(a: Arbol[A]) -> int:
    match a:
        case Hoja(_):
            return 0
        case Nodo(i, d):
            return 1 + max(altura(i), altura(d))
    assert False
