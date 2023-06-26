# BusquedaEnProfundidad.py
# Búsqueda en espacios de estados por profundidad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 28-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las características de los problemas de espacios de estados son:
# + un conjunto de las posibles situaciones o nodos que constituye el
#   espacio de estados (estos son las potenciales soluciones que se
#   necesitan explorar),
# + un conjunto de movimientos de un nodo a otros nodos, llamados los
#   sucesores del nodo,
# + un nodo inicial y
# + un nodo objetivo que es la solución.
#
# Definir la función
#    buscaProfundidad :: Eq nodo => (nodo -> [nodo]) -> (nodo -> Bool)
#                                   -> nodo -> [nodo]
# tal que (buscaProfundidad s o e) es  la lista de soluciones del
# problema de espacio de estado definido por la función sucesores s, el
# objetivo o y estado inicial e obtenidas mediante búsqueda en
# profundidad.
# ---------------------------------------------------------------------

from functools import reduce
from sys import setrecursionlimit
from typing import Callable, TypeVar

from src.TAD.pila import Pila, apila, cima, desapila, esVacia, vacia

A = TypeVar('A')

setrecursionlimit(10**6)

def buscaProfundidad(sucesores: Callable[[A], list[A]],
                     esFinal: Callable[[A], bool],
                     inicial: A) -> list[A]:
    def aux(p: Pila[A]) -> list[A]:
        if esVacia(p):
            return []
        if esFinal(cima(p)):
            return [cima(p)] + aux(desapila(p))
        return aux(reduce(lambda x, y: apila(y, x),
                          sucesores(cima(p)),
                          desapila(p)))

    return aux(apila(inicial, vacia()))
