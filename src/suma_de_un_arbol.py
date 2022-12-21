# suma_de_un_arbol.py
# Suma de un árbol.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los árboles binarios con valores en los nodos se pueden definir por
#    @dataclass
#    class Arbol:
#        pass
#
#    @dataclass
#    class H(Arbol):
#        pass
#
#    @dataclass
#    class N(Arbol):
#        x: int
#        i: Arbol
#        d: Arbol
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
#    sumaArbol : (Arbol) -> int
# tal sumaArbol(x) es la suma de los valores que hay en el árbol x.
# Por ejemplo,
#    >>> sumaArbol(N(2, N(5, N(3, H(), H()), N(7, H(), H())), N(4, H(), H())))
#    21
# ---------------------------------------------------------------------

from dataclasses import dataclass


@dataclass
class Arbol:
    pass

@dataclass
class H(Arbol):
    pass

@dataclass
class N(Arbol):
    x: int
    i: Arbol
    d: Arbol

def sumaArbol(a: Arbol) -> int:
    match a:
        case H():
            return 0
        case N(x, i, d):
            return x + sumaArbol(i) + sumaArbol(d)
    assert False
