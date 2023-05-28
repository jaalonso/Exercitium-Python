from hypothesis import strategies as st
from hypothesis.strategies import composite

from src.TAD.Grafo import Orientacion, creaGrafo_


# Generador de aristas. Por ejemplo,
#    >>> gen_aristas(5).example()
#    [(2, 5), (4, 5), (1, 2), (2, 3), (4, 1)]
#    >>> gen_aristas(5).example()
#    [(3, 4)]
#    >>> gen_aristas(5).example()
#    [(5, 3), (3, 2), (1, 3), (5, 2)]
@composite
def gen_aristas(draw, n):
    as_ = draw(st.lists(st.tuples(st.integers(1,n),
                                  st.integers(1,n)),
                        unique=True))
    return as_

# Generador de grafos no dirigidos. Por ejemplo,
#    >>> gen_grafoND().example()
#    G ND ([1, 2, 3, 4, 5], [(1, 4), (5, 5)])
#    >>> gen_grafoND().example()
#    G ND ([1], [])
#    >>> gen_grafoND().example()
#    G ND ([1, 2, 3, 4, 5, 6, 7, 8], [(7, 7)])
#    >>> gen_grafoND().example()
#    G ND ([1, 2, 3, 4, 5, 6], [(1, 3), (2, 4), (3, 3), (3, 5)])
@composite
def gen_grafoND(draw):
    n = draw(st.integers(1,10))
    as_ = [(x, y) for (x, y ) in draw(gen_aristas(n)) if x <= y]
    return creaGrafo_(Orientacion.ND, (1,n), as_)

# Generador de grafos dirigidos. Por ejemplo,
#    >>> gen_grafoD().example()
#    G D ([1, 2, 3, 4], [(3, 3), (4, 1)])
#    >>> gen_grafoD().example()
#    G D ([1, 2], [(1, 1), (2, 1), (2, 2)])
#    >>> gen_grafoD().example()
#    G D ([1, 2], [])
@composite
def gen_grafoD(draw):
    n = draw(st.integers(1,10))
    as_ = draw(gen_aristas(n))
    return creaGrafo_(Orientacion.D, (1,n), as_)

# Generador de grafos. Por ejemplo,
#    >>> gen_grafo().example()
#    G ND ([1, 2, 3, 4, 5, 6, 7], [(1, 3)])
#    >>> gen_grafo().example()
#    G D ([1], [])
#    >>> gen_grafo().example()
#    G D ([1, 2, 3, 4, 5, 6, 7], [(1, 3), (3, 4), (5, 5)])
@composite
def gen_grafo(draw):
    o = draw(st.sampled_from([Orientacion.D, Orientacion.ND]))
    if o == Orientacion.ND:
        return draw(gen_grafoND())
    return draw(gen_grafoD())
