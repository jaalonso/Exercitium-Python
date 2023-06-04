# Grafo_Grafos_ciclos.py
# TAD de los grafos: Grafos ciclo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 25-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El ciclo de orden n, C(n), es un grafo no dirigido cuyo conjunto de
# vértices es {1,...,n} y las aristas son
#    (1,2), (2,3), ..., (n-1,n), (n,1)
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    grafoCiclo : (Int) -> Grafo
# tal que grafoCiclo(n) es el grafo ciclo de orden n. Por ejemplo,
#    >>> grafoCiclo(3)
#    G ND ([1, 2, 3], [(1, 2), (1, 3), (2, 3)])
# ---------------------------------------------------------------------

from src.TAD.Grafo import Grafo, Orientacion, creaGrafo_


def grafoCiclo(n: int) -> Grafo:
    return creaGrafo_(Orientacion.ND,
                      (1, n),
                      [(n,1)] + [(x, x + 1) for x in range(1, n)])

# Verificación
# ============

def test_grafoCiclo() -> None:
    assert str(grafoCiclo(3)) == \
        "G ND ([1, 2, 3], [(1, 2), (1, 3), (2, 3)])"
    print("Verificado")

# La verificación es
#    >>> test_grafoCiclo()
#    Verificado
