# contenidaCola.py
# Inclusión de colas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 21-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    contenidaCola : (Cola[A], Cola[A]) -> bool
# tal que contenidaCola(c1, c2) se verifica si todos los elementos de la
# cola c1 son elementos de la cola c2. Por ejemplo,
#    >>> ej1 = inserta(3, inserta(2, vacia()))
#    >>> ej2 = inserta(3, inserta(4, vacia()))
#    >>> ej3 = inserta(5, inserta(2, inserta(3, vacia())))
#    >>> contenidaCola(ej1, ej3)
#    True
#    >>> contenidaCola(ej2, ej3)
#    False
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.perteneceCola import perteneceCola
from src.TAD.cola import (Cola, colaAleatoria, esVacia, inserta, primero,
                          resto, vacia)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def contenidaCola1(c1: Cola[A], c2: Cola[A]) -> bool:
    if esVacia(c1):
        return True
    return perteneceCola(primero(c1), c2) and contenidaCola1(resto(c1), c2)

# La función perteneceCola está definida en el ejercicio
# "Pertenencia a una cola" que se encuentra en
# https://bit.ly/3RcVgqb

# 2ª solución
# ===========

def contenidaCola2(c1: Cola[A], c2: Cola[A]) -> bool:
    return set(colaAlista(c1)) <= set(colaAlista(c2))

# La función colaAlista está definida en el ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

# 3ª solución
# ===========

def contenidaCola3Aux(c1: Cola[A], c2: Cola[A]) -> bool:
    if c1.esVacia():
        return True
    pc1 = c1.primero()
    c1.resto()
    return perteneceCola(pc1, c2) and contenidaCola1(c1, c2)

def contenidaCola3(c1: Cola[A], c2: Cola[A]) -> bool:
    _c1 = deepcopy(c1)
    return contenidaCola3Aux(_c1, c2)

# 4ª solución
# ===========

def contenidaCola4Aux(c1: Cola[A], c2: Cola[A]) -> bool:
    while not c1.esVacia():
        pc1 = c1.primero()
        c1.resto()
        if not perteneceCola(pc1, c2):
            return False
    return True

def contenidaCola4(c1: Cola[A], c2: Cola[A]) -> bool:
    _c1 = deepcopy(c1)
    return contenidaCola4Aux(_c1, c2)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c1=colaAleatoria(), c2=colaAleatoria())
def test_contenidaCola(c1: Cola[int], c2: Cola[int]) -> None:
    r = contenidaCola1(c1, c2)
    assert contenidaCola2(c1, c2) == r
    assert contenidaCola3(c1, c2) == r
    assert contenidaCola4(c1, c2) == r

# La comprobación es
#    src> poetry run pytest -q contenidaCola.py
#    1 passed in 0.44s
