# Grafo_Nodos_conectados_en_un_grafo.py
# TAD de los grafos: Nodos conectados en un grafo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 21-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    conectados : (Grafo, Vertice, Vertice) -> bool
# tal que conectados(g, v1, v2) se verifica si los vértices v1 y v2
# están conectados en el grafo g. Por ejemplo, si grafo1 es el grafo
# definido por
#    grafo1 = creaGrafo_(Orientacion.D,
#                        (1,6),
#                        [(1,3),(1,5),(3,5),(5,1),(5,50),
#                         (2,4),(2,6),(4,6),(4,4),(6,4)])
# entonces,
#    conectados grafo1 1 3  ==  True
#    conectados grafo1 1 4  ==  False
#    conectados grafo1 6 2  ==  False
#    conectados grafo1 3 1  ==  True
# ----------------------------------------------------------------------------

from src.TAD.Grafo import Grafo, Orientacion, Vertice, adyacentes, creaGrafo_


def unionV(xs: list[Vertice], ys: list[Vertice]) -> list[Vertice]:
    return list(set(xs) | set(ys))

def conectadosAux(g: Grafo, vs: list[Vertice], ws: list[Vertice]) -> list[Vertice]:
    if not ws:
        return vs
    w, *ws = ws
    if w in vs:
        return conectadosAux(g, vs, ws)
    return conectadosAux(g, unionV([w], vs), unionV(ws, adyacentes(g, w)))

def conectados(g: Grafo, v1: Vertice, v2: Vertice) -> bool:
    return v2 in conectadosAux(g, [], [v1])


# Verificación
# ============

def test_conectados() -> None:
    grafo1 = creaGrafo_(Orientacion.D,
                        (1,6),
                        [(1,3),(1,5),(3,5),(5,1),(5,50),
                         (2,4),(2,6),(4,6),(4,4),(6,4)])
    grafo2 = creaGrafo_(Orientacion.ND,
                        (1,6),
                        [(1,3),(1,5),(3,5),(5,1),(5,50),
                         (2,4),(2,6),(4,6),(4,4),(6,4)])
    assert conectados(grafo1, 1, 3)
    assert not conectados(grafo1, 1, 4)
    assert not conectados(grafo1, 6, 2)
    assert conectados(grafo1, 3, 1)
    assert conectados(grafo2, 1, 3)
    assert not conectados(grafo2, 1, 4)
    assert conectados(grafo2, 6, 2)
    assert conectados(grafo2, 3, 1)
    print("Verificado")

# La verificación es
#    >>> test_conectados()
#    Verificado
