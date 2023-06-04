# Grafo_Numero_de_aristas_de_un_grafo.py
# TAD de los grafos: Número de aristas de un grafo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-junio-2023
# ======================================================================

#  ---------------------------------------------------------------------
#  Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
#  definir la función,
#     nAristas : (Grafo) -> int
#  tal que nAristas(g) es el número de aristas del grafo g. Si g es no
#  dirigido, las aristas de v1 a v2 y de v2 a v1 sólo se cuentan una
#  vez. Por ejemplo,
#     g1 = creaGrafo_(Orientacion.ND, (1,5), [(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)])
#     g2 = creaGrafo_(Orientacion.D, (1,5), [(1,2),(1,3),(1,5),(2,4),(2,5),(4,3),(4,5)])
#     g3 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(1,3),(2,3),(3,3)])
#     g4 = creaGrafo_(Orientacion.ND, (1,4), [(1,1),(1,2),(3,3)])
#     >>> nAristas(g1)
#     8
#     >>> nAristas(g2)
#     7
#     >>> nAristas(g3)
#     4
#     >>> nAristas(g4)
#     3
#     >>> nAristas(completo(4))
#     6
#     >>> nAristas(completo(5))
#     10
#
#  Definir la función
#     prop_nAristasCompleto : (int) -> bool
#  tal que prop_nAristasCompleto(n) se verifica si el número de aristas
#  del grafo completo de orden n es n*(n-1)/2 y, usando la función,
#  comprobar que la propiedad se cumple para n de 1 a 20.
#  ---------------------------------------------------------------------

from src.Grafo_Grafos_completos import completo
from src.Grafo_Lazos_de_un_grafo import nLazos
from src.TAD.Grafo import Grafo, Orientacion, aristas, creaGrafo_, dirigido

# 1ª solución
# ===========

def nAristas(g: Grafo) -> int:
    if dirigido(g):
        return len(aristas(g))
    return (len(aristas(g)) + nLazos(g)) // 2

# 2ª solución
# ===========

def nAristas2(g: Grafo) -> int:
    if dirigido(g):
        return len(aristas(g))
    return len([(x, y) for ((x,y),_) in aristas(g) if x <= y])

# Propiedad
# =========

def prop_nAristasCompleto(n: int) -> bool:
    return nAristas(completo(n)) == n*(n-1) // 2

# La comprobación es
#    >>> all(prop_nAristasCompleto(n) for n in range(1, 21))
#    True

# Verificación
# ============

def test_nAristas() -> None:
    g1 = creaGrafo_(Orientacion.ND, (1,5),
                    [(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)])
    g2 = creaGrafo_(Orientacion.D, (1,5),
                    [(1,2),(1,3),(1,5),(2,4),(2,5),(4,3),(4,5)])
    g3 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(1,3),(2,3),(3,3)])
    g4 = creaGrafo_(Orientacion.ND, (1,4), [(1,1),(1,2),(3,3)])
    for nAristas_ in [nAristas, nAristas2]:
        assert nAristas_(g1) == 8
        assert nAristas_(g2) == 7
        assert nAristas_(g3) == 4
        assert nAristas_(g4) == 3
        assert nAristas_(completo(4)) == 6
        assert nAristas_(completo(5)) == 10
    print("Verificado")

# La verificación es
#    >>> test_nAristas()
#    Verificado
