# Transformacion_de_listas_en_pilas.py
# Transformación de listas en pilas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, ??-enero-2023
# ======================================================================

#    >>> print(lista2pila([3,2,5,1,7]))
#    7 | 3 | 1 | 2 | 5

from typing import TypeVar

from src.TAD.pilaConListas import Pila, apila, vacia

T = TypeVar('T')

# 1ª solución
# ===========

def lista2pila1(xs: list[T]) -> Pila[T]:
    ys = list(reversed(xs))
    if not ys:
        return vacia()
    return apila(ys[0], lista2pila1(ys[1:]))

# 2ª solución
# ===========

def lista2pila2(xs: list[T]) -> Pila[T]:
    p: Pila[T] = Pila()
    for x in xs:
        p.apila(x)
    return p
