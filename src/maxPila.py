# maxPila.py
# Máximo elemento de una pila.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las pilas](https://bit.ly/3GTToyK),
# definir la función
#    maxPila : (Pila[A]) -> A
# tal que maxPila(p) sea el mayor de los elementos de la pila p. Por
# ejemplo,
#    >>> maxPila(apila(3, apila(5, apila(1, vacia()))))
#    5
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import TypeVar

from hypothesis import assume, given

from src.TAD.pila import (Pila, apila, cima, desapila, esVacia, pilaAleatoria,
                          vacia)
from src.transformaciones_pilas_listas import pilaAlista

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def maxPila1(p: Pila[A]) -> A:
    cp = cima(p)
    dp = desapila(p)
    if esVacia(dp):
        return cp
    return max(cp, maxPila1(dp))

# 2ª solución
# ===========

# Se usará la función pilaAlista del ejercicio
# "Transformaciones entre pilas y listas" que se encuentra en
# https://bit.ly/3ZHewQ8

def maxPila2(p: Pila[A]) -> A:
    return max(pilaAlista(p))

# 3ª solución
# ===========

def maxPila3Aux(p: Pila[A]) -> A:
    cp = p.cima()
    p.desapila()
    if esVacia(p):
        return cp
    return max(cp, maxPila3Aux(p))

def maxPila3(p: Pila[A]) -> A:
    q = deepcopy(p)
    return maxPila3Aux(q)

# 4ª solución
# ===========

def maxPila4Aux(p: Pila[A]) -> A:
    r = p.cima()
    while not esVacia(p):
        cp = p.cima()
        if cp > r:
            r = cp
        p.desapila()
    return r

def maxPila4(p: Pila[A]) -> A:
    q = deepcopy(p)
    return maxPila4Aux(q)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p=pilaAleatoria())
def test_maxPila(p: Pila[int]) -> None:
    assume(not esVacia(p))
    r = maxPila1(p)
    assert maxPila2(p) == r
    assert maxPila3(p) == r
    assert maxPila4(p) == r

# La comprobación es
#    src> poetry run pytest -q maxPila.py
#    1 passed in 0.25s
