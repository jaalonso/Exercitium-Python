# Grafo_Grados_positivos_y_negativos.ps
# TAD de los grafos: Grados_positivos_y_negativos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 2-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El grado positivo de un vértice v de un grafo g es el número de
# vértices de g adyacentes con v y su grado negativo es el número de
# vértices de g incidentes con v.
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir las funciones,
#    gradoPos : (Grafo, Vertice) -> int
#    gradoNeg : (Grafo, Vertice) -> int
# tales que
# + gradoPos(g, v) es el grado positivo del vértice v en el grafo g.
#   Por ejemplo,
#      g1 = creaGrafo_(Orientacion.ND, (1,5),
#                      [(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)])
#      g2 = creaGrafo_(Orientacion.D, (1,5),
#                      [(1,2),(1,3),(1,5),(2,4),(2,5),(4,3),(4,5)])
#      λ> gradoPos(g1, 5)
#      4
#      λ> gradoPos(g2, 5)
#      0
#      λ> gradoPos(g2, 1)
#      3
# + gradoNeg(g, v) es el grado negativo del vértice v en el grafo g.
#   Por ejemplo,
#      λ> gradoNeg(g1, 5)
#      4
#      λ> gradoNeg(g2, 5)
#      3
#      λ> gradoNeg(g2, 1)
#      0
# ---------------------------------------------------------------------

from src.Grafo_Incidentes_de_un_vertice import incidentes
from src.TAD.Grafo import Grafo, Orientacion, Vertice, adyacentes, creaGrafo_


def gradoPos(g: Grafo, v: Vertice) -> int:
    return len(adyacentes(g, v))

def gradoNeg(g: Grafo, v: Vertice) -> int:
    return len(incidentes(g, v))

# Verificación
# ============

def test_GradoPosNeg() -> None:
    g1 = creaGrafo_(Orientacion.ND, (1,5),
                    [(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)])
    g2 = creaGrafo_(Orientacion.D, (1,5),
                    [(1,2),(1,3),(1,5),(2,4),(2,5),(4,3),(4,5)])
    assert gradoPos(g1, 5) == 4
    assert gradoPos(g2, 5) == 0
    assert gradoPos(g2, 1) == 3
    assert gradoNeg(g1, 5) == 4
    assert gradoNeg(g2, 5) == 3
    assert gradoNeg(g2, 1) == 0
    print("Verificado")

# La verificación es
#    >>> test_GradoPosNeg()
#    Verificado
