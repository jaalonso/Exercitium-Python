# filtraPila.py
# Filtrar pilas según una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-enero-2023
# ======================================================================

# ---------------------------------------------------------------------
# Utilizando el tipo de las listas (de un ejercicio anterior cuyo
# código se encuentra en [pilaConListas.py](https://bit.ly/3VVt8by)
# definir la función
#    filtraPila : (Callable[[A], bool], Pila[A]) -> Pila[A]
# tal que filtraPila(p, q) es la pila obtenida con los elementos de
# pila q que verifican el predicado p, en el mismo orden. Por ejemplo,
#    >>> ej = apila(3, apila(4, apila(6, apila(5, vacia()))))
#    >>> print(filtraPila(lambda x: x % 2 == 0, ej))
#    4 | 6
#    >>> print(filtraPila(lambda x: x % 2 == 1, ej))
#    3 | 5
#    >>> print(ej)
#    3 | 4 | 6 | 5
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import Callable, TypeVar

from hypothesis import given

from src.TAD.pilaConListas import (Pila, apila, cima, desapila, esVacia,
                                   pilaAleatoria, vacia)

A = TypeVar('A')

# 1ª solución
# ===========

def filtraPila1(p: Callable[[A], bool], q: Pila[A]) -> Pila[A]:
    if esVacia(q):
        return q
    cq = cima(q)
    dq = desapila(q)
    r = filtraPila1(p, dq)
    if p(cq):
        return apila(cq, r)
    return r

# 2ª solución
# ===========

# listaApila(xs) es la pila formada por los elementos de xs.
# Por ejemplo,
#    >>> print(listaApila1([3, 2, 5]))
#    5 | 3 | 2
def listaApila(ys: list[A]) -> Pila[A]:
    def aux(xs: list[A]) -> Pila[A]:
        if not xs:
            return vacia()
        return apila(xs[0], aux(xs[1:]))

    return aux(list(reversed(ys)))

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

def filtraPila2(p: Callable[[A], bool], q: Pila[A]) -> Pila[A]:
    return listaApila(list(filter(p, pilaAlista(q))))

# 3ª solución
# ===========

def filtraPila3Aux(p: Callable[[A], bool], q: Pila[A]) -> Pila[A]:
    if q.esVacia():
        return q
    cq = q.cima()
    q.desapila()
    r = filtraPila3Aux(p, q)
    if p(cq):
        r.apila(cq)
    return r

def filtraPila3(p: Callable[[A], bool], q: Pila[A]) -> Pila[A]:
    q1 = deepcopy(q)
    return filtraPila3Aux(p, q1)

# 4ª solución
# ===========

def filtraPila4Aux(p: Callable[[A], bool], q: Pila[A]) -> Pila[A]:
    r: Pila[A] = Pila()
    while not q.esVacia():
        cq = q.cima()
        q.desapila()
        if p(cq):
            r.apila(cq)
    r1: Pila[A] = Pila()
    while not r.esVacia():
        r1.apila(r.cima())
        r.desapila()
    return r1

def filtraPila4(p: Callable[[A], bool], q: Pila[A]) -> Pila[A]:
    q1 = deepcopy(q)
    return filtraPila4Aux(p, q1)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p=pilaAleatoria())
def test_filtraPila(p: Pila[int]) -> None:
    r = filtraPila1(lambda x: x % 2 == 0, p)
    assert filtraPila2(lambda x: x % 2 == 0, p) == r
    assert filtraPila3(lambda x: x % 2 == 0, p) == r
    assert filtraPila4(lambda x: x % 2 == 0, p) == r

# La comprobación es
#    src> poetry run pytest -q filtraPila.py
#    1 passed in 0.25s
