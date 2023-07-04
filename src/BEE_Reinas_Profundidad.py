# BEE_Reinas.py
# El problema de las n reinas (mediante espacios de estados).
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El problema de las n reinas consiste en colocar n reinas en un
# tablero cuadrado de dimensiones n por n de forma que no se encuentren
# más de una en la misma línea: horizontal, vertical o diagonal.
#
# Las posiciones de las reinas en el tablero se representan por su
# columna y su fila.
#    Columna = int
#    Fila    = int
#
# Una solución del problema de las n reinas es una lista de
# posiciones.
#    SolNR = list[tuple[Columna, Fila]]
#
# Usando el procedimiento de búsqueda en profundidad, definir las
# funciones
#    solucionesNR      : (int) -> list[SolNR]
#    primeraSolucionNR : (int) -> SolNR
#    nSolucionesNR     : (int) -> int
# tales que
# + solucionesNR(n) es la lista de las soluciones del problema de las n
#   reinas, por búsqueda de espacio de estados en profundidad. Por
#   ejemplo,
#      >>> solucionesNR(8)[:3]
#      [[(1, 8), (2, 4), (3, 1), (4, 3), (5, 6), (6, 2), (7, 7), (8, 5)],
#       [(1, 8), (2, 3), (3, 1), (4, 6), (5, 2), (6, 5), (7, 7), (8, 4)],
#       [(1, 8), (2, 2), (3, 5), (4, 3), (5, 1), (6, 7), (7, 4), (8, 6)]]
# + primeraSolucionNR(n) es la primera solución del problema de las n
#   reinas, por búsqueda en espacio de estados por profundidad. Por
#   ejemplo,
#      >>> primeraSolucionNR(8)
#      [(1, 8), (2, 4), (3, 1), (4, 3), (5, 6), (6, 2), (7, 7), (8, 5)]
# + nSolucionesNR(n) es el número de soluciones del problema de las n
#   reinas, por búsqueda en espacio de estados. Por ejemplo,
#      >>> nSolucionesNR(8)
#      92
# ---------------------------------------------------------------------

from src.BusquedaEnProfundidad import buscaProfundidad

Columna = int
Fila = int
SolNR = list[tuple[Columna, Fila]]

# Los nodos del problema de las n reinas son ternas formadas por la
# columna de la última reina colocada, el número de columnas del
# tablero y la solución parcial de las reinas colocadas anteriormente.
NodoNR = tuple[Columna, Columna, SolNR]

# valida(sp, p) se verifica si la posición p es válida respecto de la
# solución parcial sp; es decir, la reina en la posición p no amenaza a
# ninguna de las reinas de la sp (se supone que están en distintas
# columnas). Por ejemplo,
#    valida([(1,1)], (2,2))  ==  False
#    valida([(1,1)], (2,3))  ==  True
def valida(sp: SolNR, p: tuple[Columna, Fila]) -> bool:
    c, r = p
    def test(s: tuple[Columna, Fila]) -> bool:
        c1, r1 = s
        return c1 + r1 != c + r and c1 - r1 != c - r and r1 != r

    return all(test(s) for s in sp)

# sucesoresNR(e) es la lista de los sucesores del estado e en el
# problema de las n reinas. Por ejemplo,
#    >>> sucesoresNR((1,4,[]))
#    [(2,4,[(1,1)]),(2,4,[(1,2)]),(2,4,[(1,3)]),(2,4,[(1,4)])]
def sucesoresNR (nd: NodoNR) -> list[NodoNR]:
    c,n,solp = nd
    return [(c+1,n,solp + [(c,r)]) for r in range(1, n+1) if valida(solp, (c,r))]

# esFinalNR(e) se verifica si e es un estado final del problema de las
# n reinas.
def esFinalNR(nd: NodoNR) -> bool:
    c, n, _ = nd
    return c > n

def solucionesNR(n: int) -> list[SolNR]:
    nInicial: NodoNR = (1,n,[])
    return [e for (_, _, e) in buscaProfundidad(sucesoresNR,
                                                esFinalNR,
                                                nInicial)]

def primeraSolucionNR(n: int) -> SolNR:
    return solucionesNR(n)[0]

def nSolucionesNR(n: int) -> int:
    return len(solucionesNR(n))

# Verificación
# ============

def test_nReinas() -> None:
    assert solucionesNR(8)[:3] == \
        [[(1,8),(2,4),(3,1),(4,3),(5,6),(6,2),(7,7),(8,5)],
         [(1,8),(2,3),(3,1),(4,6),(5,2),(6,5),(7,7),(8,4)],
         [(1,8),(2,2),(3,5),(4,3),(5,1),(6,7),(7,4),(8,6)]]
    assert nSolucionesNR(8) == 92
    print("Verificado")

# La verificación es
#
