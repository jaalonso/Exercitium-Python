# imagen_especular_de_un_arbol_binario.py
# Imagen especular de un árbol binario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios](https://bit.ly/3H53exA),
# definir la función
#    espejo : (Arbol[A]) -> Arbol[A]
# tal que espejo(x) es la imagen especular del árbol x. Por ejemplo,
#    espejo(N(9, N(3, H(2), H(4)), H(7))) == N(9, H(7), N(3, H(4), H(2)))
#
# Comprobar con Hypothesis las siguientes propiedades, para todo árbol
# x,
#    espejo(espejo(x)) = x
#    list(reversed(preorden(espejo(x)))) == postorden(x)
#    postorden(espejo(x)) == list(reversed(preorden(x)))
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.arboles_binarios import Arbol, H, N, arbolArbitrario
from src.recorrido_de_arboles_binarios import postorden, preorden

A = TypeVar("A")

def espejo(a: Arbol[A]) -> Arbol[A]:
    match a:
        case H(x):
            return H(x)
        case N(x, i, d):
            return N(x, espejo(d), espejo(i))
    assert False

# Comprobación de las propiedades
# ===============================

# Las propiedades son
@given(st.integers(min_value=1, max_value=10))
def test_espejo(n: int) -> None:
    x = arbolArbitrario(n)
    assert espejo(espejo(x)) == x
    assert list(reversed(preorden(espejo(x)))) == postorden(x)
    assert postorden(espejo(x)) == list(reversed(preorden(x)))

# La comprobación es
#    src> poetry run pytest -q imagen_especular_de_un_arbol_binario.py
#    1 passed in 0.16s
