# rama_izquierda_de_un_arbol_binario.py
# Rama izquierda de un árbol binario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 26-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios con valores en los nodos]
# (https://bit.ly/40Pplzj), definir la función
#    ramaIzquierda : (Arbol[A]) -> list[A]
# tal que ramaIzquierda(a) es la lista de los valores de los nodos de
# la rama izquierda del árbol a. Por ejemplo,
#    >>> ramaIzquierda(N(2, N(5, N(3, H(), H()), N(7, H(), H())), N(4, H(), H())))
#    [2, 5, 3]
# ---------------------------------------------------------------------

from typing import TypeVar

from src.arbol_binario_valores_en_nodos import Arbol, H, N

A = TypeVar("A")

def ramaIzquierda(a: Arbol[A]) -> list[A]:
    match a:
        case H():
            return []
        case N(x, i, _):
            return [x] + ramaIzquierda(i)
    assert False
