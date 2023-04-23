# altura_de_un_arbol_binario.py
# Altura de un árbol binario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios con los valores en las hojas]
# (https://bit.ly/3N5RuyE), definir la función
#    altura : (Arbol) -> int
# tal que altura(t) es la altura del árbol t. Por ejemplo,
#    >>> altura(Hoja(1))
#    0
#    >>> altura(Nodo(Hoja(1), Hoja(6)))
#    1
#    >>> altura(Nodo(Nodo(Hoja(1), Hoja(6)), Hoja(2)))
#    2
#    >>> altura(Nodo(Nodo(Hoja(1), Hoja(6)), Nodo(Hoja(2), Hoja(7))))
#    2
# ---------------------------------------------------------------------

from typing import TypeVar

from src.arbol_binario_valores_en_hojas import Arbol, Hoja, Nodo

A = TypeVar("A")

def altura(a: Arbol[A]) -> int:
    match a:
        case Hoja(_):
            return 0
        case Nodo(i, d):
            return 1 + max(altura(i), altura(d))
    assert False
