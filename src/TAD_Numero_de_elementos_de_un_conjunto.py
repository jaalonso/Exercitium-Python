# TAD_Numero_de_elementos_de_un_conjunto.py
# TAD de los conjuntos: Número de elementos de un conjunto
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 7-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los conjuntos](https://bit.ly/3HbB7fo)
# definir la función
#    cardinal : (Conj[A]) -> int
# tal que cardinal(c) es el número de elementos del conjunto c. Por
# ejemplo,
#    cardinal(inserta(4, inserta(5, vacio()))) == 2
#    cardinal(inserta(4, inserta(5, inserta(4, vacio())))) == 2
# ---------------------------------------------------------------------

from __future__ import annotations

from abc import abstractmethod
from copy import deepcopy
from typing import Protocol, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, vacio)
from src.TAD_Transformaciones_conjuntos_listas import conjuntoAlista


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)

# 1ª solución
# ===========

def cardinal(c: Conj[A]) -> int:
    if esVacio(c):
        return 0
    return 1 + cardinal(elimina(menor(c), c))

# 2ª solución
# ===========

def cardinal2(c: Conj[A]) -> int:
    return len(conjuntoAlista(c))

# 3ª solución
# ===========

def cardinal3(c: Conj[A]) -> int:
    r = 0
    while not esVacio(c):
        r = r + 1
        c = elimina(menor(c), c)
    return r

# 4ª solución
# ===========

def cardinal4Aux(c: Conj[A]) -> int:
    r = 0
    while not c.esVacio():
        r = r + 1
        c.elimina(menor(c))
    return r

def cardinal4(c: Conj[A]) -> int:
    _c = deepcopy(c)
    return cardinal4Aux(_c)

# Comprobación de equivalencia
# ============================

@given(c=conjuntoAleatorio())
def test_cardinal(c: Conj[int]) -> None:
    r = cardinal(c)
    assert cardinal2(c) == r
    assert cardinal3(c) == r
    assert cardinal3(c) == r

# La comprobación es
#    src> poetry run pytest -q TAD_Numero_de_elementos_de_un_conjunto.py
#    1 passed in 0.33s
