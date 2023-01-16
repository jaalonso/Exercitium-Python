# subPila.py
# Reconocimiento de subpilas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 31-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo de dato de las pilas](https://bit.ly/3GTToyK)
# (cuyo código se encuentra en [PilaConListas.hs](https://bit.ly/3vL41xD))
# definir la función
#    subPila : (Pila[A], Pila[A]) -> bool
# tal que subPila(p1, p2) se verifica si p1 es una subpila de p2. Por
# ejemplo,
#    >>> ej1 = apila(2, apila(3, vacia()))
#    >>> ej2 = apila(7, apila(2, apila(3, apila(5, vacia()))))
#    >>> ej3 = apila(2, apila(7, apila(3, apila(5, vacia()))))
#    >>> subPila(ej1, ej2)
#    True
#    >>> subPila(ej1, ej3)
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.pilaConListas import (Pila, apila, cima, desapila, esVacia,
                                   pilaAleatoria, vacia)
from src.transformaciones_pilas_listas import pilaAlista
from src.prefijoPila import prefijoPila

A = TypeVar('A')

# 1ª solución
# ===========

# Se usará la función PrefijoPila del ejercicio
# "Reconocimiento de prefijos de pilas" que se encuentra en
# https://bit.ly/3Xqu7lo

def subPila1(p1: Pila[A], p2: Pila[A]) -> bool:
    if esVacia(p1):
        return True
    if esVacia(p2):
        return False
    cp1 = cima(p1)
    dp1 = desapila(p1)
    cp2 = cima(p2)
    dp2 = desapila(p2)
    if cp1 == cp2:
        return prefijoPila(dp1, dp2) or subPila1(p1, dp2)
    return subPila1(p1, dp2)

# 2ª solución
# ===========

# Se usará la función pilaAlista del ejercicio
# "Transformaciones entre pilas y listas" que se encuentra en
# https://bit.ly/3ZHewQ8

# sublista(xs, ys) se verifica si xs es una sublista de ys. Por
# ejemplo,
#    >>> sublista([3,2], [5,3,2,7])
#    True
#    >>> sublista([3,2], [5,3,7,2])
#    False
def sublista(xs: list[A], ys: list[A]) -> bool:
    return any(xs == ys[i:i+len(xs)] for i in range(len(ys) - len(xs) + 1))

def subPila2(p1: Pila[A], p2: Pila[A]) -> bool:
    return sublista(pilaAlista(p1), pilaAlista(p2))

# 3ª solución
# ===========

def subPila3Aux(p1: Pila[A], p2: Pila[A]) -> bool:
    if p1.esVacia():
        return True
    if p2.esVacia():
        return False
    if p1.cima() != p2.cima():
        p2.desapila()
        return subPila3Aux(p1, p2)
    q1 = deepcopy(p1)
    p1.desapila()
    p2.desapila()
    return prefijoPila(p1, p2) or subPila3Aux(q1, p2)

def subPila3(p1: Pila[A], p2: Pila[A]) -> bool:
    q1 = deepcopy(p1)
    q2 = deepcopy(p2)
    return subPila3Aux(q1, q2)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p1=pilaAleatoria(), p2=pilaAleatoria())
def test_subPila(p1: Pila[int], p2: Pila[int]) -> None:
    r = subPila1(p1, p2)
    assert subPila2(p1, p2) == r
    assert subPila3(p1, p2) == r

# La comprobación es
#    src> poetry run pytest -q subPila.py
#    1 passed in 0.32s
