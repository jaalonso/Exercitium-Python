# Arbol_con_las_hojas_en_la_profundidad_dada.py
# Árbol con las hojas en la profundidad dada.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-diciembre-2022
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
#    creaArbol : (int) -> Arbol[Any]:
# tal que creaArbol(n) es el árbol cuyas hoyas están en la profundidad
# n. Por ejemplo,
#    >>> creaArbol(2)
#    Nodo(Nodo(Hoja(None), Hoja(None)), Nodo(Hoja(None), Hoja(None)))
# ---------------------------------------------------------------------

from dataclasses import dataclass
from typing import Any, Generic, TypeVar

A = TypeVar("A")

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

def creaArbol(h: int) -> Arbol[Any]:
    if h <= 0:
        return Hoja(None)
    x = creaArbol(h - 1)
    return Nodo(x, x)
