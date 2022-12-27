# elementos_del_nivel_k_de_un_arbol.py
# Elementos del nivel k de un árbol.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 2-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los árboles binarios con valores en las hojas y en los nodos se
# definen por
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
# Por ejemplo, el árbol
#         7
#        / \
#       /   \
#      2     9
#     / \
#    5   4
# se representa por
#    N(7, N(2, H(5), H(4)), H(9))
#
# Un elemento de un árbol se dirá de nivel k si aparece en el árbol a
# distancia k  de la raíz.
#
# Definir la función
#    nivel : (int, Arbol[A]) -> list[A]
# tal que nivel(k, a) es la lista de los elementos de nivel k del árbol
# a. Por ejemplo,
#     >>> nivel(0, N(7, N(2, H(5), H(4)), H(9)))
#     [7]
#     >>> nivel(1, N(7, N(2, H(5), H(4)), H(9)))
#     [2, 9]
#     >>> nivel(2, N(7, N(2, H(5), H(4)), H(9)))
#     [5, 4]
#     >>> nivel(3, N(7, N(2, H(5), H(4)), H(9)))
#     []
# ---------------------------------------------------------------------

from dataclasses import dataclass
from typing import Generic, TypeVar

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

def nivel(k: int, a: Arbol[A]) -> list[A]:
    match (k, a):
        case (0, H(x)):
            return [x]
        case (0, N(x, _, _)):
            return [x]
        case (_, H(_)):
            return []
        case (_, N(_, i, d)):
            return nivel(k - 1, i) + nivel(k - 1, d)
    assert False
