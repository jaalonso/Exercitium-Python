# prefijoCola.py
# Reconocimiento de prefijos de colas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    prefijoCola : (Cola[A], Cola[A]) -> bool
# tal que prefijoCola(c1, c2) se verifica si la cola c1 es justamente
# un prefijo de la cola c2. Por ejemplo,
#    >>> ej1 = inserta(4, inserta(2, vacia()))
#    >>> ej2 = inserta(5, inserta(4, inserta(2, vacia())))
#    >>> ej3 = inserta(5, inserta(2, inserta(4, vacia())))
#    >>> prefijoCola(ej1, ej2)
#    True
#    >>> prefijoCola(ej1, ej3)
#    False
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def prefijoCola(c1: Cola[A], c2: Cola[A]) -> bool:
    if esVacia(c1):
        return True
    if esVacia(c2):
        return False
    return primero(c1) == primero(c2) and prefijoCola(resto(c1), resto(c2))

# 2ª solución
# ===========

def esPrefijoLista(xs: list[A], ys: list[A]) -> bool:
    return ys[:len(xs)] == xs

def prefijoCola2(c1: Cola[A], c2: Cola[A]) -> bool:
    return esPrefijoLista(colaAlista(c1), colaAlista(c2))

# La función colaAlista está definida en el ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

# 3ª solución
# ===========

def prefijoCola3Aux(c1: Cola[A], c2: Cola[A]) -> bool:
    if c1.esVacia():
        return True
    if c2.esVacia():
        return False
    cc1 = c1.primero()
    c1.resto()
    cc2 = c2.primero()
    c2.resto()
    return cc1 == cc2 and prefijoCola3(c1, c2)

def prefijoCola3(c1: Cola[A], c2: Cola[A]) -> bool:
    q1 = deepcopy(c1)
    q2 = deepcopy(c2)
    return prefijoCola3Aux(q1, q2)

# 4ª solución
# ===========

def prefijoCola4Aux(c1: Cola[A], c2: Cola[A]) -> bool:
    while not c2.esVacia() and not c1.esVacia():
        if c1.primero() != c2.primero():
            return False
        c1.resto()
        c2.resto()
    return c1.esVacia()

def prefijoCola4(c1: Cola[A], c2: Cola[A]) -> bool:
    q1 = deepcopy(c1)
    q2 = deepcopy(c2)
    return prefijoCola4Aux(q1, q2)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c1=colaAleatoria(), c2=colaAleatoria())
def test_prefijoCola(c1: Cola[int], c2: Cola[int]) -> None:
    r = prefijoCola(c1, c2)
    assert prefijoCola2(c1, c2) == r
    assert prefijoCola3(c1, c2) == r
    assert prefijoCola4(c1, c2) == r

# La comprobación es
#    src> poetry run pytest -q prefijoCola.py
#    1 passed in 0.29s
