# Grafo_Grafos_conexos.py
# TAD de los grafos: Grafos conexos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un grafo no dirigido G se dice conexo, si para cualquier par de
# vértices u y v en G, existe al menos una trayectoria (una  sucesión
# de vértices adyacentes) de u a v.
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    conexo :: (Grafo) -> bool
# tal que (conexo g) se verifica si el grafo g es conexo. Por ejemplo,
#    conexo (creaGrafo_(Orientacion.ND, (1,3), [(1,2),(3,2)]))       == True
#    conexo (creaGrafo_(Orientacion.ND, (1,4), [(1,2),(3,2),(4,1)])) == True
#    conexo (creaGrafo_(Orientacion.ND, (1,4), [(1,2),(3,4)]))       == False
# ---------------------------------------------------------------------

from src.Grafo_Recorrido_en_anchura import recorridoEnAnchura
from src.TAD.Grafo import Grafo, Orientacion, creaGrafo_, nodos


def conexo(g: Grafo) -> bool:
    xs = nodos(g)
    i = xs[0]
    n = len(xs)
    return len(recorridoEnAnchura(i, g)) == n

# Verificación
# ============

def test_conexo() -> None:
    g1 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(3,2)])
    g2 = creaGrafo_(Orientacion.ND, (1,4), [(1,2),(3,2),(4,1)])
    g3 = creaGrafo_(Orientacion.ND, (1,4), [(1,2),(3,4)])
    assert conexo(g1)
    assert conexo(g2)
    assert not conexo(g3)
    print("Verificado")

# La verificación es
#    >>> test_conexo()
#    Verificado
