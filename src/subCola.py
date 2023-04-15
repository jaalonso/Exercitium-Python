# subCola.py
# Reconocimiento de subcolas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    subCola : (Cola[A], Cola[A]) -> bool
# tal que subCola(c1, c2) se verifica si c1 es una subcola de c2. Por
# ejemplo,
#    >>> ej1 = inserta(2, inserta(3, vacia()))
#    >>> ej2 = inserta(7, inserta(2, inserta(3, inserta(5, vacia()))))
#    >>> ej3 = inserta(2, inserta(7, inserta(3, inserta(5, vacia()))))
#    >>> subCola(ej1, ej2)
#    True
#    >>> subCola(ej1, ej3)
#    False
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.prefijoCola import prefijoCola
from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def subCola1(c1: Cola[A], c2: Cola[A]) -> bool:
    if esVacia(c1):
        return True
    if esVacia(c2):
        return False
    pc1 = primero(c1)
    rc1 = resto(c1)
    pc2 = primero(c2)
    rc2 = resto(c2)
    if pc1 == pc2:
        return prefijoCola(rc1, rc2) or subCola1(c1, rc2)
    return subCola1(c1, rc2)

# La función prefijoCola está definida en el ejercicio
# "Reconocimiento de prefijos de colas" que se encuentra en
# https://bit.ly/3HaK20x

# 2ª solución
# ===========

# sublista(xs, ys) se verifica si xs es una sublista de ys. Por
# ejemplo,
#    >>> sublista([3,2], [5,3,2,7])
#    True
#    >>> sublista([3,2], [5,3,7,2])
#    False
def sublista(xs: list[A], ys: list[A]) -> bool:
    return any(xs == ys[i:i+len(xs)] for i in range(len(ys) - len(xs) + 1))

def subCola2(c1: Cola[A], c2: Cola[A]) -> bool:
    return sublista(colaAlista(c1), colaAlista(c2))

# La función colaAlista está definida en el ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

# 3ª solución
# ===========

def subCola3Aux(c1: Cola[A], c2: Cola[A]) -> bool:
    if c1.esVacia():
        return True
    if c2.esVacia():
        return False
    if c1.primero() != c2.primero():
        c2.resto()
        return subCola3Aux(c1, c2)
    q1 = deepcopy(c1)
    c1.resto()
    c2.resto()
    return prefijoCola(c1, c2) or subCola3Aux(q1, c2)

def subCola3(c1: Cola[A], c2: Cola[A]) -> bool:
    q1 = deepcopy(c1)
    q2 = deepcopy(c2)
    return subCola3Aux(q1, q2)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c1=colaAleatoria(), c2=colaAleatoria())
def test_subCola(c1: Cola[int], c2: Cola[int]) -> None:
    r = subCola1(c1, c2)
    assert subCola2(c1, c2) == r
    assert subCola3(c1, c2) == r

# La comprobación es
#    src> poetry run pytest -q subCola.py
#    1 passed in 0.31s
