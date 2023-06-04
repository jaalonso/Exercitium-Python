# Grafo_Lazos_de_un_grafo.py
# TAD de los grafos: Lazos de un grafo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 31-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir las funciones,
#    lazos  : (Grafo) -> list[tuple[Vertice, Vertice]]
#    nLazos : (Grafo) -> int
# tales que
# + lazos(g) es el conjunto de los lazos (es decir, aristas cuyos
#   extremos son iguales) del grafo g. Por ejemplo,
#      >>> ej1 = creaGrafo_(Orientacion.D, (1,3), [(1,1),(2,3),(3,2),(3,3)])
#      >>> ej2 = creaGrafo_(Orientacion.ND, (1,3), [(2,3),(3,1)])
#      >>> lazos(ej1)
#      [(1,1),(3,3)]
#      >>> lazos(ej2)
#      []
# + nLazos(g) es el número de lazos del grafo g. Por ejemplo,
#      >>> nLazos(ej1)
#      2
#      >>> nLazos(ej2)
#      0
# ---------------------------------------------------------------------

from src.TAD.Grafo import (Grafo, Orientacion, Vertice, aristaEn, creaGrafo_,
                           nodos)


def lazos(g: Grafo) -> list[tuple[Vertice, Vertice]]:
    return [(x, x) for x in nodos(g) if aristaEn(g, (x, x))]

def nLazos(g: Grafo) -> int:
    return len(lazos(g))

# Verificación
# ============

def test_lazos() -> None:
    ej1 = creaGrafo_(Orientacion.D, (1,3), [(1,1),(2,3),(3,2),(3,3)])
    ej2 = creaGrafo_(Orientacion.ND, (1,3), [(2,3),(3,1)])
    assert lazos(ej1) == [(1,1),(3,3)]
    assert lazos(ej2) == []
    assert nLazos(ej1) == 2
    assert nLazos(ej2) == 0
    print("Verificado")

# La verificación es
#    >>> test_lazos()
#    Verificado
