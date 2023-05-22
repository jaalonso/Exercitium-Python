# Grafo_Incidentes_de_un_vertice.py
# TAD de los grafos: Incidentes de un vértice.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# En un un grafo g, los incidentes de un vértice v es el conjuntos de
# vértices x de g para los que hay un arco (o una arista) de x a v; es
# decir, que v es adyacente a x.
#
# Usando el [tipo abstrado de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    incidentes :: (Ix v,Num p) => (Grafo v p) -> v -> [v]
# tal que (incidentes g v) es la lista de los vértices incidentes en el
# vértice v. Por ejemplo,
#    λ> g1 = creaGrafo_(Orientacion.D, (1,3), [(1,2),(2,2),(3,1),(3,2)])
#    λ> incidentes(g1,1)
#    [3]
#    λ> incidentes g1 2
#    [1,2,3]
#    λ> incidentes g1 3
#    []
#    λ> g2 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(2,2),(3,1),(3,2)])
#    λ> incidentes g2 1
#    [2,3]
#    λ> incidentes g2 2
#    [1,2,3]
#    λ> incidentes g2 3
#    [1,2]
# ---------------------------------------------------------------------

from src.TAD.Grafo import (Grafo, Orientacion, Vertice, adyacentes, creaGrafo_,
                           nodos)


def incidentes(g: Grafo, v: Vertice) -> list[Vertice]:
    return [x for x in nodos(g) if v in adyacentes(g, x)]

# Verificación
# ============

def test_incidentes() -> None:
    g1 = creaGrafo_(Orientacion.D, (1,3), [(1,2),(2,2),(3,1),(3,2)])
    g2 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(2,2),(3,1),(3,2)])
    assert incidentes(g1,1) == [3]
    assert incidentes(g1,2) == [1, 2, 3]
    assert incidentes(g1,3) == []
    assert incidentes(g2, 1) == [2, 3]
    assert incidentes(g2, 2) == [1, 2, 3]
    assert incidentes(g2, 3) == [1, 2]
    print("Verificado")

# La verificación es
#    >>> test_incidentes()
#    Verificado
