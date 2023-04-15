# TAD_Interseccion_de_varios_conjuntos.py
# TAD de los conjuntos: Intersección de varios conjuntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    interseccionG : (list[Conj[A]]) -> Conj[A]
# tal que interseccionG(cs) es la intersección de la lista de
# conjuntos cs. Por ejemplo,
#    >>> ej1 = inserta(2, inserta(3, inserta(5, vacio())))
#    >>> ej2 = inserta(5, inserta(2, inserta(7, vacio())))
#    >>> ej3 = inserta(3, inserta(2, inserta(5, vacio())))
#    >>> interseccionG([ej1, ej2, ej3])
#    {2, 5}
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from __future__ import annotations

from abc import abstractmethod
from functools import reduce
from typing import Protocol, TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.conjunto import Conj, conjuntoAleatorio, inserta, vacio
from src.TAD_Interseccion_de_dos_conjuntos import interseccion


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)

# 1ª solución
# ===========

def interseccionG(cs: list[Conj[A]]) -> Conj[A]:
    if len(cs) == 1:
        return cs[0]
    return interseccion(cs[0], interseccionG(cs[1:]))

# 2ª solución
# ===========

def interseccionG2(cs: list[Conj[A]]) -> Conj[A]:
    return reduce(interseccion, cs[1:], cs[0])

# 3ª solución
# ===========

def interseccionG3(cs: list[Conj[A]]) -> Conj[A]:
    r = cs[0]
    for c in cs[1:]:
        r = interseccion(c, r)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(conjuntoAleatorio(), min_size=1, max_size=10))
def test_interseccionG(cs: list[Conj[int]]) -> None:
    r = interseccionG(cs)
    assert interseccionG2(cs) == r
    assert interseccionG3(cs) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q TAD_Interseccion_de_varios_conjuntos.py
#    1 passed in 0.60s
