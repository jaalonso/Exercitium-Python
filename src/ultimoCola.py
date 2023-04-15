# ultimoCola.py
# TAD de las colas: Último elemento.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    ultimoCola : (Cola[A]) -> A
# tal que ultimoCola(c) es el último elemento de la cola c. Por
# ejemplo:
#    >>> ultimoCola(inserta(3, inserta(5, inserta(2, vacia()))))
#    3
#    >>> ultimoCola(inserta(2, vacia()))
#    2
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import TypeVar

from hypothesis import assume, given

from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def ultimoCola(c: Cola[A]) -> A:
    if esVacia(c):
        raise ValueError("cola vacia")
    pc = primero(c)
    rc = resto(c)
    if esVacia(rc):
        return pc
    return ultimoCola(rc)

# 2ª solución
# ===========

def ultimoCola2Aux(c: Cola[A]) -> A:
    if c.esVacia():
        raise ValueError("cola vacia")
    pc = primero(c)
    c.resto()
    if c.esVacia():
        return pc
    return ultimoCola2(c)

def ultimoCola2(c: Cola[A]) -> A:
    _c = deepcopy(c)
    return ultimoCola2Aux(_c)

# 3ª solución
# ===========

def ultimoCola3(c: Cola[A]) -> A:
    if esVacia(c):
        raise ValueError("cola vacia")
    while not esVacia(resto(c)):
        c = resto(c)
    return primero(c)

# 4ª solución
# ===========

def ultimoCola4Aux(c: Cola[A]) -> A:
    if c.esVacia():
        raise ValueError("cola vacia")
    r = primero(c)
    while not c.esVacia():
        c.resto()
        if not c.esVacia():
            r = primero(c)
    return r

def ultimoCola4(c: Cola[A]) -> A:
    _c = deepcopy(c)
    return ultimoCola4Aux(_c)

# 5ª solución
# ===========

# Se usarán la función colaAlista del ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

def ultimoCola5(c: Cola[A]) -> A:
    if esVacia(c):
        raise ValueError("cola vacia")
    return colaAlista(c)[-1]

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c=colaAleatoria())
def test_ultimoCola(c: Cola[int]) -> None:
    assume(not esVacia(c))
    r = ultimoCola(c)
    assert ultimoCola2(c) == r
    assert ultimoCola3(c) == r
    assert ultimoCola4(c) == r
    assert ultimoCola5(c) == r

# La comprobación es
#      src> poetry run pytest -q ultimoCola.py
#      1 passed in 0.25s
