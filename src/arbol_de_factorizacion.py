# arbol_de_factorizacion.py
# Árbol de factorización.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los divisores medios de un número son los que ocupan la posición
# media entre los divisores de n, ordenados de menor a mayor. Por
# ejemplo, los divisores de 60 son [1,2,3,4,5,6,10,12,15,20,30,60] y
# sus divisores medios son 6 y 10. Para los números que son cuadrados
# perfectos, sus divisores medios de son sus raíces cuadradas; por
# ejemplos, los divisores medios de 9 son 3 y 3.
#
# El árbol de factorización de un número compuesto n se construye de la
# siguiente manera:
#    * la raíz es el número n,
#    * la rama izquierda es el árbol de factorización de su divisor
#      medio menor y
#    * la rama derecha es el árbol de factorización de su divisor
#      medio mayor
# Si el número es primo, su árbol de factorización sólo tiene una hoja
# con dicho número. Por ejemplo, el árbol de factorización de 60 es
#        60
#       /  \
#      6    10
#     / \   / \
#    2   3 2   5
#
# Definir la función
#    arbolFactorizacion :: Int -> Arbol
# tal que (arbolFactorizacion n) es el árbol de factorización de n. Por
# ejemplo,
#    arbolFactorizacion(60) == N(60, N(6, H(2), H(3)), N(10, H(2), H(5)))
#    arbolFactorizacion(45) == N(45, H(5), N(9, H(3), H(3)))
#    arbolFactorizacion(7)  == H(7)
#    arbolFactorizacion(9)  == N(9, H(3), H(3))
#    arbolFactorizacion(14) == N(14, H(2), H(7))
#    arbolFactorizacion(28) == N(28, N(4, H(2), H(2)), H(7))
#    arbolFactorizacion(84) == N(84, H(7), N(12, H(3), N(4, H(2), H(2))))
# ---------------------------------------------------------------------

from dataclasses import dataclass
from math import ceil, sqrt

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

@dataclass
class Arbol:
    pass

@dataclass
class H(Arbol):
    x: int

@dataclass
class N(Arbol):
    x: int
    i: Arbol
    d: Arbol

# divisores(n) es la lista de los divisores de n. Por ejemplo,
#    divisores(30)  ==  [1,2,3,5,6,10,15,30]
def divisores(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

# divisoresMedio(n) es el par formado por los divisores medios de
# n. Por ejemplo,
#    divisoresMedio(30)  ==  (5,6)
#    divisoresMedio(7)   ==  (1,7)
#    divisoresMedio(16)  ==  (4,4)
def divisoresMedio(n: int) -> tuple[int, int]:
    xs = divisores(n)
    x = xs[len(xs) // 2]
    return (n // x, x)

# esPrimo(n) se verifica si n es primo. Por ejemplo,
#    esPrimo(7)  ==  True
#    esPrimo(9)  ==  False
def esPrimo(n: int) -> bool:
    return divisores(n) == [1, n]

def arbolFactorizacion1(n: int) -> Arbol:
    if esPrimo(n):
        return H(n)
    (x, y) = divisoresMedio(n)
    return N(n, arbolFactorizacion1(x), arbolFactorizacion1(y))

# 2ª solución
# ===========

# divisoresMedio2(n) es el par formado por los divisores medios de
# n. Por ejemplo,
#    divisoresMedio2(30) ==  (5,6)
#    divisoresMedio2(7)  ==  (1,7)
#    divisoresMedio2(16) ==  (4,4)
def divisoresMedio2(n: int) -> tuple[int, int]:
    m = ceil(sqrt(n))
    x = [y for y in range(m, n + 1) if n % y == 0][0]
    return (n // x, x)

def arbolFactorizacion2(n: int) -> Arbol:
    if esPrimo(n):
        return H(n)
    (x, y) = divisoresMedio2(n)
    return N(n, arbolFactorizacion2(x), arbolFactorizacion2(y))

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=200))
def test_arbolFactorizacion(n: int) -> None:
    assert arbolFactorizacion1(n) == arbolFactorizacion2(n)

# La comprobación es
#    src> poetry run pytest -q arbol_de_factorizacion.py
#    1 passed in 0.14s
