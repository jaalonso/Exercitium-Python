# nubPila.py
# Eliminación de repeticiones en una pila.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las pilas](https://bit.ly/3GTToyK),
# definir la función
#    nubPila : (Pila[A]) -> Pila[A]
# tal que nubPila(p) es la pila con los elementos de p sin repeticiones.
# Por ejemplo,
#    >>> ej = apila(3, apila(1, apila(3, apila(5, vacia()))))
#    >>> ej
#    3 | 1 | 3 | 5
#    >>> nubPila1(ej)
#    1 | 3 | 5
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.pertenecePila import pertenecePila
from src.TAD.pila import (Pila, apila, cima, desapila, esVacia, pilaAleatoria,
                          vacia)
from src.transformaciones_pilas_listas import listaApila, pilaAlista

A = TypeVar('A')

# 1ª solución
# ===========

# Se usará la función pertenecePila del ejercicio
# "Pertenencia a una pila" que se encuentra en
# https://bit.ly/3WdM9GC

def nubPila1(p: Pila[A]) -> Pila[A]:
    if esVacia(p):
        return p
    cp = cima(p)
    dp = desapila(p)
    if pertenecePila(cp, dp):
        return nubPila1(dp)
    return apila(cp, nubPila1(dp))

# 2ª solución
# ===========

# Se usarán las funciones listaApila y pilaAlista del ejercicio
# "Transformaciones entre pilas y listas" que se encuentra en
# https://bit.ly/3ZHewQ8

def nub(xs: list[A]) -> list[A]:
    return [x for i, x in enumerate(xs) if x not in xs[:i]]

def nubPila2(p: Pila[A]) -> Pila[A]:
    return listaApila(nub(pilaAlista(p)))

# 3ª solución
# ===========

def nubPila3Aux(p: Pila[A]) -> Pila[A]:
    if p.esVacia():
        return p
    cp = p.cima()
    p.desapila()
    if pertenecePila(cp, p):
        return nubPila3Aux(p)
    return apila(cp, nubPila3Aux(p))

def nubPila3(p: Pila[A]) -> Pila[A]:
    q = deepcopy(p)
    return nubPila3Aux(q)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p=pilaAleatoria())
def test_nubPila(p: Pila[int]) -> None:
    r = nubPila1(p)
    assert nubPila2(p) == r
    assert nubPila3(p) == r

# La comprobación es
#    src> poetry run pytest -q nubPila.py
#    1 passed in 0.27s
