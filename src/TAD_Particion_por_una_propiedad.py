# TAD_Particion_por_una_propiedad.py
# TAD de los conjuntos: Partición de un conjunto según una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    particion : (Callable[[A], bool], Conj[A]) -> tuple[Conj[A], Conj[A]]
# tal que particion(c) es el par formado por dos conjuntos: el de sus
# elementos que verifican p y el de los elementos que no lo
# verifica. Por ejemplo,
#    >>> ej = inserta(5, inserta(4, inserta(7, inserta(2, vacio()))))
#    >>> particion(lambda x: x % 2 == 0, ej)
#    ({2, 4}, {5, 7})
# ---------------------------------------------------------------------

from __future__ import annotations

from abc import abstractmethod
from copy import deepcopy
from typing import Callable, Protocol, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)
from src.TAD_Subconjunto_por_propiedad import filtra


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)

# 1ª solución
# ===========

def particion(p: Callable[[A], bool],
              c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    return (filtra(p, c), filtra(lambda x: not p(x), c))

# La función filtra está definida en el ejercicio
# "Subconjunto determinado por una propiedad" que se encuentra en
# https://bit.ly/3lplFoV

# 2ª solución
# ===========

def particion2Aux(p: Callable[[A], bool],
                  c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    r: Conj[A] = vacio()
    s: Conj[A] = vacio()
    while not esVacio(c):
        mc = menor(c)
        c = elimina(mc, c)
        if p(mc):
            r = inserta(mc, r)
        else:
            s = inserta(mc, s)
    return (r, s)

def particion2(p: Callable[[A], bool],
               c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    _c = deepcopy(c)
    return particion2Aux(p, _c)

# 3ª solución
# ===========

def particion3Aux(p: Callable[[A], bool],
                  c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    r: Conj[A] = Conj()
    s: Conj[A] = Conj()
    while not c.esVacio():
        mc = c.menor()
        c.elimina(mc)
        if p(mc):
            r.inserta(mc)
        else:
            s.inserta(mc)
    return (r, s)

def particion3(p: Callable[[A], bool],
               c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    _c = deepcopy(c)
    return particion3Aux(p, _c)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c=conjuntoAleatorio())
def test_particion(c: Conj[int]) -> None:
    r = particion(lambda x: x % 2 == 0, c)
    assert particion2(lambda x: x % 2 == 0, c) == r
    assert particion3(lambda x: x % 2 == 0, c) == r

# La comprobación es
#    src> poetry run pytest -q TAD_Particion_por_una_propiedad.py
#    1 passed in 0.28s
