# numero_de_hojas_de_un_arbol_binario.py
# Número de hojas y nodos de un árbol binario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El árbol binario
#         9
#        / \
#       /   \
#      3     7
#     / \
#    2   4
# se puede representar por
#    N(9, N(3, H(2), H(4)), H(7))
#
# El tipo de los árboles binarios se puede definir por
#    @dataclass
#    class Arbol(Generic[A]):
#        pass
#
#    @dataclass
#    class H(Arbol[A]):
#        x: A
#
#    @dataclass
#    class N(Arbol[A]):
#        x: A
#        i: Arbol[A]
#        d: Arbol[A]
#
# Definir las funciones
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

from dataclasses import dataclass
from random import choice, randint
from typing import Generic, TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar("A")

@dataclass
class Arbol(Generic[A]):
    pass

@dataclass
class H(Arbol[A]):
    x: A

@dataclass
class N(Arbol[A]):
    x: A
    i: Arbol[A]
    d: Arbol[A]

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

# (arbolArbitrario n) es un árbol aleatorio de orden n. Por ejemplo,
#    >>> arbolArbitrario(4)
#    N(x=2, i=H(x=1), d=H(x=9))
#    >>> arbolArbitrario(4)
#    H(x=10)
#    >>> arbolArbitrario(4)
#    N(x=4, i=N(x=7, i=H(x=4), d=H(x=0)), d=H(x=6))
def arbolArbitrario(n: int) -> Arbol[int]:
    if n <= 1:
        return H(randint(0, 10))
    m = n // 2
    return choice([H(randint(0, 10)),
                   N(randint(0, 10),
                     arbolArbitrario(m),
                     arbolArbitrario(m))])

# La propiedad es
@given(st.integers(min_value=1, max_value=10))
def test_nHojas(n: int) -> None:
    a = arbolArbitrario(n)
    assert nHojas(a) == nNodos(a) + 1

# La comprobación es
#    src> poetry run pytest -q numero_de_hojas_de_un_arbol_binario.py
#    1 passed in 0.10s
