# TAD_Union_de_varios_conjuntos.py
# TAD de los conjuntos: Unión de varios conjuntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los conjuntos](https://bit.ly/3HbB7fo)
# definir la función
#    unionG : (list[Conj[A]]) -> Conj[A]
# tal unionG(cs) calcule la unión de la lista de conjuntos cd. Por
# ejemplo,
#    >>> ej1 = inserta(3, inserta(5, vacio()))
#    >>> ej2 = inserta(5, inserta(6, vacio()))
#    >>> ej3 = inserta(3, inserta(6, vacio()))
#    >>> unionG([ej1, ej2, ej3])
#    {3, 5, 6}
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from __future__ import annotations

from abc import abstractmethod
from functools import reduce
from typing import Protocol, TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.conjunto import Conj, conjuntoAleatorio, inserta, vacio
from src.TAD_Union_de_dos_conjuntos import union


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)

# 1ª solución
# ===========

def unionG(cs: list[Conj[A]]) -> Conj[A]:
    if not cs:
        return vacio()
    return union(cs[0], unionG(cs[1:]))

# La función union está definida en el ejercicio
# "Unión de dos conjuntos" que se encuentra en
# https://bit.ly/3Y1jBl8

# 2ª solución
# ===========

def unionG2(cs: list[Conj[A]]) -> Conj[A]:
    return reduce(union, cs, vacio())

# 3ª solución
# ===========

def unionG3(cs: list[Conj[A]]) -> Conj[A]:
    r: Conj[A] = vacio()
    for c in cs:
        r = union(c, r)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(conjuntoAleatorio(), max_size=10))
def test_union(cs: list[Conj[int]]) -> None:
    r = unionG(cs)
    assert unionG2(cs) == r
    assert unionG3(cs) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q TAD_Union_de_varios_conjuntos.py
#    1 passed in 0.75s
