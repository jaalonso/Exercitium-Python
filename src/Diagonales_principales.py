# Diagonales_principales.py
# Diagonales principales de una matriz.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-febrero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# La lista de las diagonales principales de la matriz
#    1  2  3  4
#    5  6  7  8
#    9 10 11 12
# es
#    [[9],[5,10],[1,6,11],[2,7,12],[3,8],[4]]
#
# Definir la función
#    diagonalesPrincipales : (list[list[A]]) -> list[list[A]]
# tal que diagonalesPrincipales(p) es la lista de las diagonales
# principales de p. Por ejemplo,
#    >>> diagonalesPrincipales([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#    [[9], [5, 10], [1, 6, 11], [2, 7, 12], [3, 8], [4]]
# ---------------------------------------------------------------------

from typing import TypeVar

from src.Posiciones_diagonales_principales import (
    posicionesDiagonalesPrincipales1, posicionesDiagonalesPrincipales2)

A = TypeVar('A')

# 1ª solución
# ===========

matriz = list[list[A]]

def diagonalesPrincipales1(p: matriz[A]) -> list[list[A]]:
    m = len(p)
    n = len(p[0])
    return [[p[i-1][j-1] for (i,j) in ijs]
            for ijs in posicionesDiagonalesPrincipales1(m, n)]

# 2ª solución
# ===========

def diagonalesPrincipales2(p: matriz[A]) -> list[list[A]]:
    m = len(p)
    n = len(p[0])
    return [[p[i-1][j-1] for (i,j) in ijs]
            for ijs in posicionesDiagonalesPrincipales2(m, n)]

# Verificación
# ============

def test_diagonalesPrincipales() -> None:
    for diagonalesPrincipales in [diagonalesPrincipales1,
                                  diagonalesPrincipales2]:
        assert diagonalesPrincipales([[ 1, 2, 3, 4],
                                      [ 5, 6, 7, 8],
                                      [ 9,10,11,12]]) == \
                    [[9],[5,10],[1,6,11],[2,7,12],[3,8],[4]]
    print("Verificado")

# La verificación es
#    >>> test_diagonalesPrincipales()
#    Verificado
