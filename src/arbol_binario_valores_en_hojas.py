# arbol_binario_valores_en_hojas.py
# El tipo de los árboles binarios con valores en las hojas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-diciembre-2022
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
# usando el tipo de los árboles binarios con valores en las hojas
# definido como se muestra a continuación.

from dataclasses import dataclass
from random import randint
from typing import Generic, TypeVar

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

# Generador
# =========

# arbolArbitrario(n) es un árbol aleatorio de orden n. Por ejemplo,
#    >>> arbolArbitrario(2)
#    Nodo(i=Nodo(i=Hoja(x=6), d=Hoja(x=3)), d=Nodo(i=Hoja(x=4), d=Hoja(x=4)))
#    >>> arbolArbitrario(2)
#    Nodo(i=Nodo(i=Hoja(x=9), d=Hoja(x=6)), d=Nodo(i=Hoja(x=9), d=Hoja(x=8)))
def arbolArbitrario(n: int) -> Arbol[int]:
    if n == 0:
        return Hoja(randint(1, 10))
    if n == 1:
        return Nodo(arbolArbitrario(0), arbolArbitrario(0))
    k = min(randint(1, n + 1), n - 1)
    return Nodo(arbolArbitrario(k), arbolArbitrario(n - k))
