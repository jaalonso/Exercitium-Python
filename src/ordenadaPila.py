# ordenadaPila.py
# Reconocimiento de ordenación de pilas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las pilas](https://bit.ly/3GTToyK),
# definir la función
#    ordenadaPila : (Pila[A]) -> bool
# tal que ordenadaPila(p) se verifica si los elementos de la pila p
# están ordenados en orden creciente. Por ejemplo,
#    >>> ordenadaPila(apila(1, apila(5, apila(6, vacia()))))
#    True
#    >>> ordenadaPila(apila(1, apila(0, apila(6, vacia()))))
#    False
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.pila import (Pila, apila, cima, desapila, esVacia, pilaAleatoria,
                          vacia)
from src.transformaciones_pilas_listas import pilaAlista

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def ordenadaPila(p: Pila[A]) -> bool:
    if esVacia(p):
        return True
    cp = cima(p)
    dp = desapila(p)
    if esVacia(dp):
        return True
    cdp = cima(dp)
    return cp <= cdp and ordenadaPila(dp)

# 2ª solución
# ===========

# Se usará la función pilaAlista del ejercicio
# "Transformaciones entre pilas y listas" que se encuentra en
# https://bit.ly/3ZHewQ8

# ordenadaLista(xs, ys) se verifica si xs es una lista ordenada. Por
# ejemplo,
#    >>> ordenadaLista([2, 5, 8])
#    True
#    >>> ordenadalista([2, 8, 5])
#    False
def ordenadaLista(xs: list[A]) -> bool:
    return all((x <= y for (x, y) in zip(xs, xs[1:])))

def ordenadaPila2(p: Pila[A]) -> bool:
    return ordenadaLista(list(reversed(pilaAlista(p))))

# 3ª solución
# ===========

def ordenadaPila3Aux(p: Pila[A]) -> bool:
    if p.esVacia():
        return True
    cp = p.cima()
    p.desapila()
    if p.esVacia():
        return True
    return cp <= p.cima() and ordenadaPila3Aux(p)

def ordenadaPila3(p: Pila[A]) -> bool:
    q = deepcopy(p)
    return ordenadaPila3Aux(q)

# 4ª solución
# ===========

def ordenadaPila4Aux(p: Pila[A]) -> bool:
    while not p.esVacia():
        cp = p.cima()
        p.desapila()
        if not p.esVacia() and cp > p.cima():
            return False
    return True

def ordenadaPila4(p: Pila[A]) -> bool:
    q = deepcopy(p)
    return ordenadaPila4Aux(q)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p=pilaAleatoria())
def test_ordenadaPila(p: Pila[int]) -> None:
    r = ordenadaPila(p)
    assert ordenadaPila2(p) == r
    assert ordenadaPila3(p) == r
    assert ordenadaPila4(p) == r

# La comprobación es
#    src> poetry run pytest -q ordenadaPila.py
#    1 passed in 0.31s
