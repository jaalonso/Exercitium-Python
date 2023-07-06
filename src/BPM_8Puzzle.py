# BPM_8Puzzle.py
# El problema del 8 puzzle.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 7-julio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Para el 8-puzzle se usa un cajón cuadrado en el que hay situados 8
# bloques cuadrados. El cuadrado restante está sin rellenar. Cada
# bloque tiene un número. Un bloque adyacente al hueco puede deslizarse
# hacia él. El juego consiste en transformar la posición inicial en la
# posición final mediante el deslizamiento de los bloques. En
# particular, consideramos el estado inicial y final siguientes:
#
#    +---+---+---+                   +---+---+---+
#    |   | 1 | 3 |                   | 1 | 2 | 3 |
#    +---+---+---+                   +---+---+---+
#    | 8 | 2 | 4 |                   | 8 |   | 4 |
#    +---+---+---+                   +---+---+---+
#    | 7 | 5 | 5 |                   | 7 | 6 | 5 |
#    +---+---+---+                   +---+---+---+
#    Estado inicial                  Estado final
#
# Para solucionar el problema se definen los siguientes tipos:
# + Tablero es lista de listas de números enteros (que representan las
#   piezas en  cada posición y el 0 representa el hueco):
#      Tablero = list[list[int]]
# + Estado es una tupla (h, n, ts), donde ts es una listas de tableros
#   [t_n,...,t_1] tal que t_i es un sucesor de t_(i-1) y h es la
#   heurística de t_n.
#      Estado = tuple[int, int, list[Tablero]]
#
# Usando el procedimiento de [búsqueda por primero el mejor](???),
# definir la función
#    solucion_8puzzle : (Tablero) -> Tablero
# tal que solucion_8puzzle(t) es la solución del problema del problema
# del 8 puzzle a partir del tablero t. Por ejemplo,
#    >>> solucion_8puzzle([[0,1,3],[8,2,4],[7,6,5]])
#    [[[0, 1, 3],
#      [8, 2, 4],
#      [7, 6, 5]],
#     [[1, 0, 3],
#      [8, 2, 4],
#      [7, 6, 5]],
#     [[1, 2, 3],
#      [8, 0, 4],
#      [7, 6, 5]]]
#    >>> solucion_8puzzle([[8,1,3],[0,2,4],[7,6,5]])
#    [[[8, 1, 3],
#      [0, 2, 4],
#      [7, 6, 5]],
#     [[0, 1, 3],
#      [8, 2, 4],
#      [7, 6, 5]],
#     [[1, 0, 3],
#      [8, 2, 4],
#      [7, 6, 5]],
#     [[1, 2, 3],
#      [8, 0, 4],
#      [7, 6, 5]]]
#    >>> len(solucion_8puzzle([[2,6,3],[5,0,4],[1,7,8]]))
#    21
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import Optional

from src.BusquedaPrimeroElMejor import buscaPM

Tablero = list[list[int]]

# Tablero final
# =============

# tableroFinal es el tablero final del 8 puzzle.
tableroFinal: Tablero = [[1,2,3],
                         [8,0,4],
                         [7,6,5]]

# Posiciones
# ==========

# Una posición es un par de enteros.
Posicion = tuple[int,int]

# Heurística
# ==========

# distancia(p1, p2) es la distancia Manhatan entre las posiciones p1 y
# p2. Por ejemplo,
#    >>> distancia((2,7), (4,1))
#    8
def distancia(p1: Posicion, p2: Posicion) -> int:
    (x1, y1) = p1
    (x2, y2) = p2
    return abs(x1-x2) + abs (y1-y2)

# posicionElemento(t, a) es la posición de elemento a en el tablero
# t. Por ejemplo,
#    λ> posicionElemento([[2,1,3],[8,0,4],[7,6,5]], 4)
#    (1, 2)
def posicionElemento(t: Tablero, a: int) -> Posicion:
    for i in range(0, 3):
        for j in range(0, 3):
            if t[i][j] == a:
                return (i, j)
    return (4, 4)

# posicionHueco(t) es la posición del hueco en el tablero t. Por
# ejemplo,
#    >>> posicionHueco([[2,1,3],[8,0,4],[7,6,5]])
#    (1, 1)
def posicionHueco(t: Tablero) -> Posicion:
    return posicionElemento(t, 0)

# heuristica(t) es la suma de la distancia Manhatan desde la posición de
# cada objeto del tablero a su posición en el tablero final. Por
# ejemplo,
#    >>> heuristica([[0,1,3],[8,2,4],[7,6,5]])
#    4
def heuristica(t: Tablero) -> int:
    return sum((distancia(posicionElemento(t, i),
                          posicionElemento(tableroFinal, i))
                for i in range(0, 10)))

# Estados
# =======

# Un estado es una tupla (h, n, ts), donde ts es una listas de tableros
# [t_n,...,t_1] tal que t_i es un sucesor de t_(i-1) y h es la
# heurística de t_n.
Estado = tuple[int, int, list[Tablero]]

# Estado inicial
# ==============

# inicial(t) es el estado inicial del problema del 8 puzzle a partir del
# tablero t.
def inicial(t: Tablero) -> Estado:
    return (heuristica(t), 1, [t])

# Estado final
# ============

# esFinal(e) se verifica si e es un estado final.
def esFinal(e: Estado) -> bool:
    (_, _, ts) = e
    return ts[0] == tableroFinal

# Sucesores
# =========

# posicionesVecinas(p) son las posiciones de la matriz cuadrada de
# dimensión 3 que se encuentran encima, abajo, a la izquierda y a la
# derecha de los posición p. Por ejemplo,
#    >>> posicionesVecinas((1,1))
#    [(0, 1), (2, 1), (1, 0), (1, 2)]
#    >>> posicionesVecinas((0,1))
#    [(1, 1), (0, 0), (0, 2)]
#    >>> posicionesVecinas((0,0))
#    [(1, 0), (0, 1)]
def posicionesVecinas(p: Posicion) -> list[Posicion]:
    (i, j) = p
    vecinas = []
    if i > 0:
        vecinas.append((i - 1, j))
    if i < 2:
        vecinas.append((i + 1, j))
    if j > 0:
        vecinas.append((i, j - 1))
    if j < 2:
        vecinas.append((i, j + 1))
    return vecinas

# intercambia(t,p1, p2) es el tablero obtenido intercambiando en t los
# elementos que se encuentran en las posiciones p1 y p2. Por ejemplo,
#    >>> intercambia([[2,1,3],[8,0,4],[7,6,5]], (0,1), (1,1))
#    [[2, 0, 3], [8, 1, 4], [7, 6, 5]]
def intercambia(t: Tablero, p1: Posicion, p2: Posicion) -> Tablero:
    (i1, j1) = p1
    (i2, j2) = p2
    t1 = deepcopy(t)
    a1 = t1[i1][j1]
    a2 = t1[i2][j2]
    t1[i1][j1] = a2
    t1[i2][j2] = a1
    return t1

# tablerosSucesores(t) es la lista de los tablrtos sucesores del
# tablero t. Por ejemplo,
#    >>> tablerosSucesores([[2,1,3],[8,0,4],[7,6,5]])
#    [[[2, 0, 3], [8, 1, 4], [7, 6, 5]],
#     [[2, 1, 3], [8, 6, 4], [7, 0, 5]],
#     [[2, 1, 3], [0, 8, 4], [7, 6, 5]],
#     [[2, 1, 3], [8, 4, 0], [7, 6, 5]]]
def tablerosSucesores(t: Tablero) -> list[Tablero]:
    p = posicionHueco(t)
    return [intercambia(t, p, q) for q in posicionesVecinas(p)]

# (sucesores e) es la lista de sucesores del estado e. Por ejemplo,
#    >>> t1 = [[0,1,3],[8,2,4],[7,6,5]]
#    >>> es = sucesores((heuristica(t1), 1, [t1]))
#    >>> es
#    [(4, 2, [[[8, 1, 3],
#              [0, 2, 4],
#              [7, 6, 5]],
#             [[0, 1, 3],
#              [8, 2, 4],
#              [7, 6, 5]]]),
#     (2, 2, [[[1, 0, 3],
#              [8, 2, 4],
#              [7, 6, 5]],
#             [[0, 1, 3],
#              [8, 2, 4],
#              [7, 6, 5]]])]
#    >>> sucesores(es[1])
#    [(0, 3, [[[1, 2, 3],
#              [8, 0, 4],
#              [7, 6, 5]],
#             [[1, 0, 3],
#              [8, 2, 4],
#              [7, 6, 5]],
#             [[0, 1, 3],
#              [8, 2, 4],
#              [7, 6, 5]]]),
#     (4, 3, [[[1, 3, 0],
#              [8, 2, 4],
#              [7, 6, 5]],
#             [[1, 0, 3],
#              [8, 2, 4],
#              [7, 6, 5]],
#             [[0, 1, 3],
#              [8, 2, 4],
#              [7, 6, 5]]])]
def sucesores(e: Estado) -> list[Estado]:
    (_, n, ts) = e
    return [(heuristica(t1), n+1, [t1] + ts)
            for t1 in tablerosSucesores(ts[0])
            if t1 not in ts]

# Solución
# ========

def solucion_8puzzle(t: Tablero) -> Optional[list[Tablero]]:
    r = buscaPM(sucesores, esFinal, inicial(t))
    if r is None:
        return None
    (_, _, ts) = r
    ts.reverse()
    return ts

# Verificación
# ============

def test_8puzzle() -> None:
    assert solucion_8puzzle([[8,1,3],[0,2,4],[7,6,5]]) == \
        [[[8, 1, 3], [0, 2, 4], [7, 6, 5]],
         [[0, 1, 3], [8, 2, 4], [7, 6, 5]],
         [[1, 0, 3], [8, 2, 4], [7, 6, 5]],
         [[1, 2, 3], [8, 0, 4], [7, 6, 5]]]

# La verificación es
#    src> poetry run pytest -q BPM_8Puzzle.py
#    1 passed in 0.10s
