# pertenecePila.py
# Pertenencia a una pila.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 26-enero-2023
# ======================================================================

# ---------------------------------------------------------------------
# Utilizando el [tipo dato de las pilas](https://bit.ly/3GTToyK)
# (cuyo código se encuentra en [pilaConListas.hs](https://bit.ly/3VVt8by)
# definir la función
#    pertenecePila : (A, Pila[A]) -> bool
# tal que pertenecePila(x, p) se verifica si x es un elemento de la
# pila p. Por ejemplo,
#    >>> pertenecePila(2, apila(5, apila(2, apila(3, vacia()))))
#    True
#    >>> pertenecePila(4, apila(5, apila(2, apila(3, vacia()))))
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.pilaConListas import (Pila, apila, cima, desapila, esVacia,
                                   pilaAleatoria, vacia)

A = TypeVar('A')

# 1ª solución
# ===========

def pertenecePila1(x: A, p: Pila[A]) -> bool:
    if esVacia(p):
        return False
    cp = cima(p)
    dp = desapila(p)
    return x == cp or pertenecePila1(x, dp)

# 2ª solución
# ===========

# pilaAlista(p) es la lista formada por los elementos de la
# lista p. Por ejemplo,
#    >>> pilaAlista(apila(5, apila(2, apila(3, vacia()))))
#    [3, 2, 5]
def pilaAlista(p: Pila[A]) -> list[A]:
    if esVacia(p):
        return []
    cp = cima(p)
    dp = desapila(p)
    return pilaAlista(dp) + [cp]

def pertenecePila2(x: A, p: Pila[A]) -> bool:
    return x in pilaAlista(p)

# 3ª solución
# ===========

def pertenecePila3Aux(x: A, p: Pila[A]) -> bool:
    if p.esVacia():
        return False
    cp = p.cima()
    p.desapila()
    return x == cp or pertenecePila3Aux(x, p)

def pertenecePila3(x: A, p: Pila[A]) -> bool:
    p1 = deepcopy(p)
    return pertenecePila3Aux(x, p1)

# 4ª solución
# ===========

def pertenecePila4Aux(x: A, p: Pila[A]) -> bool:
    while not p.esVacia():
        cp = p.cima()
        p.desapila()
        if x == cp:
            return True
    return False

def pertenecePila4(x: A, p: Pila[A]) -> bool:
    p1 = deepcopy(p)
    return pertenecePila4Aux(x, p1)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(x=st.integers(), p=pilaAleatoria())
def test_pertenecePila(x: int, p: Pila[int]) -> None:
    r = pertenecePila1(x, p)
    assert pertenecePila2(x, p) == r
    assert pertenecePila3(x, p) == r
    assert pertenecePila4(x, p) == r

# La comprobación es
#    src> poetry run pytest -q pertenecePila.py
#    1 passed in 0.37s
