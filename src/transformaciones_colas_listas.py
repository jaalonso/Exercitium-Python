# transformaciones_colas_listas.py
# TAD de las colas: Transformación entre colas y listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-enero-2023
# ======================================================================

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3GTToyK)
# definir las funciones
#    listaAcola : (list[A]) -> Cola[A]
#    colaAlista : (Cola[A]) -> list[A]
# tales que
# + listaAcola(xs) es la cola formada por los elementos de xs.
#   Por ejemplo,
#      >>> print(listaAcola([3, 2, 5]))
#      3 | 2 | 5
# + colaAlista(c) es la lista formada por los elementos de la
#   cola c. Por ejemplo,
#      >>> ej = inserta(5, inserta(2, inserta(3, vacia())))
#      >>> colaAlista(ej)
#      [3, 2, 5]
#      >>> print(ej)
#      5 | 2 | 3
#
# Comprobar con Hypothesis que ambas funciones son inversas; es decir,
#    colaAlista(listaAcola(xs)) == xs
#    listaAcola(colaAlista(c))  == c
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.cola import (Cola, inserta, primero, resto, esVacia, vacia,
                          colaAleatoria)

A = TypeVar('A')

# 1ª definición de listaAcola
# ===========================

def listaAcola(ys: list[A]) -> Cola[A]:
    def aux(xs: list[A]) -> Cola[A]:
        if not xs:
            return vacia()
        return inserta(xs[0], aux(xs[1:]))

    return aux(list(reversed(ys)))

# 2ª solución de listaAcola
# =========================

def listaAcola2(xs: list[A]) -> Cola[A]:
    p: Cola[A] = Cola()
    for x in xs:
        p.inserta(x)
    return p

# Comprobación de equivalencia de las definiciones de listaAcola
# ==============================================================

# La propiedad es
@given(st.lists(st.integers()))
def test_listaAcola(xs: list[int]) -> None:
    assert listaAcola(xs) == listaAcola2(xs)

# 1ª definición de colaAlista
# ===========================

def colaAlista(c: Cola[A]) -> list[A]:
    if esVacia(c):
        return []
    pc = primero(c)
    rc = resto(c)
    return [pc] + colaAlista(rc)

# 2ª definición de colaAlista
# ===========================

def colaAlista2Aux(c: Cola[A]) -> list[A]:
    if c.esVacia():
        return []
    pc = c.primero()
    c.resto()
    return [pc] + colaAlista2Aux(c)

def colaAlista2(c: Cola[A]) -> list[A]:
    c1 = deepcopy(c)
    return colaAlista2Aux(c1)

# 3ª definición de colaAlista
# ===========================

def colaAlista3Aux(c: Cola[A]) -> list[A]:
    r = []
    while not c.esVacia():
        r.append(c.primero())
        c.resto()
    return r

def colaAlista3(c: Cola[A]) -> list[A]:
    c1 = deepcopy(c)
    return colaAlista3Aux(c1)

# Comprobación de equivalencia de las definiciones de colaAlista
# ==============================================================

@given(p=colaAleatoria())
def test_colaAlista(p: Cola[int]) -> None:
    assert colaAlista(p) == colaAlista2(p)
    assert colaAlista(p) == colaAlista3(p)

# Comprobación de las propiedades
# ===============================

# La primera propiedad es
@given(st.lists(st.integers()))
def test_1_listaAcola(xs: list[int]) -> None:
    assert colaAlista(listaAcola(xs)) == xs

# La segunda propiedad es
@given(c=colaAleatoria())
def test_2_listaAcola(c: Cola[int]) -> None:
    assert listaAcola(colaAlista(c)) == c

# La comprobación es
#      src> poetry run pytest -v transformaciones_colas_listas.py
#      test_listaAcola PASSED
#      test_colaAlista PASSED
#      test_1_listaAcola PASSED
#      test_2_listaAcola PASSED
