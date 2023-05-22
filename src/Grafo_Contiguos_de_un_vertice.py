# Grafo_Contiguos_de_un_vertice.py
# TAD de los grafos: Contiguos de un vértice.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# En un un grafo g, los contiguos de un vértice v es el conjuntos de
# vértices x de g tales que x es adyacente o incidente con v.
#
# Usando el [tipo abstrado de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    contiguos : (Grafo, Vertice) -> list[Vertice]
# tal que (contiguos g v) es el conjunto de los vértices de g contiguos
# con el vértice v. Por ejemplo,
#    >>> g1 = creaGrafo_(Orientacion.D, (1,3), [(1,2),(2,2),(3,1),(3,2)])
#    >>> contiguos(g1, 1)
#    [2, 3]
#    >>> contiguos(g1, 2)
#    [1, 2, 3]
#    >>> contiguos(g1, 3)
#    [1, 2]
#    >>> g2 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(2,2),(3,1),(3,2)])
#    >>> contiguos(g2, 1)
#    [2, 3]
#    >>> contiguos(g2, 2)
#    [1, 2, 3]
#    >>> contiguos(g2, 3)
#    [1, 2]
# ---------------------------------------------------------------------


from src.Grafo_Incidentes_de_un_vertice import incidentes
from src.TAD.Grafo import Grafo, Orientacion, Vertice, adyacentes, creaGrafo_


def contiguos(g: Grafo, v: Vertice) -> list[Vertice]:
    return list(set(adyacentes(g, v) + incidentes(g, v)))

# Verificación
# ============

def test_contiguos() -> None:
    g1 = creaGrafo_(Orientacion.D, (1,3), [(1,2),(2,2),(3,1),(3,2)])
    g2 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(2,2),(3,1),(3,2)])
    assert contiguos(g1, 1) == [2, 3]
    assert contiguos(g1, 2) == [1, 2, 3]
    assert contiguos(g1, 3) == [1, 2]
    assert contiguos(g2, 1) == [2, 3]
    assert contiguos(g2, 2) == [1, 2, 3]
    assert contiguos(g2, 3) == [1, 2]
    print("Verificado")

# La verificación es
#    >>> test_contiguos()
#    Verificado
