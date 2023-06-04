# Grafo_Anchura_de_un_grafo.py
# TAD de los grafos: Anchura de un grafo,
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# En un grafo, la anchura de un nodo es el máximo de los valores
# absolutos de la diferencia entre el valor del nodo y los de sus
# adyacentes; y la anchura del grafo es la máxima anchura de sus
# nodos. Por ejemplo, en el grafo
#    grafo1: Grafo = creaGrafo_(Orientacion.D, (1,5), [(1,2),(1,3),(1,5),
#                                                      (2,4),(2,5),
#                                                      (3,4),(3,5),
#                                                      (4,5)])
# su anchura es 4 y el nodo de máxima anchura es el 5.
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    anchura : (Grafo) -> int
# tal que anchuraG(g) es la anchura del grafo g. Por ejemplo,
#    anchura(grafo1)  ==  4
#
# Comprobar experimentalmente que la anchura del grafo ciclo de orden
# n es n-1.
# ---------------------------------------------------------------------

from src.Grafo_Grafos_ciclos import grafoCiclo
from src.TAD.Grafo import (Grafo, Orientacion, Vertice, adyacentes, aristas,
                           creaGrafo_, nodos)

grafo1: Grafo = creaGrafo_(Orientacion.D, (1,5), [(1,2),(1,3),(1,5),
                                                  (2,4),(2,5),
                                                  (3,4),(3,5),
                                                  (4,5)])

# 1ª solución
# ===========

def anchura(g: Grafo) -> int:
    return max(anchuraN(g, x) for x in nodos(g))

# (anchuraN g x) es la anchura del nodo x en el grafo g. Por ejemplo,
#    anchuraN g 1  ==  4
#    anchuraN g 2  ==  3
#    anchuraN g 4  ==  2
#    anchuraN g 5  ==  4
def anchuraN(g: Grafo, x: Vertice) -> int:
    return max([0] + [abs (x - v) for v in adyacentes(g, x)])

# 2ª solución
# ===========

def anchura2(g: Grafo) -> int:
    return max(abs (x-y) for ((x,y),_) in aristas(g))

# La conjetura
def conjetura(n: int) -> bool:
    return anchura(grafoCiclo(n)) == n - 1

# La comprobación es
#    >>> all(conjetura(n) for n in range(2, 11))
#    True

# Verificación
# ============

def test_anchura() -> None:
    g2 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(1,3),(2,3),(3,3)])
    assert anchura(grafo1) == 4
    assert anchura(g2) == 2
    print("Verificado")

# La verificación es
#    >>> test_anchura()
#    Verificado
