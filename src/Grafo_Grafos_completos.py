# Grafo_Grafos_completos.hs
# Grafos completos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El grafo completo de orden n, K(n), es un grafo no dirigido cuyos
# conjunto de vértices es {1,..n} y tiene una arista entre cada par de
# vértices distintos.
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    completo : (int) -> Grafo
# tal que completo(n) es el grafo completo de orden n. Por ejemplo,
#    >>> completo(4)
#    G ND ([1, 2, 3, 4],
#          [((1, 2), 0), ((1, 3), 0), ((1, 4), 0),
#           ((2, 1), 0), ((2, 3), 0), ((2, 4), 0),
#           ((3, 1), 0), ((3, 2), 0), ((3, 4), 0),
#           ((4, 1), 0), ((4, 2), 0), ((4, 3), 0)])
# ---------------------------------------------------------------------

from src.TAD.Grafo import Grafo, Orientacion, creaGrafo_


def completo(n: int) -> Grafo:
    return creaGrafo_(Orientacion.ND,
                      (1, n),
                      [(x, y)
                       for x in range(1, n + 1)
                       for y in range(x + 1, n+1)])

# Verificación
# ============

def test_completo() -> None:
    assert str(completo(4)) == \
        "G ND ([1, 2, 3, 4], [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])"
    print("Verificado")

# La verificación es
#    >>> test_completo()
#    Verificado
