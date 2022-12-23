# rama_izquierda_de_un_arbol_binario.py
# Rama izquierda de un árbol binario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 26-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los árboles binarios con valores en los nodos se pueden definir por
#    @dataclass
#    class Arbol(Generic[A]):
#        pass
#
#    @dataclass
#    class H(Arbol[A]):
#        pass
#
#    @dataclass
#    class N(Arbol[A]):
#        x: A
#        i: Arbol[A]
#        d: Arbol[A]
# Por ejemplo, el árbol
#         9
#        / \
#       /   \
#      8     6
#     / \   / \
#    3   2 4   5
# se puede representar por
#    N(9, N(8, N(3, H(), H()), N(2, H(), H())), N(6, N(4, H(), H()), N(5, H(), H())))
#
# Definir la función
#    ramaIzquierda : (Arbol[A]) -> list[A]
# tal que ramaIzquierda(a) es la lista de los valores de los nodos de
# la rama izquierda del árbol a. Por ejemplo,
#    >>> ramaIzquierda(N(2, N(5, N(3, H(), H()), N(7, H(), H())), N(4, H(), H())))
#    [2, 5, 3]
# ---------------------------------------------------------------------

from dataclasses import dataclass
from typing import Generic, TypeVar

A = TypeVar("A")

@dataclass
class Arbol(Generic[A]):
    pass

@dataclass
class H(Arbol[A]):
    pass

@dataclass
class N(Arbol[A]):
    x: A
    i: Arbol[A]
    d: Arbol[A]

def ramaIzquierda(a: Arbol[A]) -> list[A]:
    match a:
        case H():
            return []
        case N(x, i, _):
            return [x] + ramaIzquierda(i)
    assert False
