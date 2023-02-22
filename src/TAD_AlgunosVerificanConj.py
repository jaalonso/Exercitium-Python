# TAD_AlgunosVerificanConj.py
# TAD de los conjuntos: Algunos elementos verifican una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    algunos : algunos(Callable[[A], bool], Conj[A]) -> bool
# tal que algunos(p, c) se verifica si algún elemento de c verifica el
# predicado p. Por ejemplo,
#    >>> algunos(lambda x: x % 2 == 0, inserta(4, inserta(7, vacio())))
#    True
#    >>> algunos(lambda x: x % 2 == 0, inserta(3, inserta(7, vacio())))
#    False
# ---------------------------------------------------------------------

from __future__ import annotations

from abc import abstractmethod
from copy import deepcopy
from typing import Callable, Protocol, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)
from src.TAD_Transformaciones_conjuntos_listas import conjuntoAlista


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)

# 1ª solución
# ===========

def algunos(p: Callable[[A], bool], c: Conj[A]) -> bool:
    if esVacio(c):
        return False
    mc = menor(c)
    rc = elimina(mc, c)
    return p(mc) or algunos(p, rc)

# 2ª solución
# ===========

def algunos2(p: Callable[[A], bool], c: Conj[A]) -> bool:
    return any(p(x) for x in conjuntoAlista(c))

# La función conjuntoAlista está definida en el ejercicio
# "Transformaciones entre conjuntos y listas" que se encuentra
# en https://bit.ly/3RexzxH

# 3ª solución
# ===========

def algunos3Aux(p: Callable[[A], bool], c: Conj[A]) -> bool:
    while not esVacio(c):
        mc = menor(c)
        c = elimina(mc, c)
        if p(mc):
            return True
    return False

def algunos3(p: Callable[[A], bool], c: Conj[A]) -> bool:
    _c = deepcopy(c)
    return algunos3Aux(p, _c)

# 4ª solución
# ===========

def algunos4Aux(p: Callable[[A], bool], c: Conj[A]) -> bool:
    while not c.esVacio():
        mc = c.menor()
        c.elimina(mc)
        if p(mc):
            return True
    return False

def algunos4(p: Callable[[A], bool], c: Conj[A]) -> bool:
    _c = deepcopy(c)
    return algunos4Aux(p, _c)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c=conjuntoAleatorio())
def test_algunos(c: Conj[int]) -> None:
    r = algunos(lambda x: x % 2 == 0, c)
    assert algunos2(lambda x: x % 2 == 0, c) == r
    assert algunos3(lambda x: x % 2 == 0, c) == r
    assert algunos4(lambda x: x % 2 == 0, c) == r

# La comprobación es
#    src> poetry run pytest -q TAD_AlgunosVerificanConj.py
#    1 passed in 0.28s
