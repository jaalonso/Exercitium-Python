# ordenaInserPila.py
# Ordenación de pilas por inserción.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 2-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo de dato de las pilas](https://bit.ly/3GTToyK)
# (cuyo código se encuentra en [PilaConListas.hs](https://bit.ly/3vL41xD))
# definir la función
#    ordenaInserPila : (A, Pila[A]) -> Pila[A]
# tal que ordenaInserPila(p) es la pila obtenida ordenando por
# inserción los los elementos de la pila p. Por ejemplo,
#    >>> print(ordenaInserPila(apila(4, apila(1, apila(3, vacia())))))
#    1 | 3 | 4
#
# Comprobar con Hypothesis que la pila ordenaInserPila(p) está
# ordenada.
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.pilaConListas import (Pila, apila, cima, desapila, esVacia,
                                   pilaAleatoria, vacia)
from src.transformaciones_pilas_listas import (pilaAlista, listaApila)
from src.ordenadaPila import ordenadaPila

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def insertaPila(x: A, p: Pila[A]) -> Pila[A]:
    if esVacia(p):
        return apila(x, p)
    cp = cima(p)
    if x < cp:
        return apila(x, p)
    dp = desapila(p)
    return apila(cp, insertaPila(x, dp))

def ordenaInserPila1(p: Pila[A]) -> Pila[A]:
    if esVacia(p):
        return p
    cp = cima(p)
    dp = desapila(p)
    return insertaPila(cp, ordenaInserPila1(dp))

# 2ª solución
# ===========

# Se usarán las funciones listaApila y pilaAlista del ejercicio
# "Transformaciones entre pilas y listas" que se encuentra en
# https://bit.ly/3ZHewQ8

def insertaLista(x: A, ys: list[A]) -> list[A]:
    if not ys:
        return [x]
    if x < ys[0]:
        return [x] + ys
    return [ys[0]] + insertaLista(x, ys[1:])

def ordenaInserLista(xs: list[A]) -> list[A]:
    if not xs:
        return []
    return insertaLista(xs[0], ordenaInserLista(xs[1:]))

def ordenaInserPila2(p: Pila[A]) -> Pila[A]:
    return listaApila(list(reversed(ordenaInserLista(pilaAlista(p)))))

# 3ª solución
# ===========

def ordenaInserPila3Aux(p: Pila[A]) -> Pila[A]:
    if p.esVacia():
        return p
    cp = p.cima()
    p.desapila()
    return insertaPila(cp, ordenaInserPila3Aux(p))

def ordenaInserPila3(p: Pila[A]) -> Pila[A]:
    q = deepcopy(p)
    return ordenaInserPila3Aux(q)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p=pilaAleatoria())
def test_ordenaInserPila(p: Pila[int]) -> None:
    r = ordenaInserPila1(p)
    assert ordenaInserPila2(p) == r
    assert ordenaInserPila3(p) == r

# La comprobación es
#    src> poetry run pytest -q ordenaInserPila.py
#    1 passed in 0.31s

# Comprobación de la propiedad
# ============================

# Se usará la función ordenadaPila del ejercicio
# "Reconocimiento de ordenación de pilas" que se encuentra en
# https://bit.ly/3COqRbK

# La propiedad es
@given(p=pilaAleatoria())
def test_ordenadaOrdenaInserPila(p: Pila[int]) -> None:
    ordenadaPila(ordenaInserPila1(p))

# La comprobación es
#    src> poetry run pytest -q ordenaInserPila.py
#    2 passed in 0.47s
