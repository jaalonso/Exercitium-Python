# Escalada_Prim.py
# El algoritmo de Prim del árbol de expansión mínimo por escalada.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-agosto-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El [algoritmo de Prim](https://bit.ly/466fwRe) calcula un árbol
# recubridor mínimo en un grafo conexo y ponderado. Es decir, busca un
# subconjunto de aristas que, formando un árbol, incluyen todos los
# vértices y donde el valor de la suma de todas las aristas del árbol
# es el mínimo.
#
# El algoritmo de Prim funciona de la siguiente manera:
# + Inicializar un árbol con un único vértice, elegido arbitrariamente,
#   del grafo.
# + Aumentar el árbol por un lado. Llamamos lado a la unión entre dos
#   vértices: de las posibles uniones que pueden conectar el árbol a los
#   vértices que no están aún en el árbol, encontrar el lado de menor
#   distancia y unirlo al árbol.
# + Repetir el paso 2 (hasta que todos los vértices pertenezcan al
#   árbol)
#
# Usando la [búsqueda en escalada](https://bit.ly/3Kk4A99) el [tipo
# abstracto de datos de los grafos](https://bit.ly/45cQ3Fo), definir la
# función
#    prim : (Grafo) -> list[tuple[Peso, Vertice, Vertice]]
# tal que prim(g) es el árbol de expansión mínimo del grafo g
# calculado mediante el algoritmo de Prim con bñusqueda en
# escalada. Por ejemplo, si g1, g2, g3 y g4 son los grafos definidos
# por
#    g1 = creaGrafo (Orientacion.ND,
#                    (1,5),
#                    [((1,2),12),((1,3),34),((1,5),78),
#                     ((2,4),55),((2,5),32),
#                     ((3,4),61),((3,5),44),
#                     ((4,5),93)])
#    g2 = creaGrafo (Orientacion.ND,
#                    (1,5),
#                    [((1,2),13),((1,3),11),((1,5),78),
#                     ((2,4),12),((2,5),32),
#                     ((3,4),14),((3,5),44),
#                     ((4,5),93)])
#    g3 = creaGrafo (Orientacion.ND,
#                    (1,7),
#                    [((1,2),5),((1,3),9),((1,5),15),((1,6),6),
#                     ((2,3),7),
#                     ((3,4),8),((3,5),7),
#                     ((4,5),5),
#                     ((5,6),3),((5,7),9),
#                     ((6,7),11)])
#    g4 = creaGrafo (Orientacion.ND,
#                    (1,7),
#                    [((1,2),5),((1,3),9),((1,5),15),((1,6),6),
#                     ((2,3),7),
#                     ((3,4),8),((3,5),1),
#                     ((4,5),5),
#                     ((5,6),3),((5,7),9),
#                     ((6,7),11)])
# entonces
#    prim(g1) == [((2,4),55),((1,3),34),((2,5),32),((1,2),12)]
#    prim(g2) == [((2,5),32),((2,4),12),((1,2),13),((1,3),11)]
#    prim(g3) == [((5,7),9),((2,3),7),((5,4),5),((6,5),3),((1,6),6),((1,2),5)]
#    prim(g4) == [((5,7),9),((5,4),5),((5,3),1),((6,5),3),((1,6),6),((1,2),5)]
# ---------------------------------------------------------------------

from typing import Optional

from src.BusquedaEnEscalada import buscaEscalada
from src.TAD.Grafo import (Grafo, Orientacion, Peso, Vertice, aristaEn,
                           creaGrafo, nodos, peso)

g1 = creaGrafo (Orientacion.ND,
                (1,5),
                [((1,2),12),((1,3),34),((1,5),78),
                 ((2,4),55),((2,5),32),
                 ((3,4),61),((3,5),44),
                 ((4,5),93)])
g2 = creaGrafo (Orientacion.ND,
                (1,5),
                [((1,2),13),((1,3),11),((1,5),78),
                 ((2,4),12),((2,5),32),
                 ((3,4),14),((3,5),44),
                 ((4,5),93)])
g3 = creaGrafo (Orientacion.ND,
                (1,7),
                [((1,2),5),((1,3),9),((1,5),15),((1,6),6),
                 ((2,3),7),
                 ((3,4),8),((3,5),7),
                 ((4,5),5),
                 ((5,6),3),((5,7),9),
                 ((6,7),11)])
g4 = creaGrafo (Orientacion.ND,
                (1,7),
                [((1,2),5),((1,3),9),((1,5),15),((1,6),6),
                 ((2,3),7),
                 ((3,4),8),((3,5),1),
                 ((4,5),5),
                 ((5,6),3),((5,7),9),
                 ((6,7),11)])

Arista = tuple[tuple[Vertice, Vertice], Peso]

# Un nodo (Estado (p,t,r,aem)) está formado por el peso p de la última
# arista añadida el árbol de expansión mínimo (aem), la lista t
# de nodos del grafo que están en el aem, la lista r de nodos del
# grafo que no están en el aem y el aem.
Estado = tuple[Peso, list[Vertice], list[Vertice], list[Arista]]

# inicial(g) es el estado inicial correspondiente al grafo g.
def inicial(g: Grafo) -> Estado:
    n, *ns = nodos(g)
    return (0, [n], ns, [])

# esFinal(e) se verifica si e es un estado final; es decir, si no
# queda ningún elemento en la lista de nodos sin colocar en el árbol de
# expansión mínimo.
def esFinal(e: Estado) -> bool:
    return e[2] == []

# sucesores(g, e) es la lista de los sucesores del estado e en el
# grafo g. Por ejemplo,
#    λ> sucesores(g1, (0,[1],[2,3,4,5],[]))
#    [(12,[2,1],[3,4,5],[(1,2,12)]),
#     (34,[3,1],[2,4,5],[(1,3,34)]),
#     (78,[5,1],[2,3,4],[(1,5,78)])]
def sucesores(g: Grafo, e: Estado) -> list[Estado]:
    (_,t,r,aem) = e
    return [(peso(x, y, g),
             [y] + t,
             [x for x in r if x != y],
             [((x,y),peso(x, y, g))] + aem)
            for x in t for y in r if aristaEn(g, (x, y))]

def prim(g: Grafo) -> Optional[list[Arista]]:
    r = buscaEscalada(lambda e: sucesores(g, e), esFinal, inicial(g))
    if r is None:
        return None
    return r[3]

# Verificación
# ============

def test_prim() -> None:
    assert prim(g1) == [((2,4),55),((1,3),34),((2,5),32),((1,2),12)]
    assert prim(g2) == [((2,5),32),((2,4),12),((1,2),13),((1,3),11)]
    assert prim(g3) == [((5,7),9),((2,3),7),((5,4),5),((6,5),3),((1,6),6),((1,2),5)]
    assert prim(g4) == [((5,7),9),((5,4),5),((5,3),1),((6,5),3),((1,6),6),((1,2),5)]
    print("Verificado")

# La verificación es
#    >>> test_prim()
#    Verificado
