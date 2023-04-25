# aplanamiento_de_un_arbol.py
# Aplanamiento de un árbol
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios](https://bit.ly/3H53exA),
# definir la función
#    aplana :: Arbol t -> [t]
# tal que (aplana a) es la lista obtenida aplanando el árbol a. Por
# ejemplo,
#    >>> aplana (N(5, N(3, H(1), H(4)), N(7, H(6), (H(9)))))
#    [1, 3, 4, 5, 6, 7, 9]
# ---------------------------------------------------------------------

from typing import TypeVar

from src.arboles_binarios import Arbol, H, N

A = TypeVar("A")

def aplana(a: Arbol[A]) -> list[A]:
    match a:
        case H(n):
            return [n]
        case N(n, i, d):
            return aplana(i) + [n] + aplana(d)
    assert False
