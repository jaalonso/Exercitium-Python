# prefijoPila.py
# Reconocimiento de prefijos de pilas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las pilas](https://bit.ly/3GTToyK),
# definir la función
#    prefijoPila : (Pila[A], Pila[A]) -> bool
# tal que prefijoPila(p1, p2) se verifica si la pila p1 es justamente
# un prefijo de la pila p2. Por ejemplo,
#    >>> ej1 = apila(4, apila(2, vacia()))
#    >>> ej2 = apila(4, apila(2, apila(5, vacia())))
#    >>> ej3 = apila(5, apila(4, apila(2, vacia())))
#    >>> prefijoPila(ej1, ej2)
#    True
#    >>> prefijoPila(ej1, ej3)
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.pila import (Pila, apila, cima, desapila, esVacia, pilaAleatoria,
                          vacia)
from src.transformaciones_pilas_listas import pilaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def prefijoPila(p1: Pila[A], p2: Pila[A]) -> bool:
    if esVacia(p1):
        return True
    if esVacia(p2):
        return False
    cp1 = cima(p1)
    dp1 = desapila(p1)
    cp2 = cima(p2)
    dp2 = desapila(p2)
    return cp1 == cp2 and prefijoPila(dp1, dp2)

# 2ª solución
# ===========

# Se usará la función pilaAlista del ejercicio
# "Transformaciones entre pilas y listas" que se encuentra en
# https://bit.ly/3ZHewQ8

def esSufijoLista(xs: list[A], ys: list[A]) -> bool:
    if not xs:
        return True
    return xs == ys[-len(xs):]

def prefijoPila2(p1: Pila[A], p2: Pila[A]) -> bool:
    return esSufijoLista(pilaAlista(p1), pilaAlista(p2))

# 3ª solución
# ===========

def prefijoPila3Aux(p1: Pila[A], p2: Pila[A]) -> bool:
    if p1.esVacia():
        return True
    if p2.esVacia():
        return False
    cp1 = p1.cima()
    p1.desapila()
    cp2 = p2.cima()
    p2.desapila()
    return cp1 == cp2 and prefijoPila3(p1, p2)

def prefijoPila3(p1: Pila[A], p2: Pila[A]) -> bool:
    q1 = deepcopy(p1)
    q2 = deepcopy(p2)
    return prefijoPila3Aux(q1, q2)

# 4ª solución
# ===========

def prefijoPila4Aux(p1: Pila[A], p2: Pila[A]) -> bool:
    while not p2.esVacia() and not p1.esVacia():
        if p1.cima() != p2.cima():
            return False
        p1.desapila()
        p2.desapila()
    return p1.esVacia()

def prefijoPila4(p1: Pila[A], p2: Pila[A]) -> bool:
    q1 = deepcopy(p1)
    q2 = deepcopy(p2)
    return prefijoPila4Aux(q1, q2)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p1=pilaAleatoria(), p2=pilaAleatoria())
def test_prefijoPila(p1: Pila[int], p2: Pila[int]) -> None:
    r = prefijoPila(p1, p2)
    assert prefijoPila2(p1, p2) == r
    assert prefijoPila3(p1, p2) == r
    assert prefijoPila4(p1, p2) == r

# La comprobación es
#    src> poetry run pytest -q prefijoPila.py
#    1 passed in 0.32s
