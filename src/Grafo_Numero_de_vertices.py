# Grafo_Numero_de_vertices.py
# TAD de los grafos: Número de vértices.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 26-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    nVertices : (Grafo) -> int
# tal que nVertices(g) es el número de vértices del grafo g. Por
# ejemplo,
#    >>> nVertices(creaGrafo_(Orientacion.D, (1,5), [(1,2),(3,1)]))
#    5
#    >>> nVertices(creaGrafo_(Orientacion.ND, (2,4), [(1,2),(3,1)]))
#    3
# ---------------------------------------------------------------------

from src.TAD.Grafo import Grafo, Orientacion, creaGrafo_, nodos


def nVertices(g: Grafo) -> int:
    return len(nodos(g))

# Verificación
# ============

def test_nVertices() -> None:
    assert nVertices(creaGrafo_(Orientacion.D, (1,5), [(1,2),(3,1)])) == 5
    assert nVertices(creaGrafo_(Orientacion.ND, (2,4), [(1,2),(3,1)])) == 3
    print("Verificado")

# La verificación es
#    >>> test_nVertices()
#    Verificado
