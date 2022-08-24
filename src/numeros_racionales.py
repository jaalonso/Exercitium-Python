# numeros_racionales.py
# Números racionales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los números racionales pueden representarse mediante pares de números
# enteros. Por ejemplo, el número 2/5 puede representarse mediante el
# par (2,5).
#
# El tipo de los racionales se define por
#    Racional = tuple[int, int]
# Definir las funciones
#    formaReducida    : (Racional) -> Racional
#    sumaRacional     : (Racional, Racional) -> Racional
#    productoRacional : (Racional, Racional) -> Racional
#    igualdadRacional : (Racional, Racional) -> bool
# tales que
# + formaReducida(x) es la forma reducida del número racional x. Por
#   ejemplo,
#      formaReducida((4, 10))  ==  (2, 5)
#      formaReducida((0, 5))   ==  (0, 1)
# + sumaRacional(x, y) es la suma de los números racionales x e y,
#   expresada en forma reducida. Por ejemplo,
#      sumaRacional((2, 3), (5, 6))  ==  (3, 2)
#      sumaRacional((3, 5), (-3, 5)) ==  (0, 1)
# + productoRacional(x, y) es el producto de los números racionales x e
#   y, expresada en forma reducida. Por ejemplo,
#      productoRacional((2, 3), (5, 6))  ==  (5, 9)
# + igualdadRacional(x, y) se verifica si los números racionales x e y
#   son iguales. Por ejemplo,
#      igualdadRacional((6, 9), (10, 15))  ==  True
#      igualdadRacional((6, 9), (11, 15))  ==  False
#      igualdadRacional((0, 2), (0, -5))   ==  True
#
# Comprobar con Hypothesis la propiedad distributiva del producto
# racional respecto de la suma.
# ---------------------------------------------------------------------

from math import gcd
from hypothesis import given, assume, strategies as st

Racional = tuple[int, int]

def formaReducida(x: Racional) -> Racional:
    (a, b) = x
    if a == 0:
        return (0, 1)
    c = gcd(a, b)
    return (a % c, b % c)

def sumaRacional(x: Racional,
                 y: Racional) -> Racional:
    (a, b) = x
    (c, d) = y
    return formaReducida((a*d+b*c, b*d))

def productoRacional(x: Racional,
                     y: Racional) -> Racional:
    (a, b) = x
    (c, d) = y
    return formaReducida((a*c, b*d))

def igualdadRacional(x: Racional,
                     y: Racional) -> bool:
    (a, b) = x
    (c, d) = y
    return a*d == b*c

# La propiedad es
@given(st.tuples(st.integers(), st.integers()),
       st.tuples(st.integers(), st.integers()),
       st.tuples(st.integers(), st.integers()))
def test_prop_distributiva(x, y, z):
    (_, x2) = x
    (_, y2) = y
    (_, z2) = z
    assume(x2 != 0 and y2 != 0 and z2 != 0)
    assert igualdadRacional(productoRacional(x, sumaRacional(y, z)),
                            sumaRacional(productoRacional(x, y),
                                         productoRacional(x, z)))

# La comprobación es
#    src> poetry run pytest -q numeros_racionales.py
#    1 passed in 0.37s
