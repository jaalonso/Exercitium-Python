# arboles_con_igual_estructura.py
# Árboles con igual estructura.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-diciembre-2022
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
# Por ejemplo, los árboles
#         5              8             5           5
#        / \            / \           / \         / \
#       /   \          /   \         /   \       /   \
#      9     7        9     3       9     2     4     7
#     / \   / \      / \   / \     / \               / \
#    1   4 6   8    1   4 6   2   1   4             6   2
# se pueden representar por
#     ej3arbol1: Arbol[int] = N(5, N(9, H(1), H(4)), N(7, H(6), H(8)))
#     ej3arbol2: Arbol[int] = N(8, N(9, H(1), H(4)), N(3, H(6), H(2)))
#     ej3arbol3: Arbol[int] = N(5, N(9, H(1), H(4)), H(2))
#     ej3arbol4: Arbol[int] = N(5, H(4), N(7, H(6), H(2)))
#
# Definir la función
#    igualEstructura : (Arbol[A], Arbol[A]) -> bool
# tal que igualEstructura(a1, a2) se verifica si los árboles a1 y a2
# tienen la misma estructura. Por ejemplo,
#    igualEstructura(ej3arbol1, ej3arbol2) == True
#    igualEstructura(ej3arbol1, ej3arbol3) == False
#    igualEstructura(ej3arbol1, ej3arbol4) == False
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

ej3arbol1: Arbol[int] = N(5, N(9, H(1), H(4)), N(7, H(6), H(8)))
ej3arbol2: Arbol[int] = N(8, N(9, H(1), H(4)), N(3, H(6), H(2)))
ej3arbol3: Arbol[int] = N(5, N(9, H(1), H(4)), H(2))
ej3arbol4: Arbol[int] = N(5, H(4), N(7, H(6), H(2)))

def igualEstructura(a: Arbol[A], b: Arbol[A]) -> bool:
    match (a, b):
        case (H(_), H(_)):
            return True
        case (N(_, i1, d1), N(_, i2, d2)):
            return igualEstructura(i1, i2) and igualEstructura(d1, d2)
        case (_, _):
            return False
    assert False
