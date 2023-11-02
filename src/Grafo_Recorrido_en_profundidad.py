# Grafo_Recorrido_en_profundidad.py
# TAD de los grafos: Recorrido en profundidad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    recorridoEnProfundidad : (Vertice, Grafo) -> list[Vertice]
# tal que recorridoEnProfundidad(i, g) es el recorrido en profundidad
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
#    recorridoEnProfundidad(1, grafo1)  ==  [1,2,3,6,5,4]
# -----------------------------------------------------------

from src.TAD.Grafo import Grafo, Orientacion, Vertice, adyacentes, creaGrafo_

grafo1: Grafo = creaGrafo_(Orientacion.D,
                           (1,6),
                           [(1,2),(1,3),(1,4),(3,6),(5,4),(6,2),(6,5)])

# 1ª solución
# ===========

def recorridoEnProfundidad1(i: Vertice, g: Grafo) -> list[Vertice]:
    def rp(cs: list[Vertice], vis: list[Vertice]) -> list[Vertice]:
        if not cs:
            return vis
        d, *ds = cs
        if d in vis:
            return rp(ds, vis)
        return rp(adyacentes(g, d) + ds, vis + [d])
    return rp([i], [])

# Traza del cálculo de recorridoEnProfundidad1(1, grafo1)
#    recorridoEnProfundidad1(1, grafo1)
#    = rp([1],     [])
#    = rp([2,3,4], [1])
#    = rp([3,4],   [1,2])
#    = rp([6,4],   [1,2,3])
#    = rp([2,5,4], [1,2,3,6])
#    = rp([5,4],   [1,2,3,6])
#    = rp([4,4],   [1,2,3,6,5])
#    = rp([4],     [1,2,3,6,5,4])
#    = rp([],      [1,2,3,6,5,4])
#    = [1,2,3,6,5,4]

# 2ª solución
# ===========

def recorridoEnProfundidad(i: Vertice, g: Grafo) -> list[Vertice]:
    def rp(cs: list[Vertice], vis: list[Vertice]) -> list[Vertice]:
        if not cs:
            return vis
        d, *ds = cs
        if d in vis:
            return rp(ds, vis)
        return rp(adyacentes(g, d) + ds, [d] + vis)
    return list(reversed(rp([i], [])))

# Traza del cálculo de (recorridoEnProfundidad(1, grafo1)
#    recorridoEnProfundidad(1, grafo1)
#    = reverse(rp([1],     []))
#    = reverse(rp([2,3,4], [1]))
#    = reverse(rp([3,4],   [2,1]))
#    = reverse(rp([6,4],   [3,2,1]))
#    = reverse(rp([2,5,4], [6,3,2,1]))
#    = reverse(rp([5,4],   [6,3,2,1]))
#    = reverse(rp([4,4],   [5,6,3,2,1]))
#    = reverse(rp([4],     [4,5,6,3,2,1]))
#    = reverse(rp([],      [4,5,6,3,2,1]))
#    = reverse([4,5,6,3,2,1])
#    = [1,2,3,6,5,4]

# Verificación
# ============

def test_recorridoEnProfundidad() -> None:
    grafo2 = creaGrafo_(Orientacion.ND,
                        (1,6),
                        [(1,2),(1,3),(1,4),(3,6),(5,4),(6,2),(6,5)])
    assert recorridoEnProfundidad1(1, grafo1) == [1,2,3,6,5,4]
    assert recorridoEnProfundidad1(1, grafo2) == [1,2,6,3,5,4]
    assert recorridoEnProfundidad(1, grafo1) == [1,2,3,6,5,4]
    assert recorridoEnProfundidad(1, grafo2) == [1,2,6,3,5,4]
    print("Verificado")

# La verificación es
#    >>> test_recorridoEnProfundidad()
#    Verificado
