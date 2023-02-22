# TAD_Diferencia_simetrica.py
# TAD de los conjuntos: Diferencia simétrica.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    diferenciaSimetrica : (Conj[A], Conj[A]) -> Conj[A]
# tal que diferenciaSimetrica(c1, c2) es la diferencia simétrica de los
# conjuntos c1 y c2. Por ejemplo,
#    >>> ej1 = inserta(5, inserta(3, inserta(2, inserta(7, vacio()))))
#    >>> ej2 = inserta(7, inserta(4, inserta(3, vacio())))
#    >>> diferenciaSimetrica(ej1, ej2)
#    {2, 4, 5}
# ---------------------------------------------------------------------

from __future__ import annotations

from abc import abstractmethod
from copy import deepcopy
from typing import Protocol, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, pertenece, vacio)
from src.TAD_Diferencia_de_conjuntos import diferencia
from src.TAD_Interseccion_de_dos_conjuntos import interseccion
from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista,
                                                       listaAconjunto)
from src.TAD_Union_de_dos_conjuntos import union


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: A, otro: A) -> bool:
        pass

A = TypeVar('A', bound=Comparable)

# 1ª solución
# ===========

def diferenciaSimetrica(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    return diferencia(union(c1, c2), interseccion(c1, c2))

# 2ª solución
# ===========

def diferenciaSimetrica2(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    xs = conjuntoAlista(c1)
    ys = conjuntoAlista(c2)
    return listaAconjunto([x for x in xs if x not in ys] +
                          [y for y in ys if y not in xs])

# 3ª solución
# ===========

def diferenciaSimetrica3(c1: Conj[A], c2: Conj[A]) -> Conj[A]:
    r: Conj[A] = vacio()
    _c1 = deepcopy(c1)
    _c2 = deepcopy(c2)
    while not esVacio(_c1):
        mc1 = menor(_c1)
        if not pertenece(mc1, c2):
            r = inserta(mc1, r)
        _c1 = elimina(mc1, _c1)
    while not esVacio(_c2):
        mc2 = menor(_c2)
        if not pertenece(mc2, c1):
            r = inserta(mc2, r)
        _c2 = elimina(mc2, _c2)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(c1=conjuntoAleatorio(), c2=conjuntoAleatorio())
def test_diferenciaSimetrica(c1: Conj[int], c2: Conj[int]) -> None:
    r = diferenciaSimetrica(c1, c2)
    assert diferenciaSimetrica2(c1, c2) == r
    assert diferenciaSimetrica3(c1, c2) == r

# La comprobación de las propiedades es
#    > poetry run pytest -q TAD_Diferencia_simetrica.py
#    1 passed in 0.30s
