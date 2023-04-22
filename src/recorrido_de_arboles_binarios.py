# recorrido_de_arboles_binarios.py
# Recorrido de árboles binarios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios](https://bit.ly/3H53exA),
# definir las funciones
#    preorden  : (Arbol[A]) -> list[A]
#    postorden : (Arbol[A]) -> list[A]
# tales que
# + preorden(x) es la lista correspondiente al recorrido preorden del
#   árbol x; es decir, primero visita la raíz del árbol, a continuación
#   recorre el subárbol izquierdo y, finalmente, recorre el subárbol
#   derecho. Por ejemplo,
#      >>> preorden(N(9, N(3, H(2), H(4)), H(7)))
#      [9, 3, 2, 4, 7]
# + (postorden x) es la lista correspondiente al recorrido postorden
#   del árbol x; es decir, primero recorre el subárbol izquierdo, a
#   continuación el subárbol derecho y, finalmente, la raíz del
#   árbol. Por ejemplo,
#      >>> postorden(N(9, N(3, H(2), H(4)), H(7)))
#      [2, 4, 3, 7, 9]
#
# Comprobar con Hypothesis que la longitud de la lista obtenida
# recorriendo un árbol en cualquiera de los sentidos es igual al número
# de nodos del árbol más el número de hojas.
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.arboles_binarios import Arbol, H, N, arbolArbitrario
from src.numero_de_hojas_de_un_arbol_binario import nHojas, nNodos

A = TypeVar("A")

def preorden(a: Arbol[A]) -> list[A]:
    match a:
        case H(x):
            return [x]
        case N(x, i, d):
            return [x] + preorden(i) + preorden(d)
    assert False

def postorden(a: Arbol[A]) -> list[A]:
    match a:
        case H(x):
            return [x]
        case N(x, i, d):
            return postorden(i) + postorden(d) + [x]
    assert False

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=10))
def test_recorrido(n: int) -> None:
    a = arbolArbitrario(n)
    m = nNodos(a) + nHojas(a)
    assert len(preorden(a)) == m
    assert len(postorden(a)) == m

# La comprobación es
#    src> poetry run pytest -q recorrido_de_arboles_binarios.py
#    1 passed in 0.16s
