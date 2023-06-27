# BusquedaEnAnchura.hs
# Búsqueda en espacios de estados por anchura.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-junio-2023
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
#    buscaAnchura :: Eq nodo => (nodo -> [nodo]) -> (nodo -> Bool)
#                               -> nodo -> [nodo]
# tal que (buscaAnchura s o e) es  la lista de soluciones del
# problema de espacio de estado definido por la función sucesores s, el
# objetivo o y estado inicial e obtenidas mediante búsqueda en
# anchura.
# ---------------------------------------------------------------------

from functools import reduce
from sys import setrecursionlimit
from typing import Callable, TypeVar

from src.TAD.cola import Cola, esVacia, inserta, primero, resto, vacia

A = TypeVar('A')

setrecursionlimit(10**6)

def buscaAnchura(sucesores: Callable[[A], list[A]],
                  esFinal: Callable[[A], bool],
                  inicial: A) -> list[A]:
    def aux(p: Cola[A]) -> list[A]:
        if esVacia(p):
            return []
        if esFinal(primero(p)):
            return [primero(p)] + aux(resto(p))
        return aux(reduce(lambda x, y: inserta(y, x),
                          sucesores(primero(p)),
                          resto(p)))

    return aux (inserta(inicial, vacia()))
