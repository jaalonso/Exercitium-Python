# existencia_de_elemento_del_arbol_con_propiedad.py
# Existencia de elementos del árbol que verifican una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-diciembre-2022
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
#         5
#        / \
#       /   \
#      3     2
#     / \
#    1   4
# se representa por
#    N(5, N(3, H(1), H(4)), H(2))
#
# Definir la función
#    algunoArbol : (Arbol[A], Callable[[A], bool]) -> bool
# tal que algunoArbol(a, p) se verifica si algún elemento del árbol a
# cumple la propiedad p. Por ejemplo,
#    >>> algunoArbol(N(5, N(3, H(1), H(4)), H(2)), lambda x: x > 4)
#    True
#    >>> algunoArbol(N(5, N(3, H(1), H(4)), H(2)), lambda x: x > 7)
#    False
# ---------------------------------------------------------------------

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

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

def algunoArbol(a: Arbol[A], p: Callable[[A], bool]) -> bool:
    match a:
        case H(x):
            return p(x)
        case N(x, i, d):
            return p(x) or algunoArbol(i, p) or algunoArbol(d, p)
    assert False
