# agrupaColas.py
# TAD de las colas: Agrupación de colas
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 17-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de las colas](https://bit.ly/3QWTsRL),
# definir la función
#    agrupaColas : (list[Cola[A]]) -> Cola[A]
# tal que (agrupaColas [c1,c2,c3,...,cn]) es la cola formada mezclando
# las colas de la lista como sigue: mezcla c1 con c2, el resultado con
# c3, el resultado con c4, y así sucesivamente. Por ejemplo,
#    >>> ej1 = inserta(2, inserta(5, vacia()))
#    >>> ej2 = inserta(3, inserta(7, inserta(4, vacia())))
#    >>> ej3 = inserta(9, inserta(0, inserta(1, inserta(6, vacia()))))
#    >>> print(agrupaColas([]))
#    -
#    >>> print(agrupaColas([ej1]))
#    5 | 2
#    >>> print(agrupaColas([ej1, ej2]))
#    5 | 4 | 2 | 7 | 3
#    >>> print(agrupaColas([ej1, ej2, ej3]))
#    5 | 6 | 4 | 1 | 2 | 0 | 7 | 9 | 3
# ---------------------------------------------------------------------

from functools import reduce
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.cola import (Cola, colaAleatoria, inserta, vacia)
from src.intercalaColas import intercalaColas

A = TypeVar('A')

# 1ª solución
# ===========

def agrupaColas1(cs: list[Cola[A]]) -> Cola[A]:
    if not cs:
        return vacia()
    if len(cs) == 1:
        return cs[0]
    return agrupaColas1([intercalaColas(cs[0], cs[1])] + cs[2:])

# La función intercalaColas está definida en el ejercicio
# "TAD de las colas: Intercalado de dos colas" que se encuentra en
# https://bit.ly/3XYyjsM

# 2ª solución
# ===========

def agrupaColas2(cs: list[Cola[A]]) -> Cola[A]:
    return reduce(intercalaColas, cs, vacia())

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(colaAleatoria(), max_size=4))
def test_extiendeCola(cs: list[Cola[int]]) -> None:
    assert agrupaColas1(cs) == agrupaColas2(cs)

# La comprobación es
#    src> poetry run pytest -q agrupaColas.py
#    1 passed in 0.50s
