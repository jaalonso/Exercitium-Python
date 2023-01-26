# intercalaColas.py
# TAD de las colas: Intercalado de dos colas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    intercalaColas : (Cola[A], Cola[A]) -> Cola[A]
# tal que (intercalaColas c1 c2) es la cola formada por los elementos de
# c1 y c2 colocados en una cola, de forma alternativa, empezando por
# los elementos de c1. Por ejemplo,
#    >>> ej1 = inserta(3, inserta(5, vacia()))
#    >>> ej2 = inserta(0, inserta(7, inserta(4, inserta(9, vacia()))))
#    >>> print(intercalaColas(ej1, ej2))
#    5 | 9 | 3 | 4 | 7 | 0
#    >>> print(intercalaColas(ej2, ej1))
#    9 | 5 | 4 | 3 | 7 | 0
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.extiendeCola import extiendeCola
from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista, listaAcola

A = TypeVar('A')

# 1ª solución
# ===========

def intercalaColas(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    if esVacia(c1):
        return c2
    if esVacia(c2):
        return c1
    pc1 = primero(c1)
    rc1 = resto(c1)
    pc2 = primero(c2)
    rc2 = resto(c2)
    return extiendeCola(inserta(pc2, inserta(pc1, vacia())),
                        intercalaColas(rc1, rc2))

# La función extiendeCola está definida en el ejercicio
# "TAD de las colas: Extensión de colas" que se encuentra en
# https://bit.ly/3XIJJ4m

# 2ª solución
# ===========

def intercalaColas2(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    def aux(d1: Cola[A], d2: Cola[A], d3: Cola[A]) -> Cola[A]:
        if esVacia(d1):
            return extiendeCola(d3, d2)
        if esVacia(d2):
            return extiendeCola(d3, d1)
        pd1 = primero(d1)
        rd1 = resto(d1)
        pd2 = primero(d2)
        rd2 = resto(d2)
        return aux(rd1, rd2, inserta(pd2, inserta(pd1, d3)))

    return aux(c1, c2, vacia())

# 3ª solución
# ===========

# intercalaListas(xs, ys) es la lista obtenida intercalando los
# elementos de xs e ys. Por ejemplo,
def intercalaListas(xs: list[A], ys: list[A]) -> list[A]:
    if not xs:
        return ys
    if not ys:
        return xs
    return [xs[0], ys[0]] + intercalaListas(xs[1:], ys[1:])

def intercalaColas3(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    return listaAcola(intercalaListas(colaAlista(c1), colaAlista(c2)))

# 4ª solución
# ===========

def intercalaColas4Aux(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    if c1.esVacia():
        return c2
    if c2.esVacia():
        return c1
    pc1 = c1.primero()
    c1.resto()
    pc2 = c2.primero()
    c2.resto()
    return extiendeCola(inserta(pc2, inserta(pc1, vacia())),
                        intercalaColas4Aux(c1, c2))

def intercalaColas4(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    _c1 = deepcopy(c1)
    _c2 = deepcopy(c2)
    return intercalaColas4Aux(_c1, _c2)

# 5ª solución
# ===========

def intercalaColas5Aux(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    r: Cola[A] = vacia()
    while not esVacia(c1) and not esVacia(c2):
        pc1 = primero(c1)
        c1.resto()
        pc2 = primero(c2)
        c2.resto()
        r = inserta(pc2, inserta(pc1, r))
    if esVacia(c1):
        return extiendeCola(r, c2)
    return extiendeCola(r, c1)

def intercalaColas5(c1: Cola[A], c2: Cola[A]) -> Cola[A]:
    _c1 = deepcopy(c1)
    _c2 = deepcopy(c2)
    return intercalaColas5Aux(_c1, _c2)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=colaAleatoria(), c2=colaAleatoria())
def test_extiendeCola(c1: Cola[int], c2: Cola[int]) -> None:
    r = intercalaColas(c1, c2)
    assert intercalaColas2(c1, c2) == r
    assert intercalaColas3(c1, c2) == r
    assert intercalaColas4(c1, c2) == r
    assert intercalaColas5(c1, c2) == r

# La comprobación es
#    src> poetry run pytest -q intercalaColas.py
#    1 passed in 0.47s
