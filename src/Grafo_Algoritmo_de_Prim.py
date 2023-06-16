# Grafo_Algoritmo_de_Prim.py
# TAD de los grafos: Algoritmo de Prim.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-junio-2023
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
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    prim : (Grafo) -> list[tuple[Peso, Vertice, Vertice]]
# tal que prim(g) es el árbol de expansión mínimo del grafo g
# calculado mediante el algoritmo de Prim. Por ejemplo, si g1, g2, g3 y
# g4 son los grafos definidos por
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
#    prim(g1)  == [(55,2,4),(34,1,3),(32,2,5),(12,1,2)]
#    prim(g2)  == [(32,2,5),(12,2,4),(13,1,2),(11,1,3)]
#    prim(g3)  == [(9,5,7),(7,2,3),(5,5,4),(3,6,5),(6,1,6),(5,1,2)]
# ---------------------------------------------------------------------

from src.TAD.Grafo import (Grafo, Orientacion, Peso, Vertice, aristas,
                           creaGrafo, nodos)

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

def prim(g: Grafo) -> list[tuple[Peso, Vertice, Vertice]]:
    n, *ns = nodos(g)
    def prim_(t: list[Vertice],
              r: list[Vertice],
              ae: list[tuple[Peso, Vertice, Vertice]],
              as_: list[tuple[tuple[Vertice, Vertice], Peso]]) \
              -> list[tuple[Peso, Vertice, Vertice]]:
        if not as_:
            return []
        if not r:
            return ae
        e = min(((c,u,v)
                 for ((u,v),c) in as_
                 if u in t and v in r))
        (_,_, v_) = e
        return prim_([v_] + t, [x for x in r if x != v_], [e] + ae, as_)
    return prim_([n], ns, [], aristas(g))

# Verificación
# ============

def test_prim() -> None:
    assert prim(g1)  == [(55,2,4),(34,1,3),(32,2,5),(12,1,2)]
    assert prim(g2)  == [(32,2,5),(12,2,4),(13,1,2),(11,1,3)]
    assert prim(g3)  == [(9,5,7),(7,2,3),(5,5,4),(3,6,5),(6,1,6),(5,1,2)]
    print("Verificado")

# La verificación es
#    >>> test_prim()
#    Verificado
