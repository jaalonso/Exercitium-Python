# longitudCola.py
# TAD de las colas: Longitud de una cola.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    longitudCola : (Cola[A]) -> int
# tal que longitudCola(c) es el número de elementos de la cola c. Por
# ejemplo,
#    >>> longitudCola(inserta(4, inserta(2, inserta(5, vacia()))))
#    3
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.cola import Cola, colaAleatoria, esVacia, inserta, resto, vacia
from src.transformaciones_colas_listas import colaAlista

A = TypeVar('A')

# 1ª solución
# ===========

def longitudCola1(c: Cola[A]) -> int:
    if esVacia(c):
        return 0
    return 1 + longitudCola1(resto(c))

# 2ª solución
# ===========

def longitudCola2(c: Cola[A]) -> int:
    return len(colaAlista(c))

# 3ª solución
# ===========

def longitudCola3Aux(c: Cola[A]) -> int:
    if c.esVacia():
        return 0
    c.resto()
    return 1 + longitudCola3Aux(c)

def longitudCola3(c: Cola[A]) -> int:
    _c = deepcopy(c)
    return longitudCola3Aux(_c)

# 4ª solución
# ===========

def longitudCola4Aux(c: Cola[A]) -> int:
    r = 0
    while not esVacia(c):
        r = r + 1
        c = resto(c)
    return r

def longitudCola4(c: Cola[A]) -> int:
    _c = deepcopy(c)
    return longitudCola4Aux(_c)

# 5ª solución
# ===========

def longitudCola5Aux(c: Cola[A]) -> int:
    r = 0
    while not c.esVacia():
        r = r + 1
        c.resto()
    return r

def longitudCola5(c: Cola[A]) -> int:
    _c = deepcopy(c)
    return longitudCola5Aux(_c)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c=colaAleatoria())
def test_longitudCola_(c: Cola[int]) -> None:
    r = longitudCola1(c)
    assert longitudCola2(c) == r
    assert longitudCola3(c) == r
    assert longitudCola4(c) == r
    assert longitudCola5(c) == r

# La comprobación es
#    src> poetry run pytest -q longitudCola.py
#    1 passed in 0.28s
