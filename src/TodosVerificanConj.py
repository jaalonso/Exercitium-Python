# TodosVerificanConj.py
# TAD de los conjuntos: Todos los elementos verifican una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    todos : (Callable[[A], bool], Conj[A]) -> bool
# tal que todos(p, c) se verifica si todos los elemsntos de c
# verifican el predicado p.  Por ejemplo,
#    >>> todos(lambda x: x % 2 == 0, inserta(4, inserta(6, vacio())))
#    True
#    >>> todos(lambda x: x % 2 == 0, inserta(4, inserta(7, vacio())))
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import Callable, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)
from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista)

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def todos(p: Callable[[A], bool], c: Conj[A]) -> bool:
    if esVacio(c):
        return True
    mc = menor(c)
    rc = elimina(mc, c)
    return p(mc) and todos(p, rc)

# 2ª solución
# ===========

def todos2(p: Callable[[A], bool], c: Conj[A]) -> bool:
    return all(p(x) for x in conjuntoAlista(c))

# La función conjuntoAlista está definida en el ejercicio
# "Transformaciones entre conjuntos y listas" que se encuentra
# en https://bit.ly/3RexzxH

# 3ª solución
# ===========

def todos3Aux(p: Callable[[A], bool], c: Conj[A]) -> bool:
    while not esVacio(c):
        mc = menor(c)
        c = elimina(mc, c)
        if not p(mc):
            return False
    return True

def todos3(p: Callable[[A], bool], c: Conj[A]) -> bool:
    _c = deepcopy(c)
    return todos3Aux(p, _c)

# 4ª solución
# ===========

def todos4Aux(p: Callable[[A], bool], c: Conj[A]) -> bool:
    while not c.esVacio():
        mc = c.menor()
        c.elimina(mc)
        if not p(mc):
            return False
    return True

def todos4(p: Callable[[A], bool], c: Conj[A]) -> bool:
    _c = deepcopy(c)
    return todos4Aux(p, _c)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c=conjuntoAleatorio())
def test_todos(c: Conj[int]) -> None:
    r = todos(lambda x: x % 2 == 0, c)
    assert todos2(lambda x: x % 2 == 0, c) == r
    assert todos3(lambda x: x % 2 == 0, c) == r
    assert todos4(lambda x: x % 2 == 0, c) == r

# La comprobación es
#    src> poetry run pytest -q TodosVerificanConj.py
#    1 passed in 0.28s
