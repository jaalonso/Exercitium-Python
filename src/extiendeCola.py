# extiendeCola.py
# TAD de las colas: Extensión de colas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    extiendeCola : (Cola[A], Cola[A]) -> Cola[A]
# tal que extiendeCola(c1, c2) es la cola que resulta de poner los
# elementos de la cola c2 a continuación de los de la cola de c1. Por
# ejemplo,
#    >>> ej1 = inserta(3, inserta(2, vacia()))
#    >>> ej2 = inserta(5, inserta(3, inserta(4, vacia())))
#    >>> ej1
#    2 | 3
#    >>> ej2
#    4 | 3 | 5
#    >>> extiendeCola(ej1, ej2)
#    2 | 3 | 4 | 3 | 5
#    >>> extiendeCola(ej2, ej1)
#    4 | 3 | 5 | 2 | 3
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista, listaAcola

A = TypeVar('A')

# 1ª solución
# ===========

def extiendeCola(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    if esVacia(c2):
        return c1
    pc2 = primero(c2)
    rc2 = resto(c2)
    return extiendeCola(inserta(pc2, c1), rc2)

# 2ª solución
# ===========

def extiendeCola2(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    return listaAcola(colaAlista(c1) + colaAlista(c2))

# Las funciones colaAlista y listaAcola están definidas en el ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

# 3ª solución
# ===========

def extiendeCola3Aux(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    if c2.esVacia():
        return c1
    pc2 = c2.primero()
    c2.resto()
    return extiendeCola(inserta(pc2, c1), c2)

def extiendeCola3(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    _c2 = deepcopy(c2)
    return extiendeCola3Aux(c1, _c2)

# 4ª solución
# ===========

def extiendeCola4Aux(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    r = c1
    while not esVacia(c2):
        r = inserta(primero(c2), r)
        c2 = resto(c2)
    return r

def extiendeCola4(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    _c2 = deepcopy(c2)
    return extiendeCola4Aux(c1, _c2)

# 5ª solución
# ===========

def extiendeCola5Aux(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    r = c1
    while not c2.esVacia():
        r.inserta(primero(c2))
        c2.resto()
    return r

def extiendeCola5(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    _c1 = deepcopy(c1)
    _c2 = deepcopy(c2)
    return extiendeCola5Aux(_c1, _c2)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=colaAleatoria(), c2=colaAleatoria())
def test_extiendeCola(c1: Cola[int], c2: Cola[int]) -> None:
    r = extiendeCola(c1, c2)
    assert extiendeCola2(c1, c2) == r
    assert extiendeCola3(c1, c2) == r
    assert extiendeCola4(c1, c2) == r

# La comprobación es
#    src> poetry run pytest -q extiendeCola.py
#    1 passed in 0.32s
