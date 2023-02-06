# TAD_Diferencia_de_conjuntos.py
# TAD de los conjuntos: Diferencia de conjuntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    diferencia : (Conj[A], Conj[A]) -> Conj[A]
# tal que diferencia(c1, c2) es el conjunto de los elementos de c1 que
# no son elementos de c2. Por ejemplo,
#    >>> ej1 = inserta(5, inserta(3, inserta(2, inserta(7, vacio()))))
#    >>> ej2 = inserta(7, inserta(4, inserta(3, vacio())))
#    >>> diferencia(ej1, ej2)
#    {2, 5}
#    >>> diferencia(ej2, ej1)
#    {4}
#    >>> diferencia(ej1, ej1)
#    {}
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, pertenece, vacio)
from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista,
                                                       listaAconjunto)

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def diferencia(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    if esVacio(c1):
        return vacio()
    mc1 = menor(c1)
    rc1 = elimina(mc1, c1)
    if pertenece(mc1, c2):
        return diferencia(rc1, c2)
    return inserta(mc1, diferencia(rc1, c2))

# 2ª solución
# ===========

def diferencia2(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    return listaAconjunto([x for x in conjuntoAlista(c1)
                           if not pertenece(x, c2)])

# Las funciones conjuntoAlista y listaAconjunto está definida en el
# ejercicio Transformaciones entre conjuntos y listas" que se encuentra
# en https://bit.ly/3RexzxH

# 3ª solución
# ===========

def diferencia3Aux(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    r: Conj[A] = vacio()
    while not esVacio(c1):
        mc1 = menor(c1)
        if not pertenece(mc1, c2):
            r = inserta(mc1, r)
        c1 = elimina(mc1, c1)
    return r

def diferencia3(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    _c1 = deepcopy(c1)
    return diferencia3Aux(_c1, c2)

# 4ª solución
# ===========

def diferencia4Aux(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    r: Conj[A] = Conj()
    while not c1.esVacio():
        mc1 = c1.menor()
        if not c2.pertenece(mc1):
            r.inserta(mc1)
        c1.elimina(mc1)
    return r

def diferencia4(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    _c1 = deepcopy(c1)
    return diferencia4Aux(_c1, c2)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=conjuntoAleatorio(), c2=conjuntoAleatorio())
def test_diferencia(c1: Conj[int], c2: Conj[int]) -> None:
    r = diferencia(c1, c2)
    assert diferencia2(c1, c2) == r
    assert diferencia3(c1, c2) == r
    assert diferencia4(c1, c2) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q TAD_Diferencia_de_conjuntos.py
#    1 passed in 0.31s
