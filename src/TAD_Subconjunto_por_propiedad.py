# TAD_Subconjunto_por_propiedad.py
# TAD de los conjuntos: Subconjunto determinado por una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 17-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el tipo abstracto de datos de los conjuntos
# (https://bit.ly/3HbB7fo) definir la función
#    filtra : (Callable[[A], bool], Conj[A]) -> Conj[A]
# tal (filtra p c) es el conjunto de elementos de c que verifican el
# predicado p. Por ejemplo,
#    >>> ej = inserta(5, inserta(4, inserta(7, inserta(2, vacio()))))
#    >>> filtra(lambda x: x % 2 == 0, ej)
#    {2, 4}
#    >>> filtra(lambda x: x % 2 == 1, ej)
#    {5, 7}
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import Callable, TypeVar

from hypothesis import given

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, pertenece, vacio)
from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista,
                                                       listaAconjunto)

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def filtra(p: Callable[[A], bool], c: Conj[A]) -> Conj[A]:
    if esVacio(c):
        return vacio()
    mc = menor(c)
    rc = elimina(mc, c)
    if p(mc):
        return inserta(mc, filtra(p, rc))
    return filtra(p, rc)

# 2ª solución
# ===========

def filtra2(p: Callable[[A], bool], c: Conj[A]) -> Conj[A]:
    return listaAconjunto(list(filter(p, conjuntoAlista(c))))

# 3ª solución
# ===========

def filtra3Aux(p: Callable[[A], bool], c: Conj[A]) -> Conj[A]:
    r: Conj[A] = vacio()
    while not esVacio(c):
        mc = menor(c)
        c = elimina(mc, c)
        if p(mc):
            r = inserta(mc, r)
    return r

def filtra3(p: Callable[[A], bool], c: Conj[A]) -> Conj[A]:
    _c = deepcopy(c)
    return filtra3Aux(p, _c)

# 4ª solución
# ===========

def filtra4Aux(p: Callable[[A], bool], c: Conj[A]) -> Conj[A]:
    r: Conj[A] = Conj()
    while not c.esVacio():
        mc = c.menor()
        c.elimina(mc)
        if p(mc):
            r.inserta(mc)
    return r

def filtra4(p: Callable[[A], bool], c: Conj[A]) -> Conj[A]:
    _c = deepcopy(c)
    return filtra4Aux(p, _c)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(c=conjuntoAleatorio())
def test_filtra(c: Conj[int]) -> None:
    r = filtra(lambda x: x % 2 == 0, c)
    assert filtra2(lambda x: x % 2 == 0, c) == r
    assert filtra3(lambda x: x % 2 == 0, c) == r
    assert filtra4(lambda x: x % 2 == 0, c) == r

# La comprobación es
#    src> poetry run pytest -q TAD_Subconjunto_por_propiedad.py
#    1 passed in 0.28s
