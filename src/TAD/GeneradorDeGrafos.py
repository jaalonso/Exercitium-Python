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

# Generador de grafos. Por ejemplo,
#    >>> gen_grafo().example()
#    G ND ([1, 2, 3, 4, 5, 6, 7], [(1, 3)])
#    >>> gen_grafo().example()
#    G D ([1], [])
#    >>> gen_grafo().example()
#    G D ([1, 2, 3, 4, 5, 6, 7], [(1, 3), (3, 4), (5, 5)])
@composite
def gen_grafo(draw):
    n = draw(st.integers(1,10))
    o = draw(st.sampled_from([Orientacion.D, Orientacion.ND]))
    as_ = draw(gen_aristas(n))
    return creaGrafo_(o, (1,n), as_)
