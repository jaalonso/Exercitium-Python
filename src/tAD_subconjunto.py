# tAD_subconjunto.py
# TAD de los conjuntos: Reconocimiento de subconjunto.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 01-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los conjuntos](https://bit.ly/3HbB7fo)
# definir la función
#    subconjunto :: Ord a => Conj a -> Conj a -> Bool
# tal que (subconjunto c1 c2) se verifica si todos los elementos de c1
# pertenecen a c2. Por ejemplo,
#    >>> ej1 = inserta(5, inserta(2, vacio()))
#    >>> ej2 = inserta(3, inserta(2, inserta(5, vacio())))
#    >>> ej3 = inserta(3, inserta(4, inserta(5, vacio())))
#    >>> subconjunto(ej1, ej2)
#    True
#    >>> subconjunto(ej1, ej3)
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, pertenece, vacio)
from src.transformaciones_conjuntos_listas import conjuntoAlista

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def subconjunto(c1: Conj[A], c2: Conj[A]) -> bool:
    if esVacio(c1):
        return True
    mc1 = menor(c1)
    rc1 = elimina(mc1, c1)
    return pertenece(mc1, c2) and subconjunto(rc1, c2)

# 2ª solución
# ===========

def subconjunto2(c1: Conj[A], c2: Conj[A]) -> bool:
    return all((pertenece(x, c2) for x in conjuntoAlista(c1)))

# La función conjuntoAlista está definida en el ejercicio
# "Transformaciones entre conjuntos y listas" que se encuentra en
# https://bit.ly/3RexzxH

# 3ª solución
# ===========

# (sublista xs ys) se verifica si xs es una sublista de ys. Por
# ejemplo,
#    sublista [5, 2] [3, 2, 5]  ==  True
#    sublista [5, 2] [3, 4, 5]  ==  False
def sublista(xs: list[A], ys: list[A]) -> bool:
    if not xs:
        return True
    return xs[0] in ys and sublista(xs[1:], ys)

def subconjunto3(c1: Conj[A], c2: Conj[A]) -> bool:
    return sublista(conjuntoAlista(c1), conjuntoAlista(c2))

# 4ª solución
# ===========

def subconjunto4(c1: Conj[A], c2: Conj[A]) -> bool:
    while not esVacio(c1):
        mc1 = menor(c1)
        if not pertenece(mc1, c2):
            return False
        c1 = elimina(mc1, c1)
    return True

# 5ª solución
# ===========

def subconjunto5Aux(c1: Conj[A], c2: Conj[A]) -> bool:
    while not c1.esVacio():
        mc1 = c1.menor()
        if not c2.pertenece(mc1):
            return False
        c1.elimina(mc1)
    return True

def subconjunto5(c1: Conj[A], c2: Conj[A]) -> bool:
    _c1 = deepcopy(c1)
    return subconjunto5Aux(_c1, c2)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=conjuntoAleatorio(), c2=conjuntoAleatorio())
def test_subconjunto(c1: Conj[int], c2: Conj[int]) -> None:
    r = subconjunto(c1, c2)
    assert subconjunto2(c1, c2) == r
    assert subconjunto3(c1, c2) == r
    assert subconjunto4(c1, c2) == r
    assert subconjunto5(c1, c2) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q tAD_subconjunto.py
#    1 passed in 0.37s
