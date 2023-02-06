# TAD_Conjuntos_disjuntos.py
# TAD de los conjuntos: Conjuntos disjuntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    disjuntos : (Conj[A], Conj[A]) -> bool
# tal que disjuntos(c1, c2) se verifica si los conjuntos c1 y c2 son
# disjuntos. Por ejemplo,
#    >>> ej1 = inserta(2, inserta(5, vacio()))
#    >>> ej2 = inserta(4, inserta(3, vacio()))
#    >>> ej3 = inserta(5, inserta(3, vacio()))
#    >>> disjuntos(ej1, ej2)
#    True
#    >>> disjuntos(ej1, ej3)
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from functools import reduce
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.conjunto import (Conj, conjuntoAleatorio, inserta, vacio,
                              esVacio, menor, elimina, pertenece)
from src.TAD_Interseccion_de_dos_conjuntos import interseccion
from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista)

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def disjuntos(c1: Conj[A], c2: Conj[A]) -> bool:
    return esVacio(interseccion(c1, c2))

# 2ª solución
# ===========

def disjuntos2(c1: Conj[A], c2: Conj[A]) -> bool:
    if esVacio(c1):
        return True
    mc1 = menor(c1)
    rc1 = elimina(mc1, c1)
    if pertenece(mc1, c2):
        return False
    return disjuntos2(rc1, c2)

# 3ª solución
# ===========

def disjuntos3(c1: Conj[A], c2: Conj[A]) -> bool:
    xs = conjuntoAlista(c1)
    ys = conjuntoAlista(c2)
    return all((x not in ys for x in xs))

# La función conjuntoAlista está definida en el ejercicio
# "Transformaciones entre conjuntos y listas" que se encuentra en
# https://bit.ly/3RexzxH

# 4ª solución
# ===========

def disjuntos4Aux(c1: Conj[A], c2: Conj[A]) -> bool:
    while not esVacio(c1):
        mc1 = menor(c1)
        if pertenece(mc1, c2):
            return False
        c1 = elimina(mc1, c1)
    return True

def disjuntos4(c1: Conj[A], c2: Conj[A]) -> bool:
    _c1 = deepcopy(c1)
    return disjuntos4Aux(_c1, c2)

# 5ª solución
# ===========

def disjuntos5Aux(c1: Conj[A], c2: Conj[A]) -> bool:
    while not c1.esVacio():
        mc1 = c1.menor()
        if c2.pertenece(mc1):
            return False
        c1.elimina(mc1)
    return True

def disjuntos5(c1: Conj[A], c2: Conj[A]) -> bool:
    _c1 = deepcopy(c1)
    return disjuntos5Aux(_c1, c2)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=conjuntoAleatorio(), c2=conjuntoAleatorio())
def test_disjuntos(c1: Conj[int], c2: Conj[int]) -> None:
    r = disjuntos(c1, c2)
    assert disjuntos2(c1, c2) == r
    assert disjuntos3(c1, c2) == r
    assert disjuntos4(c1, c2) == r
    assert disjuntos5(c1, c2) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q TAD_Conjuntos_disjuntos.py
#    1 passed in 0.34s
