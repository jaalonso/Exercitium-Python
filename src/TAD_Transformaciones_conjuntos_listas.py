# TAD_Transformaciones_conjuntos_listas.py
# TAD de los conjuntos: Transformaciones entre conjuntos y listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los conjuntos](https://bit.ly/3HbB7fo)
# definir las funciones
#    listaAconjunto : (list[A]) -> Conj[A]
#    conjuntoAlista : (Conj[A]) -> list[A]
# tales que
# + listaAconjunto(xs) es el conjunto formado por los elementos de xs.
#   Por ejemplo,
#      >>> listaAconjunto([3, 2, 5])
#      {2, 3, 5}
# + conjuntoAlista(c) es la lista formada por los elementos del
#   conjunto c. Por ejemplo,
#      >>> conjuntoAlista(inserta(5, inserta(2, inserta(3, vacio()))))
#      [2, 3, 5]
#
# Comprobar con Hypothesis que ambas funciones son inversa; es decir,
#    conjuntoAlista (listaAconjunto xs) = sorted(list(set(xs)))
#    listaAconjunto (conjuntoAlista c)  = c
# ---------------------------------------------------------------------

from __future__ import annotations

from abc import abstractmethod
from copy import deepcopy
from functools import reduce
from typing import Protocol, TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)

# 1ª definición de listaAconjunto
# ===============================

def listaAconjunto(xs: list[A]) -> Conj[A]:
    if not xs:
        return vacio()
    return inserta(xs[0], listaAconjunto(xs[1:]))

# 2ª definición de listaAconjunto
# ===============================

def listaAconjunto2(xs: list[A]) -> Conj[A]:
    return reduce(lambda ys, y: inserta(y, ys), xs, vacio())

# 3ª solución de listaAconjunto
# =============================

def listaAconjunto3(xs: list[A]) -> Conj[A]:
    c: Conj[A] = Conj()
    for x in xs:
        c.inserta(x)
    return c

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers()))
def test_listaAconjunto(xs: list[int]) -> None:
    r = listaAconjunto(xs)
    assert listaAconjunto2(xs) == r
    assert listaAconjunto3(xs) == r

# 1ª definición de conjuntoAlista
# ===============================

def conjuntoAlista(c: Conj[A]) -> list[A]:
    if esVacio(c):
        return []
    mc = menor(c)
    rc = elimina(mc, c)
    return [mc] + conjuntoAlista(rc)

# 2ª definición de conjuntoAlista
# ===============================

def conjuntoAlista2Aux(c: Conj[A]) -> list[A]:
    if c.esVacio():
        return []
    mc = c.menor()
    c.elimina(mc)
    return [mc] + conjuntoAlista2Aux(c)

def conjuntoAlista2(c: Conj[A]) -> list[A]:
    c1 = deepcopy(c)
    return conjuntoAlista2Aux(c1)

# 3ª definición de conjuntoAlista
# ===============================

def conjuntoAlista3Aux(c: Conj[A]) -> list[A]:
    r = []
    while not c.esVacio():
        mc = c.menor()
        r.append(mc)
        c.elimina(mc)
    return r

def conjuntoAlista3(c: Conj[A]) -> list[A]:
    c1 = deepcopy(c)
    return conjuntoAlista3Aux(c1)

# Comprobación de equivalencia de las definiciones de conjuntoAlista
# ==============================================================

@given(c=conjuntoAleatorio())
def test_conjuntoAlista(c: Conj[int]) -> None:
    r = conjuntoAlista(c)
    assert conjuntoAlista2(c) == r
    assert conjuntoAlista3(c) == r

# Comprobación de las propiedades
# ===============================

# La primera propiedad es
@given(st.lists(st.integers()))
def test_1_listaAconjunto(xs: list[int]) -> None:
    assert conjuntoAlista(listaAconjunto(xs)) == sorted(list(set(xs)))

# La segunda propiedad es
@given(c=conjuntoAleatorio())
def test_2_listaAconjunto(c: Conj[int]) -> None:
    assert listaAconjunto(conjuntoAlista(c)) == c

# La comprobación de las propiedades es
#    > poetry run pytest -v TAD_Transformaciones_conjuntos_listas.py
#       test_listaAconjunto PASSED
#       test_conjuntoAlista PASSED
#       test_1_listaAconjunto PASSED
#       test_2_listaAconjunto PASSED
