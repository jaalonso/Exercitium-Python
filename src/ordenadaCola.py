# ordenadaCola.py
# Reconocimiento de ordenación de colas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    ordenadaCola : (Cola[A]) -> bool
# tal que ordenadaCola(c) se verifica si los elementos de la cola c
# están ordenados en orden creciente. Por ejemplo,
#    >>> ordenadaCola(inserta(6, inserta(5, inserta(1, vacia()))))
#    True
#    >>> ordenadaCola(inserta(1, inserta(0, inserta(6, vacia()))))
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def ordenadaCola(c: Cola[A]) -> bool:
    if esVacia(c):
        return True
    pc = primero(c)
    rc = resto(c)
    if esVacia(rc):
        return True
    prc = primero(rc)
    return pc <= prc and ordenadaCola(rc)

# 2ª solución
# ===========

# ordenadaLista(xs, ys) se verifica si xs es una lista ordenada. Por
# ejemplo,
#    >>> ordenadaLista([2, 5, 8])
#    True
#    >>> ordenadalista([2, 8, 5])
#    False
def ordenadaLista(xs: list[A]) -> bool:
    return all((x <= y for (x, y) in zip(xs, xs[1:])))

def ordenadaCola2(p: Cola[A]) -> bool:
    return ordenadaLista(colaAlista(p))

# La función colaAlista  está definida en el ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

# 3ª solución
# ===========

def ordenadaCola3Aux(c: Cola[A]) -> bool:
    if c.esVacia():
        return True
    pc = c.primero()
    c.resto()
    if c.esVacia():
        return True
    return pc <= c.primero() and ordenadaCola3Aux(c)

def ordenadaCola3(c: Cola[A]) -> bool:
    _c = deepcopy(c)
    return ordenadaCola3Aux(_c)

# 4ª solución
# ===========

def ordenadaCola4Aux(c: Cola[A]) -> bool:
    while not c.esVacia():
        pc = c.primero()
        c.resto()
        if not c.esVacia() and pc > c.primero():
            return False
    return True

def ordenadaCola4(c: Cola[A]) -> bool:
    _c = deepcopy(c)
    return ordenadaCola4Aux(_c)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p=colaAleatoria())
def test_ordenadaCola(p: Cola[int]) -> None:
    r = ordenadaCola(p)
    assert ordenadaCola2(p) == r
    assert ordenadaCola3(p) == r
    assert ordenadaCola4(p) == r

# La comprobación es
#    src> poetry run pytest -q ordenadaCola.py
#    1 passed in 0.27s
