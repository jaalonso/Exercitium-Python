# Universo_y_grafo_de_una_relacion_binaria.py
# Universo y grafo de una relación binaria.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 28-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Una relación binaria R sobre un conjunto A se puede representar
# mediante un par (xs,ps) donde xs es la lista de los elementos de A
# (el universo de R) y ps es la lista de pares de R (el grafo de R).
#
# Definir el tipo de dato Rel, para representar las relaciones
# binarias sobre A, y las siguientes funciones
#    universo : (Rel[A]) -> list[A]
#    grafo    : (Rel[A]) -> list[tuple[A, A]]
# tales que
# + universo(r) es el universo de la relación r. Por ejemplo,
#      >>> r = (list(range(1, 10)), [(1, 3), (2, 6), (8, 9), (2, 7)])
#      >>> universo(r)
#      [1, 2, 3, 4, 5, 6, 7, 8, 9]
# + grafo(r) es el grafo de la relación r. Por ejemplo,
#      >>> grafo(r)
#      [(1, 3), (2, 6), (8, 9), (2, 7)]
# ---------------------------------------------------------------------

from typing import TypeVar

A = TypeVar('A')

Rel = tuple[list[A], list[tuple[A, A]]]

r: Rel[int] = (list(range(1, 10)), [(1, 3), (2, 6), (8, 9), (2, 7)])

def universo(r: Rel[A]) -> list[A]:
    return r[0]

def grafo(r: Rel[A]) -> list[tuple[A, A]]:
    return r[1]
