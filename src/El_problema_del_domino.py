# El_problema_del_domino.py
# El problema del dominó mediante búsqueda en espacio de estados.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-agosto-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las fichas del dominó se pueden representar por pares de números
# enteros. El problema del dominó consiste en colocar todas las fichas
# de una lista dada de forma que el segundo número de cada ficha
# coincida con el primero de la siguiente.
#
# Definir, mediante búsqueda en espacio de estados, la función
#    domino : (Problema) -> list[list[Ficha]]
# tal que domino(fs) es la lista de las soluciones del problema del
# dominó correspondiente a las fichas fs. Por ejemplo,
#    >>> domino([(1,2),(2,3),(1,4)])
#    [[(3, 2), (2, 1), (1, 4)], [(4, 1), (1, 2), (2, 3)]]
#    >>> domino([(1,2),(1,1),(1,4)])
#    [[(2, 1), (1, 1), (1, 4)], [(4, 1), (1, 1), (1, 2)]]
#    >>> domino([(1,2),(3,4),(2,3)])
#    [[(4, 3), (3, 2), (2, 1)], [(1, 2), (2, 3), (3, 4)]]
#    >>> domino([(1,2),(2,3),(5,4)])
#    []
# ---------------------------------------------------------------------

from src.BusquedaEnProfundidad import buscaProfundidad

# Las fichas son pares de números enteros.
Ficha  = tuple[int, int]

# Un problema está definido por la lista de fichas que hay que colocar
Problema = list[Ficha]

# Los estados son los pares formados por la listas sin colocar y las
# colocadas.
Estado = tuple[list[Ficha], list[Ficha]]

# inicial(p) es el estado inicial del problema p. Por ejemplo,
#    >>> inicial([(1,2),(2,3),(1,4)])
#    ([(1, 2), (2, 3), (1, 4)], [])
def inicial(p: Problema) -> Estado:
    return (p, [])

# esFinal(e) se verifica si e es un estado final. Por ejemplo,
#    >>> esFinal(([], [(4,1),(1,2),(2,3)]))
#    True
#    >>> esFinal(([(2,3)], [(4,1),(1,2)]))
#    False
def esFinal(e: Estado) -> bool:
    return not e[0]

# elimina(f, fs) es la lista obtenida eliminando la ficha f de la lista
# fs. Por ejemplo,
#    >>> elimina((1,2),[(4,1),(1,2),(2,3)])
#    [(4, 1), (2, 3)]
def elimina(f: Ficha, fs: list[Ficha]) -> list[Ficha]:
    return [g for g in fs if g != f]

# sucesores(e) es la lista de los sucesores del estado e. Por ejemplo,
#    >>> sucesores(([(1,2),(2,3),(1,4)],[]))
#    [([(2,3),(1,4)],[(1,2)]),
#     ([(1,2),(1,4)],[(2,3)]),
#     ([(1,2),(2,3)],[(1,4)]),
#     ([(2,3),(1,4)],[(2,1)]),
#     ([(1,2),(1,4)],[(3,2)]),
#     ([(1,2),(2,3)],[(4,1)])]
#    >>> sucesores(([(2,3),(1,4)],[(1,2)]))
#    [([(2,3)],[(4,1),(1,2)])]
#    >>> sucesores(([(2,3),(1,4)],[(2,1)]))
#    [([(1,4)],[(3,2),(2,1)])]
def sucesores(e: Estado) -> list[Estado]:
    if not e[1]:
        return [(elimina((a,b), e[0]), [(a,b)]) for (a,b) in e[0] if a != b] + \
               [(elimina((a,b), e[0]), [(b,a)]) for (a,b) in e[0]]
    return [(elimina((u,v),e[0]),[(u,v)]+e[1]) for (u,v) in e[0] if u != v and v == e[1][0][0]] +\
           [(elimina((u,v),e[0]),[(v,u)]+e[1]) for (u,v) in e[0] if u != v and u == e[1][0][0]] +\
           [(elimina((u,v),e[0]),[(u,v)]+e[1]) for (u,v) in e[0] if u == v and u == e[1][0][0]]

# soluciones(p) es la lista de las soluciones del problema p. Por
# ejemplo,
#    >>> soluciones([(1,2),(2,3),(1,4)])
#    [([], [(3, 2), (2, 1), (1, 4)]), ([], [(4, 1), (1, 2), (2, 3)])]
def soluciones(p: Problema) -> list[Estado]:
    return buscaProfundidad(sucesores, esFinal, inicial(p))

def domino(p: Problema) -> list[list[Ficha]]:
    return [s[1] for s in soluciones(p)]

# # Verificación
# # ============

def test_domino() -> None:
    assert domino([(1,2),(2,3),(1,4)]) == \
        [[(3, 2), (2, 1), (1, 4)], [(4, 1), (1, 2), (2, 3)]]
    assert domino([(1,2),(1,1),(1,4)]) == \
        [[(2, 1), (1, 1), (1, 4)], [(4, 1), (1, 1), (1, 2)]]
    assert domino([(1,2),(3,4),(2,3)]) == \
        [[(4, 3), (3, 2), (2, 1)], [(1, 2), (2, 3), (3, 4)]]
    assert domino([(1,2),(2,3),(5,4)]) == \
        []
    print("Verificado")

# La verificación es
#    >>> test_domino()
#    Verificado
