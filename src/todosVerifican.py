# todosVerifican.py
# TAD de las colas: Todos los elementos verifican una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    todosVerifican : (Callable[[A], bool], Cola[A]) -> bool
# tal que todosVerifican(p, c) se verifica si todos los elementos de la
# cola c cumplen la propiedad p. Por ejemplo,
#    >>> todosVerifican(lambda x: x > 0, inserta(3, inserta(2, vacia())))
#    True
#    >>> todosVerifican(lambda x: x > 0, inserta(3, inserta(-2, vacia())))
#    False
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import Callable, TypeVar

from hypothesis import given

from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def todosVerifican1(p: Callable[[A], bool], c: Cola[A]) -> bool:
    if esVacia(c):
        return True
    pc = primero(c)
    rc = resto(c)
    return p(pc) and todosVerifican1(p, rc)

# 2ª solución
# ===========

def todosVerifican2(p: Callable[[A], bool], c: Cola[A]) -> bool:
    return all(p(x) for x in colaAlista(c))

# La función colaAlista está definida en el ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

# 3ª solución
# ===========

def todosVerifican3Aux(p: Callable[[A], bool], c: Cola[A]) -> bool:
    if c.esVacia():
        return True
    pc = c.primero()
    c.resto()
    return p(pc) and todosVerifican3Aux(p, c)

def todosVerifican3(p: Callable[[A], bool], c: Cola[A]) -> bool:
    _c = deepcopy(c)
    return todosVerifican3Aux(p, _c)

# 4ª solución
# ===========

def todosVerifican4Aux(p: Callable[[A], bool], c: Cola[A]) -> bool:
    if c.esVacia():
        return True
    pc = c.primero()
    c.resto()
    return p(pc) and todosVerifican4Aux(p, c)

def todosVerifican4(p: Callable[[A], bool], c: Cola[A]) -> bool:
    _c = deepcopy(c)
    return todosVerifican4Aux(p, _c)

# 5ª solución
# ===========

def todosVerifican5Aux(p: Callable[[A], bool], c: Cola[A]) -> bool:
    while not c.esVacia():
        if not p(c.primero()):
            return False
        c.resto()
    return True

def todosVerifican5(p: Callable[[A], bool], c: Cola[A]) -> bool:
    _c = deepcopy(c)
    return todosVerifican5Aux(p, _c)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c=colaAleatoria())
def test_filtraPila(c: Cola[int]) -> None:
    r = todosVerifican1(lambda x: x > 0, c)
    assert todosVerifican2(lambda x: x > 0, c) == r
    assert todosVerifican3(lambda x: x > 0, c) == r
    assert todosVerifican4(lambda x: x > 0, c) == r
    assert todosVerifican5(lambda x: x > 0, c) == r

# La comprobación es
#    src> poetry run pytest -q todosVerifican.py
#    1 passed in 0.25s
