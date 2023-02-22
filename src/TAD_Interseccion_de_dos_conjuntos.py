# TAD_Interseccion_de_dos_conjuntos.py
# TAD de los conjuntos: Intersección de dos conjuntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los conjuntos](https://bit.ly/3HbB7fo)
# definir la función
#    interseccion : (Conj[A], Conj[A]) -> Conj[A]
# tal que interseccion(c1, c2) es la intersección de los conjuntos c1 y
# c2. Por ejemplo,
#    >>> ej1 = inserta(3, inserta(5, inserta(2, vacio())))
#    >>> ej2 = inserta(2, inserta(4, inserta(3, vacio())))
#    >>> interseccion(ej1, ej2)
#    {2, 3}
# ---------------------------------------------------------------------

from __future__ import annotations

from abc import abstractmethod
from copy import deepcopy
from typing import Protocol, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, pertenece, vacio)
from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista,
                                                       listaAconjunto)


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)

# 1ª solución
# ===========

def interseccion(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    if esVacio(c1):
        return vacio()
    mc1 = menor(c1)
    rc1 = elimina(mc1, c1)
    if pertenece(mc1, c2):
        return inserta(mc1, interseccion(rc1, c2))
    return interseccion(rc1, c2)

# 2ª solución
# ===========

def interseccion2(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    return listaAconjunto([x for x in conjuntoAlista(c1)
                           if pertenece(x, c2)])
#
# Las funciones conjuntoAlista y listaAconjunto está definida en el
# ejercicio Transformaciones entre conjuntos y listas" que se encuentra
# en https://bit.ly/3RexzxH

# 3ª solución
# ===========

def interseccion3(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    r: Conj[A] = vacio()
    while not esVacio(c1):
        mc1 = menor(c1)
        c1 = elimina(mc1, c1)
        if pertenece(mc1, c2):
            r = inserta(mc1, r)
    return r

# 4ª solución
# ===========

def interseccion4Aux(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    r: Conj[A] = vacio()
    while not c1.esVacio():
        mc1 = c1.menor()
        c1.elimina(mc1)
        if c2.pertenece(mc1):
            r.inserta(mc1)
    return r

def interseccion4(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    _c1 = deepcopy(c1)
    return interseccion4Aux(_c1, c2)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=conjuntoAleatorio(), c2=conjuntoAleatorio())
def test_interseccion(c1: Conj[int], c2: Conj[int]) -> None:
    r = interseccion(c1, c2)
    assert interseccion2(c1, c2) == r
    assert interseccion3(c1, c2) == r
    assert interseccion4(c1, c2) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q TAD_Interseccion_de_dos_conjuntos.py
#    1 passed in 0.30s
