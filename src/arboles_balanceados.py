# arboles_balanceados.py
# Árboles balanceados.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 27-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Diremos que un árbol está balanceado si para cada nodo la diferencia
# entre el número de nodos de sus subárboles izquierdo y derecho es
# menor o igual que uno.
#
# Usando el [tipo de los árboles binarios con valores en los nodos]
# (https://bit.ly/40Pplzj), definir la función
#    balanceado : (Arbol[A]) -> bool
# tal que balanceado(a) se verifica si el árbol a está balanceado. Por
# ejemplo,
#    >>> balanceado(N(5, H(), N(3, H(), H())))
#    True
#    >>> balanceado(N(4, N(3, N(2, H(), H()), H()), N(5, H(), N(6, H(), N(7, H(), H())))))
#    False
# ---------------------------------------------------------------------

from typing import TypeVar

from src.arbol_binario_valores_en_nodos import Arbol, H, N

A = TypeVar("A")

def numeroNodos(a: Arbol[A]) -> int:
    match a:
        case H():
            return 0
        case N(_, i, d):
            return 1 + numeroNodos(i) + numeroNodos(d)
    assert False

def balanceado(a: Arbol[A]) -> bool:
    match a:
        case H():
            return True
        case N(_, i, d):
            return abs(numeroNodos(i) - numeroNodos(d)) <= 1 \
                and balanceado(i) and balanceado(d)
    assert False
