# transformaciones_pilas_listas.py
# Transformación entre pilas y listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-enero-2023
# ======================================================================

# ---------------------------------------------------------------------
# Utilizando el [tipo abstacto de datos de las pilas](https://bit.ly/3GTToyK)
# definir las funciones
#    listaApila : (list[A]) -> Pila[A]
#    pilaAlista : (Pila[A]) -> list[A]
# tales que
# + listaApila(xs) es la pila formada por los elementos de xs.
#   Por ejemplo,
#      >>> listaApila([3, 2, 5])
#      5 | 2 | 3
# + pilaAlista(p) es la lista formada por los elementos de la
#   pila p. Por ejemplo,
#      >>> ej = apila(5, apila(2, apila(3, vacia())))
#      >>> pilaAlista(ej)
#      [3, 2, 5]
#      >>> print(ej)
#      5 | 2 | 3
#
# Comprobar con Hypothesis que ambas funciones son inversas; es decir,
#    pilaAlista(listaApila(xs)) == xs
#    listaApila(pilaAlista(p))  == p
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.pila import (Pila, apila, cima, desapila, esVacia, pilaAleatoria,
                          vacia)

A = TypeVar('A')

# 1ª definición de listaApila
# ===========================

def listaApila(ys: list[A]) -> Pila[A]:
    def aux(xs: list[A]) -> Pila[A]:
        if not xs:
            return vacia()
        return apila(xs[0], aux(xs[1:]))

    return aux(list(reversed(ys)))

# 2ª solución de listaApila
# =========================

def listaApila2(xs: list[A]) -> Pila[A]:
    p: Pila[A] = Pila()
    for x in xs:
        p.apila(x)
    return p

# Comprobación de equivalencia de las definiciones de listaApila
# ==============================================================

# La propiedad es
@given(st.lists(st.integers()))
def test_listaApila(xs: list[int]) -> None:
    assert listaApila(xs) == listaApila2(xs)

# 1ª definición de pilaAlista
# ===========================

def pilaAlista(p: Pila[A]) -> list[A]:
    if esVacia(p):
        return []
    cp = cima(p)
    dp = desapila(p)
    return pilaAlista(dp) + [cp]

# 2ª definición de pilaAlista
# ===========================

def pilaAlista2Aux(p: Pila[A]) -> list[A]:
    if p.esVacia():
        return []
    cp = p.cima()
    p.desapila()
    return pilaAlista2Aux(p) + [cp]

def pilaAlista2(p: Pila[A]) -> list[A]:
    p1 = deepcopy(p)
    return pilaAlista2Aux(p1)

# 3ª definición de pilaAlista
# ===========================

def pilaAlista3Aux(p: Pila[A]) -> list[A]:
    r = []
    while not p.esVacia():
        r.append(p.cima())
        p.desapila()
    return r[::-1]

def pilaAlista3(p: Pila[A]) -> list[A]:
    p1 = deepcopy(p)
    return pilaAlista3Aux(p1)

# Comprobación de equivalencia de las definiciones de pilaAlista
# ==============================================================

@given(p=pilaAleatoria())
def test_pilaAlista(p: Pila[int]) -> None:
    assert pilaAlista(p) == pilaAlista2(p)
    assert pilaAlista(p) == pilaAlista3(p)

# Comprobación de las propiedades
# ===============================

# La primera propiedad es
@given(st.lists(st.integers()))
def test_1_listaApila(xs: list[int]) -> None:
    assert pilaAlista(listaApila(xs)) == xs

# La segunda propiedad es
@given(p=pilaAleatoria())
def test_2_listaApila(p: Pila[int]) -> None:
    assert listaApila(pilaAlista(p)) == p

# La comprobación es
#      src> poetry run pytest -v transformaciones_pilas_listas.py
#      test_listaApila PASSED
#      test_pilaAlista PASSED
#      test_1_listaApila PASSED
#      test_2_listaApila PASSED
