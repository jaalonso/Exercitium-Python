# Grafo_Nodos_aislados_de_un_grafo.py
# TAD de los grafos: Nodos aislados de un grafo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Dado un grafo dirigido G, diremos que un nodo está aislado si o bien
# de dicho nodo no sale ninguna arista o bien no llega al nodo ninguna
# arista. Por ejemplo, en el siguiente grafo
#    grafo1: Grafo = creaGrafo_(Orientacion.D,
#                               (1,6),
#                               [(1,2),(1,3),(1,4),(3,6),(5,4),(6,2),(6,5)])
# podemos ver que del nodo 1 salen 3 aristas pero no llega ninguna, por
# lo que lo consideramos aislado. Así mismo, a los nodos 2 y 4 llegan
# aristas pero no sale ninguna, por tanto también estarán aislados.
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    aislados :: (Ix v, Num p) => Grafo v p -> [v]
# tal que (aislados g) es la lista de nodos aislados del grafo g. Por
# ejemplo,
#    aislados grafo1 == [1,2,4]
# ---------------------------------------------------------------------

from src.Grafo_Incidentes_de_un_vertice import incidentes
from src.TAD.Grafo import (Grafo, Orientacion, Vertice, adyacentes, creaGrafo_,
                           nodos)

grafo1: Grafo = creaGrafo_(Orientacion.D,
                           (1,6),
                           [(1,2),(1,3),(1,4),(3,6),(5,4),(6,2),(6,5)])

def aislados(g: Grafo) -> list[Vertice]:
    return [n for n in nodos(g)
            if not adyacentes(g, n) or not incidentes(g, n)]

# Verificación
# ============

def test_aislados() -> None:
    assert aislados(grafo1) == [1, 2, 4]
    print("Verificado")

# La verificación es
#    >>> test_aislados()
#    Verificado
