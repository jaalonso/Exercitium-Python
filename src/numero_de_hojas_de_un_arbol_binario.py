# numero_de_hojas_de_un_arbol_binario.py
# Número de hojas y nodos de un árbol binario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios](???), definir las funciones
#    nHojas : (Arbol[A]) -> int
#    nNodos : (Arbol[A]) -> int
# tales que
# + nHojas(x) es el número de hojas del árbol x. Por ejemplo,
#      nHojas(N(9, N(3, H(2), H(4)), H(7)))  ==  3
# + nNodos(x) es el número de nodos del árbol x. Por ejemplo,
#      nNodos(N(9, N(3, H(2), H(4)), H(7)))  ==  2
#
# Comprobar con Hypothesis que en todo árbol binario el número de sus
# hojas es igual al número de sus nodos más uno.
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.arboles_binarios import Arbol, H, N, arbolArbitrario

A = TypeVar("A")

def nHojas(a: Arbol[A]) -> int:
    match a:
        case H(_):
            return 1
        case N(_, i, d):
            return nHojas(i) + nHojas(d)
    assert False

def nNodos(a: Arbol[A]) -> int:
    match a:
        case H(_):
            return 0
        case N(_, i, d):
            return 1 + nNodos(i) + nNodos(d)
    assert False

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=10))
def test_nHojas(n: int) -> None:
    a = arbolArbitrario(n)
    assert nHojas(a) == nNodos(a) + 1

# La comprobación es
#    src> poetry run pytest -q numero_de_hojas_de_un_arbol_binario.py
#    1 passed in 0.10s
