# aplicacion_de_una_funcion_a_un_arbol.py
# Aplicación de una función a un árbol.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 7-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios con los valores en las hojas]
# (https://bit.ly/3N5RuyE), definir la función
#    mapArbol : (Callable[[A], B], Arbol[A]) -> Arbol[B]
# tal que mapArbol(f, t) es el árbolo obtenido aplicando la función f a
# los elementos del árbol t. Por ejemplo,
#    >>> mapArbol(lambda x: 1 + x, Nodo(Hoja(2), Hoja(4)))
#    Nodo(i=Hoja(x=3), d=Hoja(x=5))
# ---------------------------------------------------------------------

from typing import Callable, TypeVar

from src.arbol_binario_valores_en_hojas import Arbol, Hoja, Nodo

A = TypeVar("A")
B = TypeVar("B")

def mapArbol(f: Callable[[A], B], a: Arbol[A]) -> Arbol[B]:
    match a:
        case Hoja(x):
            return Hoja(f(x))
        case Nodo(i, d):
            return Nodo(mapArbol(f, i), mapArbol(f, d))
    assert False
