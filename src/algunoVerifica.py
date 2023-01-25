# algunoVerifica.py
# TAD de las colas: Todos los elementos verifican una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    algunoVerifica : (Callable[[A], bool], Cola[A]) -> bool
# tal que algunoVerifica(p, c) se verifica si alguno de los elementos de la
# cola c cumplen la propiedad p. Por ejemplo,
#    >>> algunoVerifica(lambda x: x > 0, inserta(-3, inserta(2, vacia())))
#    True
#    >>> algunoVerifica(lambda x: x > 0, inserta(-3, inserta(-2, vacia())))
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import Callable, TypeVar

from hypothesis import given

from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def algunoVerifica1(p: Callable[[A], bool], c: Cola[A]) -> bool:
    if esVacia(c):
        return False
    pc = primero(c)
    rc = resto(c)
    return p(pc) or algunoVerifica1(p, rc)

# 2ª solución
# ===========

def algunoVerifica2(p: Callable[[A], bool], c: Cola[A]) -> bool:
    return any(p(x) for x in colaAlista(c))

# La función colaAlista está definida en el ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

# 3ª solución
# ===========

def algunoVerifica3Aux(p: Callable[[A], bool], c: Cola[A]) -> bool:
    if c.esVacia():
        return False
    pc = c.primero()
    c.resto()
    return p(pc) or algunoVerifica3Aux(p, c)

def algunoVerifica3(p: Callable[[A], bool], c: Cola[A]) -> bool:
    _c = deepcopy(c)
    return algunoVerifica3Aux(p, _c)

# 4ª solución
# ===========

def algunoVerifica4Aux(p: Callable[[A], bool], c: Cola[A]) -> bool:
    if c.esVacia():
        return False
    pc = c.primero()
    c.resto()
    return p(pc) or algunoVerifica4Aux(p, c)

def algunoVerifica4(p: Callable[[A], bool], c: Cola[A]) -> bool:
    _c = deepcopy(c)
    return algunoVerifica4Aux(p, _c)

# 5ª solución
# ===========

def algunoVerifica5Aux(p: Callable[[A], bool], c: Cola[A]) -> bool:
    while not c.esVacia():
        if p(c.primero()):
            return True
        c.resto()
    return False

def algunoVerifica5(p: Callable[[A], bool], c: Cola[A]) -> bool:
    _c = deepcopy(c)
    return algunoVerifica5Aux(p, _c)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c=colaAleatoria())
def test_algunoVerifica(c: Cola[int]) -> None:
    r = algunoVerifica1(lambda x: x > 0, c)
    assert algunoVerifica2(lambda x: x > 0, c) == r
    assert algunoVerifica3(lambda x: x > 0, c) == r
    assert algunoVerifica4(lambda x: x > 0, c) == r
    assert algunoVerifica5(lambda x: x > 0, c) == r

# La comprobación es
#    src> poetry run pytest -q algunoVerifica.py
#    1 passed in 0.31s
