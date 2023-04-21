# subarbol_de_profundidad_dada.py
# Subárbol de profundidad dada.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 21-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios](???), definir la función
#    takeArbol : (int, Arbol[A]) -> Arbol[A]
# tal que takeArbol(n, t) es el subárbol de t de profundidad n. Por
# ejemplo,
#    >>> takeArbol(0, N(9, N(3, H(2), H(4)), H(7)))
#    H(9)
#    >>> takeArbol(1, N(9, N(3, H(2), H(4)), H(7)))
#    N(9, H(3), H(7))
#    >>> takeArbol(2, N(9, N(3, H(2), H(4)), H(7)))
#    N(9, N(3, H(2), H(4)), H(7))
#    >>> takeArbol(3, N(9, N(3, H(2), H(4)), H(7)))
#    N(9, N(3, H(2), H(4)), H(7))
#
# Comprobar con Hypothesis que la profundidad de takeArbol(n, x) es
# menor o igual que n, para todo número natural n y todo árbol x.
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.arboles_binarios import Arbol, H, N, arbolArbitrario
from src.profundidad_de_un_arbol_binario import profundidad

A = TypeVar("A")

def takeArbol(n: int, a: Arbol[A]) -> Arbol[A]:
    match (n, a):
        case (_, H(x)):
            return H(x)
        case (0, N(x, _, _)):
            return H(x)
        case (n, N(x, i, d)):
            return N(x, takeArbol(n - 1, i), takeArbol(n - 1, d))
    assert False

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=12),
       st.integers(min_value=1, max_value=10))
def test_takeArbol(n: int, m: int) -> None:
    x = arbolArbitrario(m)
    assert profundidad(takeArbol(n, x)) <= n

# La comprobación es
#    src> poetry run pytest -q subarbol_de_profundidad_dada.py
#    1 passed in 0.23s
