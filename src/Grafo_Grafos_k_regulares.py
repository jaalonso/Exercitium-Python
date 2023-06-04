# Grafo_Grafos_k_regulares.py
# TAD de los grafos: Grafos k-regulares.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un grafo es k-regular si todos sus vértices son de grado k.
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    regularidad : (Grafo) -> Optional[int]
# tal que regularidad(g) es la regularidad de g. Por ejemplo,
#    regularidad(creaGrafo_(Orientacion.ND, (1,2), [(1,2),(2,3)]) == 1
#    regularidad(creaGrafo_(Orientacion.D, (1,2), [(1,2),(2,3)])  == None
#    regularidad(completo(4))                                     == 3
#    regularidad(completo(5))                                     == 4
#    regularidad(grafoCiclo(4))                                   == 2
#    regularidad(grafoCiclo(5))                                   == 2
#
# Comprobar que el grafo completo de orden n es (n-1)-regular (para
# n de 1 a 20) y el grafo ciclo de orden n es 2-regular (para n de
# 3 a 20).
# ---------------------------------------------------------------------

from typing import Optional

from src.Grafo_Grado_de_un_vertice import grado
from src.Grafo_Grafos_ciclos import grafoCiclo
from src.Grafo_Grafos_completos import completo
from src.Grafo_Grafos_regulares import regular
from src.TAD.Grafo import Grafo, Orientacion, creaGrafo_, nodos


def regularidad(g: Grafo) -> Optional[int]:
    if regular(g):
        return grado(g, nodos(g)[0])
    return None

# La propiedad de k-regularidad de los grafos completos es
def prop_completoRegular(n: int) -> bool:
    return regularidad(completo(n)) == n - 1

# La comprobación es
#    >>> all(prop_completoRegular(n) for n in range(1, 21))
#    True

# La propiedad de k-regularidad de los grafos ciclos es
def prop_cicloRegular(n: int) -> bool:
    return regularidad(grafoCiclo(n)) == 2

# La comprobación es
#    >>> all(prop_cicloRegular(n) for n in range(3, 21))
#    True

# Verificación
# ============

def test_k_regularidad() -> None:
    g1 = creaGrafo_(Orientacion.ND, (1,2), [(1,2),(2,3)])
    g2 = creaGrafo_(Orientacion.D, (1,2), [(1,2),(2,3)])
    assert regularidad(g1) == 1
    assert regularidad(g2) is None
    assert regularidad(completo(4)) == 3
    assert regularidad(completo(5)) == 4
    assert regularidad(grafoCiclo(4)) == 2
    assert regularidad(grafoCiclo(5)) == 2
    print("Verificado")

# La verificación es
#    >>> test_k_regularidad()
#    Verificado
