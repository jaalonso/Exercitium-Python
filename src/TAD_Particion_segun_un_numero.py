# TAD_Particion_segun_un_numero.py
# TAD de los conjuntos: Partición según un número.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 21-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    divide : (A, Conj[A]) -> tuple[Conj[A], Conj[A]]
# tal que (divide x c) es el par formado por dos subconjuntos de c: el
# de los elementos menores o iguales que x y el de los mayores que x.
# Por ejemplo,
#    >>> divide(5, inserta(7, inserta(2, inserta(8, vacio()))))
#    ({2}, {7, 8})
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)
from src.TAD_Particion_por_una_propiedad import particion

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def divide(x: A, c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    if esVacio(c):
        return (vacio(), vacio())
    mc = menor(c)
    rc = elimina(mc, c)
    (c1, c2) = divide(x, rc)
    if mc <= x:
        return (inserta(mc, c1), c2)
    return (c1, inserta(mc, c2))

# 2ª solución
# ===========

def divide2(x: A, c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    return particion(lambda y: y <= x, c)

# La función particion está definida en el ejercicio
# "Partición de un conjunto según una propiedad" que se encuentra en
# https://bit.ly/3YCOah5

# 3ª solución
# ===========

def divide3Aux(x: A, c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    r: Conj[A] = vacio()
    s: Conj[A] = vacio()
    while not esVacio(c):
        mc = menor(c)
        c = elimina(mc, c)
        if mc <= x:
            r = inserta(mc, r)
        else:
            s = inserta(mc, s)
    return (r, s)

def divide3(x: A, c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    _c = deepcopy(c)
    return divide3Aux(x, _c)

# 4ª solución
# ===========

def divide4Aux(x: A, c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    r: Conj[A] = Conj()
    s: Conj[A] = Conj()
    while not c.esVacio():
        mc = c.menor()
        c.elimina(mc)
        if mc <= x:
            r.inserta(mc)
        else:
            s.inserta(mc)
    return (r, s)

def divide4(x: A, c: Conj[A]) -> tuple[Conj[A], Conj[A]]:
    _c = deepcopy(c)
    return divide4Aux(x, _c)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(x=st.integers(), c=conjuntoAleatorio())
def test_particion(x: int, c: Conj[int]) -> None:
    r = divide(x, c)
    assert divide2(x, c) == r
    assert divide3(x, c) == r
    assert divide4(x, c) == r

# La comprobación es
#    src> poetry run pytest -q TAD_Particion_segun_un_numero.py
#    1 passed in 0.30s
