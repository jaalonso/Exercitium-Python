# arboles_con_la_misma_forma.py
# Árboles con la misma forma.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 8-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios con los valores en las hojas]
# (https://bit.ly/3N5RuyE), definir la función
#    mismaForma : (Arbol[A], Arbol[B]) -> bool
# tal que mismaForma(t1, t2) se verifica si t1 y t2 tienen la misma
# estructura. Por ejemplo,
#    >>> arbol1 = Hoja(5)
#    >>> arbol2 = Hoja(3)
#    >>> mismaForma(arbol1, arbol2)
#    True
#    >>> arbol3 = Nodo(Hoja(6), Hoja(7))
#    >>> mismaForma(arbol1, arbol3)
#    False
#    >>> arbol4 = Nodo(Hoja(9), Hoja(5))
#    >>> mismaForma(arbol3, arbol4)
#    True
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.aplicacion_de_una_funcion_a_un_arbol import mapArbol
from src.arbol_binario_valores_en_hojas import (Arbol, Hoja, Nodo,
                                                arbolArbitrario)

A = TypeVar("A")
B = TypeVar("B")

# -- 1ª solución
# -- ===========

def mismaForma1(a: Arbol[A], b: Arbol[B]) -> bool:
    match (a, b):
        case (Hoja(_), Hoja(_)):
            return True
        case (Nodo(i1, d1), Nodo(i2, d2)):
            return mismaForma1(i1, i2) and mismaForma1(d1, d2)
        case (_, _):
            return False
    assert False

# -- 2ª solución
# -- ===========

def mismaForma2(a: Arbol[A], b: Arbol[B]) -> bool:
    return mapArbol(lambda x: 0, a) == mapArbol(lambda x: 0, b)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=10),
       st.integers(min_value=1, max_value=10))
def test_mismaForma(n1: int, n2: int) -> None:
    a1 = arbolArbitrario(n1)
    a2 = arbolArbitrario(n2)
    assert mismaForma1(a1, a2) == mismaForma2(a1, a2)

# La comprobación es
#    src> poetry run pytest -q arboles_con_la_misma_forma.py
#    1 passed in 0.22s
