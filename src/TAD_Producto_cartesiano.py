# TAD_Producto_cartesiano.py
# TAD de los conjuntos: TAD_Producto_cartesiano.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 27-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    productoC : (A, Conj[B]) -> Any
# tal que (productoC c1 c2) es el producto cartesiano de los
# conjuntos c1 y c2. Por ejemplo,
#    >>> ej1 = inserta(2, inserta(5, vacio()))
#    >>> ej2 = inserta(9, inserta(4, inserta(3, vacio())))
#    >>> productoC(ej1, ej2)
#    {(2, 3), (2, 4), (2, 9), (5, 3), (5, 4), (5, 9)}
# ---------------------------------------------------------------------

from __future__ import annotations

from abc import abstractmethod
from copy import deepcopy
from functools import reduce
from typing import Protocol, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)
from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista,
                                                       listaAconjunto)
from src.TAD_Union_de_dos_conjuntos import union


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)
B = TypeVar('B', bound=Comparable)

# 1ª solución
# ===========

# (agrega x c) es el conjunto de los pares de x con los elementos de
# c. Por ejemplo,
#    >>> agrega(2, inserta(9, inserta(4, inserta(3, vacio()))))
#    {(2, 3), (2, 4), (2, 9)}
def agrega(x: A, c: Conj[B]) -> Conj[tuple[A, B]]:
    if esVacio(c):
        return vacio()
    mc = menor(c)
    rc = elimina(mc, c)
    return inserta((x, mc), agrega(x, rc))

def productoC(c1: Conj[A], c2: Conj[B]) -> Conj[tuple[A, B]]:
    if esVacio(c1):
        return vacio()
    mc1 = menor(c1)
    rc1 = elimina(mc1, c1)
    return union(agrega(mc1, c2), productoC(rc1, c2))

# La función union está definida en el ejercicio
# "Unión de dos conjuntos" que se encuentra en
# https://bit.ly/3Y1jBl8

# 2ª solución
# ===========

def productoC2(c1: Conj[A], c2: Conj[B]) -> Conj[tuple[A, B]]:
    xs = conjuntoAlista(c1)
    ys = conjuntoAlista(c2)
    return reduce(lambda bs, a: inserta(a, bs), [(x,y) for x in xs for y in ys], vacio())

# 3ª solución
# ===========

def productoC3(c1: Conj[A], c2: Conj[B]) -> Conj[tuple[A, B]]:
    xs = conjuntoAlista(c1)
    ys = conjuntoAlista(c2)
    return listaAconjunto([(x,y) for x in xs for y in ys])

# 4ª solución
# ===========

def agrega4Aux(x: A, c: Conj[B]) -> Conj[tuple[A, B]]:
    r: Conj[tuple[A, B]] = vacio()
    while not esVacio(c):
        mc = menor(c)
        c = elimina(mc, c)
        r = inserta((x, mc), r)
    return r

def agrega4(x: A, c: Conj[B]) -> Conj[tuple[A, B]]:
    _c = deepcopy(c)
    return agrega4Aux(x, _c)

def productoC4(c1: Conj[A], c2: Conj[B]) -> Conj[tuple[A, B]]:
    r: Conj[tuple[A, B]] = vacio()
    while not esVacio(c1):
        mc1 = menor(c1)
        c1 = elimina(mc1, c1)
        r = union(agrega4(mc1, c2), r)
    return r

# 5ª solución
# ===========

def agrega5Aux(x: A, c: Conj[B]) -> Conj[tuple[A, B]]:
    r: Conj[tuple[A, B]] = Conj()
    while not c.esVacio():
        mc = c.menor()
        c.elimina(mc)
        r.inserta((x, mc))
    return r

def agrega5(x: A, c: Conj[B]) -> Conj[tuple[A, B]]:
    _c = deepcopy(c)
    return agrega5Aux(x, _c)

def productoC5(c1: Conj[A], c2: Conj[B]) -> Conj[tuple[A, B]]:
    r: Conj[tuple[A, B]] = Conj()
    while not c1.esVacio():
        mc1 = c1.menor()
        c1.elimina(mc1)
        r = union(agrega5(mc1, c2), r)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=conjuntoAleatorio(), c2=conjuntoAleatorio())
def test_productoC(c1: Conj[int], c2: Conj[int]) -> None:
    r = productoC(c1, c2)
    assert productoC2(c1, c2) == r
    assert productoC3(c1, c2) == r
    assert productoC4(c1, c2) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q TAD_Producto_cartesiano.py
#    1 passed in 0.35s
