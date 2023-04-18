# Pol_Termino_lider.py
# TAD de los polinomios: Término líder de un polinomio.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 25-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    termLider : (Polinomio[A]) -> Polinomio[A]
# tal que termLider(p) es el término líder del polinomio p. Por
# ejemplo,
#    >>> ejPol = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
#    >>> ejPol
#    x^5 + 5*x^2 + 4*x
#    >>> termLider(ejPol)
#    x^5
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from typing import TypeVar

from hypothesis import given

from src.Pol_Crea_termino import creaTermino
from src.TAD.Polinomio import (Polinomio, coefLider, consPol, grado, polCero,
                               polinomioAleatorio)

A = TypeVar('A', int, float, complex)

# 1ª solución
# ===========

def termLider(p: Polinomio[A]) -> Polinomio[A]:
    return creaTermino(grado(p), coefLider(p))

# 2ª solución
# ===========

def termLider2(p: Polinomio[A]) -> Polinomio[A]:
    return creaTermino(p.grado(), p.coefLider())

# La función creaTermino está definida en el ejercicio
# "Construcción de términos" que se encuentra en
# https://bit.ly/3GXteuH

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(p=polinomioAleatorio())
def test_termLider(p: Polinomio[int]) -> None:
    assert termLider(p) == termLider2(p)

# La comprobación es
#    > poetry run pytest -q Pol_Termino_lider.py
#    1 passed in 0.21s
