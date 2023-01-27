# perteneceCola.py
# Pertenencia a una cola.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-febrero-2023
# ======================================================================

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    perteneceCola : (A, Cola[A]) -> bool
# tal que perteneceCola(x, c) se verifica si x es un elemento de la
# cola p. Por ejemplo,
#    >>> perteneceCola(2, inserta(5, inserta(2, inserta(3, vacia()))))
#    True
#    >>> perteneceCola(4, inserta(5, inserta(2, inserta(3, vacia()))))
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.cola import (Cola, vacia, inserta, primero, resto, esVacia,
                          colaAleatoria)
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def perteneceCola(x: A, c: Cola[A]) -> bool:
    if esVacia(c):
        return False
    return x == primero(c) or perteneceCola(x, resto(c))

# 2ª solución
# ===========

def perteneceCola2(x: A, c: Cola[A]) -> bool:
    return x in colaAlista(c)

# Las función colaAlista está definida en el ejercicio
# "Transformaciones entre colas y listas" que se encuentra en
# https://bit.ly/3Xv0oIt

# 3ª solución
# ===========

def perteneceCola3Aux(x: A, c: Cola[A]) -> bool:
    if c.esVacia():
        return False
    pc = c.primero()
    c.resto()
    return x == pc or perteneceCola3Aux(x, c)

def perteneceCola3(x: A, c: Cola[A]) -> bool:
    c1 = deepcopy(c)
    return perteneceCola3Aux(x, c1)

# 4ª solución
# ===========

def perteneceCola4Aux(x: A, c: Cola[A]) -> bool:
    while not c.esVacia():
        pc = c.primero()
        c.resto()
        if x == pc:
            return True
    return False

def perteneceCola4(x: A, c: Cola[A]) -> bool:
    c1 = deepcopy(c)
    return perteneceCola4Aux(x, c1)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(x=st.integers(), c=colaAleatoria())
def test_perteneceCola(x: int, c: Cola[int]) -> None:
    r = perteneceCola(x, c)
    assert perteneceCola2(x, c) == r
    assert perteneceCola3(x, c) == r
    assert perteneceCola4(x, c) == r

# La comprobación es
#    src> poetry run pytest -q perteneceCola.py
#    1 passed in 0.25s
