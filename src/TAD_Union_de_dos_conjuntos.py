# TAD_Union_de_dos_conjuntos.py
# TAD de los conjuntos: Unión de dos conjuntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 8-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los conjuntos](https://bit.ly/3HbB7fo)
# definir la función
#    union : (Conj[A], Conj[A]) -> Conj[A]
# tal (union c1 c2) es la unión de ambos conjuntos. Por ejemplo,
#    >>> ej1 = inserta(3, inserta(5, vacio()))
#    >>> ej2 = inserta(4, inserta(3, vacio()))
#    >>> union(ej1, ej2)
#    {3, 4, 5}
# ---------------------------------------------------------------------

from copy import deepcopy
from functools import reduce
from typing import TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)
from src.TAD_Transformaciones_conjuntos_listas import conjuntoAlista

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def union(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    if esVacio(c1):
        return c2
    mc1 = menor(c1)
    rc1 = elimina(mc1, c1)
    return inserta(mc1, union(rc1, c2))

# 2ª solución
# ===========

def union2(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    return reduce(lambda c, x: inserta(x, c), conjuntoAlista(c1), c2)

# La función conjuntoAlista está definida en el ejercicio
# "Transformaciones entre conjuntos y listas" que se encuentra en
# https://bit.ly/3RexzxH

# 3ª solución
# ===========

def union3(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    r = c2
    while not esVacio(c1):
        mc1 = menor(c1)
        r = inserta(mc1, r)
        c1 = elimina(mc1, c1)
    return r

# 4ª solución
# ===========

def union4Aux(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    while not c1.esVacio():
        mc1 = menor(c1)
        c2.inserta(mc1)
        c1.elimina(mc1)
    return c2

def union4(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    _c1 = deepcopy(c1)
    _c2 = deepcopy(c2)
    return union4Aux(_c1, _c2)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=conjuntoAleatorio(), c2=conjuntoAleatorio())
def test_union(c1: Conj[int], c2: Conj[int]) -> None:
    r = union(c1, c2)
    assert union2(c1, c2) == r
    assert union3(c1, c2) == r
    assert union4(c1, c2) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q TAD_Union_de_dos_conjuntos.py
#    1 passed in 0.35s
