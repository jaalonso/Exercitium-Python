# Grafo_Recorrido_en_anchura.py
# TAD de los grafos: Recorrido en anchura.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    recorridoEnAnchura : (Vertice, Grafo) -> list[Vertice]
# tal que recorridoEnAnchura(i, g) es el recorrido en anchura
# del grafo g desde el vértice i. Por ejemplo, en el grafo
#
#    +---> 2 <---+
#    |           |
#    |           |
#    1 --> 3 --> 6 --> 5
#    |                 |
#    |                 |
#    +---> 4 <---------+
#
# definido por
#    grafo1: Grafo = creaGrafo_(Orientacion.D,
#                               (1,6),
#                               [(1,2),(1,3),(1,4),(3,6),(5,4),(6,2),(6,5)])
# entonces
#    recorridoEnAnchura(1, grafo1)  ==  [1,2,3,4,6,5]
# -----------------------------------------------------------

from src.TAD.Grafo import Grafo, Orientacion, Vertice, adyacentes, creaGrafo_

grafo1: Grafo = creaGrafo_(Orientacion.D,
                           (1,6),
                           [(1,2),(1,3),(1,4),(3,6),(5,4),(6,2),(6,5)])

def recorridoEnAnchura(i: Vertice, g: Grafo) -> list[Vertice]:
    def ra(cs: list[Vertice], vis: list[Vertice]) -> list[Vertice]:
        if not cs:
            return vis
        d, *ds = cs
        if d in vis:
            return ra(ds, vis)
        return ra(ds + adyacentes(g, d), [d] + vis)
    return list(reversed(ra([i], [])))

# Traza del cálculo de recorridoEnAnchura(1, grafo1)
#    recorridoEnAnchura(1, grafo1
#    = ra([1],     [])
#    = ra([2,3,4], [1])
#    = ra([3,4],   [2,1])
#    = ra([4,6],   [3,2,1])
#    = ra([6],     [4,3,2,1])
#    = ra([2,5],   [6,4,3,2,1])
#    = ra([5],     [6,4,3,2,1])
#    = ra([4],     [5,6,4,3,2,1])
#    = ra([],      [5,6,4,3,2,1])
#    = [1,2,3,4,6,5]

# Verificación
# ============

def test_recorridoEnAnchura() -> None:
    grafo2 = creaGrafo_(Orientacion.ND,
                        (1,6),
                        [(1,2),(1,3),(1,4),(3,6),(5,4),(6,2),(6,5)])
    assert recorridoEnAnchura(1, grafo1) == [1,2,3,4,6,5]
    assert recorridoEnAnchura(1, grafo2) == [1,2,3,4,6,5]
    print("Verificado")

# La verificación es
#    >>> test_recorridoEnAnchura()
#    Verificado
