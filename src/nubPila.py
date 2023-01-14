# nubPila.py
# Eliminación de repeticiones en una pila.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo de dato de las pilas](https://bit.ly/3GTToyK)
# (cuyo código se encuentra en [PilaConListas.hs](https://bit.ly/3vL41xD))
# definir la función
#    nubPila :: Eq a => Pila a -> Pila a
# tal que (nubPila p) es la pila con los elementos de p sin repeticiones.
# Por ejemplo,
#    >>> ej = apila(3, apila(1, apila(3, apila(5, vacia()))))
#    >>> print(ej)
#    3 | 1 | 3 | 5
#    >>> print(nubPila1(ej))
#    1 | 3 | 5
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.pilaConListas import (Pila, apila, cima, desapila, esVacia,
                                   pilaAleatoria, vacia)

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

# pertenecePila(x, p) se verifica si x es un elemento de la pila p. Por
# ejemplo,
#    >>> pertenecePila(2, apila(5, apila(2, apila(3, vacia()))))
#    True
#    >>> pertenecePila(4, apila(5, apila(2, apila(3, vacia()))))
#    False
def pertenecePila(x: A, p: Pila[A]) -> bool:
    if esVacia(p):
        return False
    cp = cima(p)
    dp = desapila(p)
    return x == cp or pertenecePila(x, dp)

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

# listaApila(xs) es la pila formada por los elementos de xs.
# Por ejemplo,
#    >>> print(listaApila([3, 2, 5]))
#    5 | 2 | 3
def listaApila(ys: list[A]) -> Pila[A]:
    def aux(xs: list[A]) -> Pila[A]:
        if not xs:
            return vacia()
        return apila(xs[0], aux(xs[1:]))

    return aux(list(reversed(ys)))

# pilaAlista(p) es la lista formada por los elementos de la
# lista p. Por ejemplo,
#    >>> ej = apila(5, apila(2, apila(3, vacia())))
#    >>> pilaAlista(ej)
#    [3, 2, 5]
#    >>> print(ej)
#    5 | 2 | 3
def pilaAlista(p: Pila[A]) -> list[A]:
    if esVacia(p):
        return []
    cp = cima(p)
    dp = desapila(p)
    return pilaAlista(dp) + [cp]

def nub(xs):
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
