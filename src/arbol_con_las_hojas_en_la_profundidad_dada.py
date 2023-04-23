# Arbol_con_las_hojas_en_la_profundidad_dada.py
# Árbol con las hojas en la profundidad dada.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios con los valores en las hojas]
# (https://bit.ly/3N5RuyE), definir la función
#    creaArbol : (int) -> Arbol[Any]:
# tal que creaArbol(n) es el árbol cuyas hoyas están en la profundidad
# n. Por ejemplo,
#    >>> creaArbol(2)
#    Nodo(Nodo(Hoja(None), Hoja(None)), Nodo(Hoja(None), Hoja(None)))
# ---------------------------------------------------------------------

from typing import Any, TypeVar

from src.arbol_binario_valores_en_hojas import Arbol, Hoja, Nodo

A = TypeVar("A")

def creaArbol(h: int) -> Arbol[Any]:
    if h <= 0:
        return Hoja(None)
    x = creaArbol(h - 1)
    return Nodo(x, x)
