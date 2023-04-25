# pertenencia_de_un_elemento_a_un_arbol.py
# Pertenencia de un elemento a un árbol
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios](https://bit.ly/3H53exA),
# definir la función
#    pertenece : (A, Arbol[A]) -> bool
# tal que pertenece(m, a) se verifica si m pertenece en el árbol a. Por
# ejemplo,
#    >>> pertenece(4, N(5, N(3, H(1), H(4)), N(7, H(6), (H(9)))))
#    True
#    >>> pertenece(0, N(5, N(3, H(1), H(4)), N(7, H(6), (H(9)))))
#    False
# ---------------------------------------------------------------------

from typing import TypeVar

from src.arboles_binarios import Arbol, H, N

A = TypeVar("A")

def pertenece(m: A, a: Arbol[A]) -> bool:
    match a:
        case H(n):
            return m == n
        case N(n, i, d):
            return m == n or pertenece(m, i) or pertenece(m, d)
    assert False
