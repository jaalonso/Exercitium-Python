# arbol_de_profundidad_n_con_nodos_iguales.py
# Árbol de profundidad n con nodos iguales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-diciembre-2022
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
# Definir la función
#    replicateArbol : (int, A) -> Arbol[A]
# tal que (replicate n x) es el árbol de profundidad n cuyos nodos son
# x. Por ejemplo,
#    >>> replicateArbol(0, 5)
#    H(5)
#    >>> replicateArbol(1, 5)
#    N(5, H(5), H(5))
#    >>> replicateArbol(2, 5)
#    N(5, N(5, H(5), H(5)), N(5, H(5), H(5)))
#
# Comprobar con Hypothesis que el número de hojas de
# replicateArbol(n, x) es 2^n, para todo número natural n.
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

def replicateArbol(n: int, x: A) -> Arbol[A]:
    match n:
        case 0:
            return H(x)
        case n:
            t = replicateArbol(n - 1, x)
            return N(x, t, t)
    assert False

# Generador para las comprobaciones
# =================================

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

# Función auxiliar para la comprobación
# =====================================

# nHojas(x) es el número de hojas del árbol x. Por ejemplo,
#    nHojas(N(9, N(3, H(2), H(4)), H(7)))  ==  3
def nHojas(a: Arbol[A]) -> int:
    match a:
        case H(_):
            return 1
        case N(_, i, d):
            return nHojas(i) + nHojas(d)
    assert False

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=10),
       st.integers(min_value=1, max_value=10))
def test_nHojas(n: int, x: int) -> None:
    assert nHojas(replicateArbol(n, x)) == 2**n

# La comprobación es
#    src> poetry run pytest -q arbol_de_profundidad_n_con_nodos_iguales.py
#    1 passed in 0.20s
