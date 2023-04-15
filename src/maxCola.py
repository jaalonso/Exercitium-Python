# maxCola.py
# Máximo elemento de una cola.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 27-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    maxCola : (Cola[A]) -> A
# tal que maxCola(c) sea el mayor de los elementos de la cola c. Por
# ejemplo,
#    >>> maxCola(inserta(3, inserta(5, inserta(1, vacia()))))
#    5
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import TypeVar

from hypothesis import assume, given

from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def maxCola1(c: Cola[A]) -> A:
    pc = primero(c)
    rc = resto(c)
    if esVacia(rc):
        return pc
    return max(pc, maxCola1(rc))

# 2ª solución
# ===========

# Se usará la función colaAlista del ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3ZHewQ8

def maxCola2(c: Cola[A]) -> A:
    return max(colaAlista(c))

# 3ª solución
# ===========

def maxCola3Aux(c: Cola[A]) -> A:
    pc = c.primero()
    c.resto()
    if esVacia(c):
        return pc
    return max(pc, maxCola3Aux(c))

def maxCola3(c: Cola[A]) -> A:
    _c = deepcopy(c)
    return maxCola3Aux(_c)

# 4ª solución
# ===========

def maxCola4Aux(c: Cola[A]) -> A:
    r = c.primero()
    while not esVacia(c):
        pc = c.primero()
        if pc > r:
            r = pc
        c.resto()
    return r

def maxCola4(c: Cola[A]) -> A:
    _c = deepcopy(c)
    return maxCola4Aux(_c)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c=colaAleatoria())
def test_maxCola(c: Cola[int]) -> None:
    assume(not esVacia(c))
    r = maxCola1(c)
    assert maxCola2(c) == r
    assert maxCola3(c) == r
    assert maxCola4(c) == r

# La comprobación es
#    src> poetry run pytest -q maxCola.py
#    1 passed in 0.30s
