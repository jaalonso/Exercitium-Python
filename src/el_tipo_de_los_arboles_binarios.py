# el_tipo_de_los_arboles_binarios.py
# El tipo de_los árboles binarios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El árbol binario
#         5
#        / \
#       /   \
#      3     7
#     / \   / \
#    1   4 6   9
# se puede representar por
#    ejArbol = Nodo (Nodo (Hoja 1) 3 (Hoja 4))
#                   5
#                   (Nodo (Hoja 6) 7 (Hoja 9))
#
# El tipo de los árboles binarios se puede definir por
#    @dataclass
#    class Arbol:
#        pass
#
#    @dataclass
#    class Hoja(Arbol):
#        x: int
#
#    @dataclass
#    class Nodo(Arbol):
#        i: Arbol
#        x: int
#        d: Arbol
#
# Definir las funciones
#    ocurre : (int, Arbol) -> bool
#    aplana : (Arbol) -> list[int]
# tales que
# + ocurre(m, a) se verifica si m ocurre en el árbol a. Por ejemplo,
#      ocurre(4, ejArbol)  ==  True
#      ocurre(0, ejArbol)  ==  False
# + aplana(a) es la lista obtenida aplanando el árbol a. Por ejemplo,
#      aplana(ejArbol)  ==  [1,3,4,5,6,7,9]
# ---------------------------------------------------------------------

from dataclasses import dataclass


@dataclass
class Arbol:
    pass

@dataclass
class Hoja(Arbol):
    x: int

@dataclass
class Nodo(Arbol):
    i: Arbol
    x: int
    d: Arbol

ejArbol = Nodo(Nodo(Hoja(1), 3, Hoja(4)),
               5,
               Nodo(Hoja(6), 7, Hoja(9)))

def ocurre(m: int, a: Arbol) -> bool:
    match a:
        case Hoja(n):
            return m == n
        case Nodo(i, n, d):
            return m == n or ocurre(m, i) or ocurre(m, d)
    assert False

def aplana(a: Arbol) -> list[int]:
    match a:
        case Hoja(n):
            return [n]
        case Nodo(i, n, d):
            return aplana(i) + [n] + aplana(d)
    assert False
