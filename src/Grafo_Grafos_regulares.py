# Grafo_Grafos_regulares.py
# TAD de los grafos: Grafos regulares.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 8-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un grafo es regular si todos sus vértices tienen el mismo
# grado.
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    regular : (Grafo) -> bool
# tal que regular(g) se verifica si el grafo g es regular. Por ejemplo,
#    >>> regular(creaGrafo_(Orientacion.D, (1,3), [(1,2),(2,3),(3,1)]))
#    True
#    >>> regular(creaGrafo_(Orientacion.ND, (1,3), [(1,2),(2,3)]))
#    False
#    >>> regular(completo(4))
#    True
#
# Comprobar que los grafos completos son regulares.
# ---------------------------------------------------------------------

from src.Grafo_Grado_de_un_vertice import grado
from src.Grafo_Grafos_completos import completo
from src.TAD.Grafo import Grafo, Orientacion, creaGrafo_, nodos


def regular(g: Grafo) -> bool:
    vs = nodos(g)
    k = grado(g, vs[0])
    return all(grado(g, v) == k for v in vs)

# La propiedad de la regularidad de todos los grafos completos de orden
# entre m y n es
def prop_CompletoRegular(m: int, n: int) -> bool:
    return all(regular(completo(x)) for x in range(m, n + 1))

# La comprobación es
#    >>> prop_CompletoRegular(1, 30)
#    True

# Verificación
# ============

def test_regular() -> None:
    g1 = creaGrafo_(Orientacion.D, (1,3), [(1,2),(2,3),(3,1)])
    g2 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(2,3)])
    assert regular(g1)
    assert not regular(g2)
    assert regular(completo(4))
    print("Verificado")

# La verificación es
#    >>> test_regular()
#    Verificado
