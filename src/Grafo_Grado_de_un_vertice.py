# Grafo_Grado_de_un_vertice.py
# TAD de los grafos: Grado de un vértice.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El grado de un vértice v de un grafo dirigido g, es el número de
# aristas de g que contiene a v. Si g es no dirigido, el grado de un
# vértice v es el número de aristas incidentes en v, teniendo en cuenta
# que los lazos se cuentan dos veces.
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir las funciones,
#    grado : (Grafo, Vertice) -> int
# tal que grado(g, v) es el grado del vértice v en el grafo g. Por
# ejemplo,
#    >>> g1 = creaGrafo_(Orientacion.ND, (1,5),
#                        [(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)])
#    >>> g2 = creaGrafo_(Orientacion.D, (1,5),
#                        [(1,2),(1,3),(1,5),(2,4),(2,5),(4,3),(4,5)])
#    >>> g3 = creaGrafo_(Orientacion.D, (1,3),
#                        [(1,2),(2,2),(3,1),(3,2)])
#    >>> g4 = creaGrafo_(Orientacion.D, (1,1),
#                        [(1,1)])
#    >>> g5 = creaGrafo_(Orientacion.ND, (1,3),
#                        [(1,2),(1,3),(2,3),(3,3)])
#    >>> g6 = creaGrafo_(Orientacion.D, (1,3),
#                        [(1,2),(1,3),(2,3),(3,3)])
#    >>> grado(g1, 5)
#    4
#    >>> grado(g2, 5)
#    3
#    >>> grado(g2, 1)
#    3
#    >>> grado(g3, 2)
#    4
#    >>> grado(g3, 1)
#    2
#    >>> grado(g3, 3)
#    2
#    >>> grado(g4, 1)
#    2
#    >>> grado(g5, 3)
#    4
#    >>> grado(g6, 3)
#    4
#
# Comprobar con Hypothesis que en todo grafo, el número de nodos de
# grado impar es par.
# ---------------------------------------------------------------------

from hypothesis import given

from src.Grafo_Grados_positivos_y_negativos import gradoNeg, gradoPos
from src.Grafo_Incidentes_de_un_vertice import incidentes
from src.Grafo_Lazos_de_un_grafo import lazos
from src.TAD.Grafo import (Grafo, Orientacion, Vertice, creaGrafo_, dirigido,
                           nodos)
from src.TAD.GrafoGenerador import gen_grafo


def grado(g: Grafo, v: Vertice) -> int:
    if dirigido(g):
        return gradoNeg(g, v) + gradoPos(g, v)
    if (v, v) in lazos(g):
        return len(incidentes(g, v)) + 1
    return len(incidentes(g, v))

# La propiedad es
@given(gen_grafo())
def test_grado1(g):
    assert len([v for v in nodos(g) if grado(g, v) % 2 == 1]) % 2 == 0

# La comprobación es
#    src> poetry run pytest -q Grafo_Grado_de_un_vertice.py
#    1 passed in 0.36s

# Verificación
# ============

def test_grado() -> None:
    g1 = creaGrafo_(Orientacion.ND, (1,5),
                    [(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)])
    g2 = creaGrafo_(Orientacion.D, (1,5),
                    [(1,2),(1,3),(1,5),(2,4),(2,5),(4,3),(4,5)])
    g3 = creaGrafo_(Orientacion.D, (1,3),
                    [(1,2),(2,2),(3,1),(3,2)])
    g4 = creaGrafo_(Orientacion.D, (1,1),
                    [(1,1)])
    g5 = creaGrafo_(Orientacion.ND, (1,3),
                    [(1,2),(1,3),(2,3),(3,3)])
    g6 = creaGrafo_(Orientacion.D, (1,3),
                    [(1,2),(1,3),(2,3),(3,3)])
    assert grado(g1, 5) == 4
    assert grado(g2, 5) == 3
    assert grado(g2, 1) == 3
    assert grado(g3, 2) == 4
    assert grado(g3, 1) == 2
    assert grado(g3, 3) == 2
    assert grado(g4, 1) == 2
    assert grado(g5, 3) == 4
    assert grado(g6, 3) == 4
    print("Verificado")

# La verificación es
#    >>> test_grado()
#    Verificado
