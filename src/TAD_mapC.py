# TAD_mapC.py
# TAD de los conjuntos: Aplicación de una función a los elementos de
#   un conjunto.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    mapC : (Callable[[A], B], Conj[A]) -> Conj[B]
# tal que map(f, c) es el conjunto formado por las imágenes de los
# elementos de c, mediante f. Por ejemplo,
#    >>> mapC(lambda x: 2 * x, inserta(3, inserta(1, vacio())))
#    {2, 6}
# ---------------------------------------------------------------------

from __future__ import annotations

from abc import abstractmethod
from copy import deepcopy
from typing import Callable, Protocol, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)
from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista,
                                                       listaAconjunto)


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)
B = TypeVar('B', bound=Comparable)

# 1ª solución
# ===========

def mapC(f: Callable[[A], B], c: Conj[A]) -> Conj[B]:
    if esVacio(c):
        return vacio()
    mc = menor(c)
    rc = elimina(mc, c)
    return inserta(f(mc), mapC(f, rc))

# 2ª solución
# ===========

def mapC2(f: Callable[[A], B], c: Conj[A]) -> Conj[B]:
    return listaAconjunto(list(map(f, conjuntoAlista(c))))

# Las funciones conjuntoAlista y listaAconjunto está definida en el
# ejercicio Transformaciones entre conjuntos y listas" que se encuentra
# en https://bit.ly/3RexzxH

# 3ª solución
# ===========

def mapC3Aux(f: Callable[[A], B], c: Conj[A]) -> Conj[B]:
    r: Conj[B] = vacio()
    while not esVacio(c):
        mc = menor(c)
        c = elimina(mc, c)
        r = inserta(f(mc), r)
    return r

def mapC3(f: Callable[[A], B], c: Conj[A]) -> Conj[B]:
    _c = deepcopy(c)
    return mapC3Aux(f, _c)

# 4ª solución
# ===========

def mapC4Aux(f: Callable[[A], B], c: Conj[A]) -> Conj[B]:
    r: Conj[B] = Conj()
    while not c.esVacio():
        mc = c.menor()
        c.elimina(mc)
        r.inserta(f(mc))
    return r

def mapC4(f: Callable[[A], B], c: Conj[A]) -> Conj[B]:
    _c = deepcopy(c)
    return mapC4Aux(f, _c)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c=conjuntoAleatorio())
def test_mapPila(c: Conj[int]) -> None:
    r = mapC(lambda x: 2 * x, c)
    assert mapC2(lambda x: 2 * x, c) == r
    assert mapC3(lambda x: 2 * x, c) == r
    assert mapC4(lambda x: 2 * x, c) == r

# La comprobación es
#    src> poetry run pytest -q TAD_mapC.py
#    1 passed in 0.29s
