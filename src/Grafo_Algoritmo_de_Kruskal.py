# Grafo_Algoritmo_de_Kruskal.py
# TAD de los grafos: Algoritmo de Kruskal.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El [algoritmo de Kruskal]()https://bit.ly/3N8bOOg) calcula un árbol
# recubridor mínimo en un grafo conexo y ponderado. Es decir, busca un
# subconjunto de aristas que, formando un árbol, incluyen todos los
# vértices y donde el valor de la suma de todas las aristas del árbol
# es el mínimo.
#
# El algoritmo de Kruskal funciona de la siguiente manera:
# + se crea un bosque B (un conjunto de árboles), donde cada vértice
#   del grafo es un árbol separado
# + se crea un conjunto C que contenga a todas las aristas del grafo
# + mientras C es no vacío,
#   + eliminar una arista de peso mínimo de C
#   + si esa arista conecta dos árboles diferentes se añade al bosque,
#     combinando los dos árboles en un solo árbol
#   + en caso contrario, se desecha la arista
# Al acabar el algoritmo, el bosque tiene un solo componente, el cual
# forma un árbol de expansión mínimo del grafo.
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    kruskal : (Grafo) -> list[tuple[Peso, Vertice, Vertice]]
# tal que kruskal(g) es el árbol de expansión mínimo del grafo g calculado
# mediante el algoritmo de Kruskal. Por ejemplo, si g1, g2, g3 y g4 son
# los grafos definidos por
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
#    kruskal(g1) == [(55,2,4),(34,1,3),(32,2,5),(12,1,2)]
#    kruskal(g2) == [(32,2,5),(13,1,2),(12,2,4),(11,1,3)]
#    kruskal(g3) == [(9,5,7),(7,2,3),(6,1,6),(5,4,5),(5,1,2),(3,5,6)]
#    kruskal(g4) == [(9,5,7),(6,1,6),(5,4,5),(5,1,2),(3,5,6),(1,3,5)]
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

# raiz(d, n) es la raíz de n en el diccionario. Por ejemplo,
#    raiz({1:1, 3:1, 4:3, 5:4, 2:6, 6:6}, 5)  == 1
#    raiz({1:1, 3:1, 4:3, 5:4, 2:6, 6:6}, 2)  == 6
def raiz(d: dict[Vertice, Vertice], x: Vertice) -> Vertice:
    v = d[x]
    if v == x:
        return v
    return raiz(d, v)

# modificaR(x, y, y_, d) actualiza d como sigue:
# + el valor de todas las claves z con valor y es y_
# + el valor de todas las claves z con (z > x) con valor x es y_
def modificaR(x: Vertice,
              y: Vertice,
              y_: Vertice,
              d: dict[Vertice, Vertice]) -> dict[Vertice, Vertice]:
    def aux1(vs: list[Vertice],
             tb: dict[Vertice, Vertice],
             y: Vertice) -> dict[Vertice, Vertice]:
        for a in vs:
            if tb[a] == y:
                tb[a] = y_
        return tb

    def aux2(vs: list[Vertice],
             tb: dict[Vertice, Vertice],
             y_: Vertice) -> dict[Vertice, Vertice]:
        for b in vs:
            if tb[b] == x:
                tb[b] = y_
        return tb

    cs = list(d.keys())
    ds = [c for c in cs if c > x]

    tb = aux1(cs, d, y)
    tb = aux2(ds, tb, y_)

    return tb

# buscaActualiza(a, d) es el par formado por False y el diccionario d,
# si los dos vértices de la arista a tienen la misma raíz en d y el par
# formado por True y la tabla obtenida añadiéndole a d la arista
# formada por el vértice de a de mayor raíz y la raíz del vértice de a
# de menor raíz. Y actualizando las raices de todos los elementos
# afectados por la raíz añadida. Por ejemplo,
#    >>> buscaActualiza((5,4), {1:1, 2:1, 3:3, 4:4, 5:5, 6:5, 7:7})
#    (True, {1: 1, 2: 1, 3: 3, 4: 4, 5: 4, 6: 4, 7: 7})
#    >>> buscaActualiza((6,1), {1:1, 2:1, 3:3, 4:4, 5:4, 6:4, 7:7})
#    (True, {1: 1, 2: 1, 3: 3, 4: 1, 5: 1, 6: 1, 7: 7})
#    >>> buscaActualiza((6,2), {1:1, 2:1, 3:3, 4:1, 5:4, 6:5, 7:7})
#    (False, {1: 1, 2: 1, 3: 3, 4: 1, 5: 4, 6: 5, 7: 7})
def buscaActualiza(a: tuple[Vertice, Vertice],
                   d: dict[Vertice, Vertice]) -> tuple[bool,
                                                       dict[Vertice, Vertice]]:
    x, y = a
    x_ = raiz(d, x)
    y_ = raiz(d, y)

    if x_ == y_:
        return False, d
    if y_ < x_:
        return True, modificaR(x, d[x], y_, d)
    return True, modificaR(y, d[y], x_, d)

def kruskal(g: Grafo) -> list[tuple[Peso, Vertice, Vertice]]:
    def aux(as_: list[tuple[Peso, Vertice, Vertice]],
            d: dict[Vertice, Vertice],
            ae: list[tuple[Peso, Vertice, Vertice]],
            n: int) -> list[tuple[Peso, Vertice, Vertice]]:
        if n == 0:
            return ae
        p, x, y = as_[0]
        actualizado, d = buscaActualiza((x, y), d)
        if actualizado:
            return aux(as_[1:], d, [(p, x, y)] + ae, n - 1)
        return aux(as_[1:], d, ae, n)
    return aux(list(sorted([(p, x, y) for ((x, y), p) in aristas(g)])),
               {x: x for x in nodos(g)},
               [],
               len(nodos(g)) - 1)

# Traza del diccionario correspondiente al grafo g3
# =================================================

# Lista de aristas, ordenadas según su peso:
# [(3,5,6),(5,1,2),(5,4,5),(6,1,6),(7,2,3),(7,3,5),(8,3,4),(9,1,3),(9,5,7),(11,6,7),(15,1,5)]
#
# Inicial
#   {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7}
#
# Después de añadir la arista (5,6) de peso 3
#   {1:1, 2:2, 3:3, 4:4, 5:5, 6:5, 7:7}
#
# Después de añadir la arista (1,2) de peso 5
#   {1:1, 2:1, 3:3, 4:4, 5:5, 6:5, 7:7}
#
# Después de añadir la arista (4,5) de peso 5
#   {1:1, 2:1, 3:3, 4:4, 5:4, 6:4, 7:7}
#
# Después de añadir la arista (1,6) de peso 6
#   {1:1, 2:1, 3:3, 4:1, 5:1, 6:1, 7:7}
#
# Después de añadir la arista (2,3) de peso 7
#   {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:7}
#
# Las posibles aristas a añadir son:
# + la (3,5) con peso 7, que no es posible pues la raíz de 3
#   coincide con la raíz de 5, por lo que formaría un ciclo
# + la (3,4) con peso 8, que no es posible pues la raíz de 3
#   coincide con la raíz de 4, por lo que formaría un ciclo
# + la (1,3) con peso 9, que no es posible pues la raíz de 3
#   coincide con la raíz de 1, por lo que formaría un ciclo
# + la (5,7) con peso 9, que no forma ciclo
#
# Después de añadir la arista (5,7) con peso 9
#    {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1}
#
# No es posible añadir más aristas, pues formarían ciclos.

# Verificación
# ============

def test_kruskal() -> None:
    assert kruskal(g1) == [(55,2,4),(34,1,3),(32,2,5),(12,1,2)]
    assert kruskal(g2) == [(32,2,5),(13,1,2),(12,2,4),(11,1,3)]
    assert kruskal(g3) == [(9,5,7),(7,2,3),(6,1,6),(5,4,5),(5,1,2),(3,5,6)]
    assert kruskal(g4) == [(9,5,7),(6,1,6),(5,4,5),(5,1,2),(3,5,6),(1,3,5)]
    print("Vefificado")

# La verificación es
#    >>> test_kruskal()
#    Vefificado
