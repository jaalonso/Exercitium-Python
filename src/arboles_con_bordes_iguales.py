# arboles_con_bordes_iguales.py
# Árboles con bordes iguales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 28-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usaremos el [tipo de los árboles binarios con los valores en las
# hojas](https://bit.ly/3N5RuyE).
#
# Por ejemplo, los árboles
#    árbol1          árbol2       árbol3     árbol4
#       o              o           o           o
#      / \            / \         / \         / \
#     1   o          o   3       o   3       o   1
#        / \        / \         / \         / \
#       2   3      1   2       1   4       2   3
# se representan por
#    arbol1: Arbol[int] = N(H(1), N(H(2), H(3)))
#    arbol2: Arbol[int] = N(N(H(1), H(2)), H(3))
#    arbol3: Arbol[int] = N(N(H(1), H(4)), H(3))
#    arbol4: Arbol[int] = N(N(H(2), H(3)), H(1))
#
# Definir la función
#    igualBorde : (Arbol[A], Arbol[A]) -> bool
# tal que igualBorde(t1, t2) se verifica si los bordes de los árboles
# t1 y t2 son iguales. Por ejemplo,
#    igualBorde(arbol1, arbol2)  ==  True
#    igualBorde(arbol1, arbol3)  ==  False
#    igualBorde(arbol1, arbol4)  ==  False
# ---------------------------------------------------------------------

from typing import TypeVar

from src.arbol_binario_valores_en_hojas import Arbol, Hoja, Nodo

A = TypeVar("A")

arbol1: Arbol[int] = Nodo(Hoja(1), Nodo(Hoja(2), Hoja(3)))
arbol2: Arbol[int] = Nodo(Nodo(Hoja(1), Hoja(2)), Hoja(3))
arbol3: Arbol[int] = Nodo(Nodo(Hoja(1), Hoja(4)), Hoja(3))
arbol4: Arbol[int] = Nodo(Nodo(Hoja(2), Hoja(3)), Hoja(1))

# borde(t) es el borde del árbol t; es decir, la lista de las hojas
# del árbol t leídas de izquierda a derecha. Por ejemplo,
#    borde(arbol4)  ==  [2, 3, 1]
def borde(a: Arbol[A]) -> list[A]:
    match a:
        case Hoja(x):
            return [x]
        case Nodo(i, d):
            return borde(i) + borde(d)
    assert False

def igualBorde(t1: Arbol[A], t2: Arbol[A]) -> bool:
    return borde(t1) == borde(t2)
