# Pol_Transformaciones_polinomios_densas.py
# Transformaciones entre polinomios y listas densas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 21-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los polinomios]
# (https://bit.ly/3KwqXYu) definir las funciones
#    densaApolinomio : (list[A]) -> Polinomio[A]
#    polinomioAdensa : (Polinomio[A]) -> list[A]
# tales que
# + densaApolinomio(xs) es el polinomio cuya representación densa es
#   xs. Por ejemplo,
#      >>> densaApolinomio([9, 0, 0, 5, 0, 4, 7])
#      9*x^6 + 5*x^3 + 4*x + 7
# + polinomioAdensa(c) es la representación densa del polinomio p. Por
#   ejemplo,
#      >>> ejPol = consPol(6, 9, consPol(3, 5, consPol(1, 4, consPol(0, 7, polCero()))))
#      >>> ejPol
#      9*x^6 + 5*x^3 + 4*x + 7
#      >>> polinomioAdensa(ejPol)
#      [9, 0, 0, 5, 0, 4, 7]
#
# Comprobar con Hypothesis que ambas funciones son inversas.
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from typing import TypeVar

from hypothesis import given

from src.Pol_Coeficiente import coeficiente
from src.Pol_Transformaciones_dispersa_y_densa import (densaAdispersa,
                                                       densaAleatoria,
                                                       dispersaAdensa)
from src.Pol_Transformaciones_polinomios_dispersas import (dispersaApolinomio,
                                                           polinomioAdispersa)
from src.TAD.Polinomio import (Polinomio, coefLider, consPol, esPolCero, grado,
                               polCero, polinomioAleatorio, restoPol)

A = TypeVar('A', int, float, complex)

# 1ª definición de densaApolinomio
# ================================

def densaApolinomio(xs: list[A]) -> Polinomio[A]:
    if not xs:
        return polCero()
    return consPol(len(xs[1:]), xs[0], densaApolinomio(xs[1:]))

# 2ª definición de densaApolinomio
# ================================

def densaApolinomio2(xs: list[A]) -> Polinomio[A]:
    return dispersaApolinomio(densaAdispersa(xs))

# La función densaAdispersa está definida en el ejercicio
# "Transformaciones entre las representaciones dispersa y densa" que se
# encuentra en https://bit.ly/3GTyIqe

# La función dispersaApolinomio se encuentra en el ejercicio
# "Transformaciones entre polinomios y listas dispersas" que se
# encuentra en https://bit.ly/41GgQaB

# Comprobación de equivalencia de densaApolinomio
# ===============================================

# La propiedad es
@given(xs=densaAleatoria())
def test_densaApolinomio(xs: list[int]) -> None:
    assert densaApolinomio(xs) == densaApolinomio2(xs)

# La función densaAleatoria está definida en el ejercicio
# "Transformaciones entre las representaciones dispersa y densa" que se
# encuentra en https://bit.ly/3GTyIqe

# 1ª definición de polinomioAdensa
# ================================

def polinomioAdensa(p: Polinomio[A]) -> list[A]:
    if esPolCero(p):
        return []
    n = grado(p)
    return [coeficiente(k, p) for k in range(n, -1, -1)]

# La función coeficiente está definida en el ejercicio
# "Coeficiente del término de grado k" que se encuentra en
# https://bit.ly/413l3oQ

# 2ª definición de polinomioAdensa
# ================================

def polinomioAdensa2(p: Polinomio[A]) -> list[A]:
    return dispersaAdensa(polinomioAdispersa(p))

# La función dispersaAdensa está definida en el ejercicio
# "Transformaciones entre las representaciones dispersa y densa" que se
# encuentra en https://bit.ly/3GTyIqe

# La función polinomioAdispersa se encuentra en el ejercicio
# "Transformaciones entre polinomios y listas dispersas" que se
# encuentra en https://bit.ly/41GgQaB

# Comprobación de equivalencia de polinomioAdensa
# ===============================================

# La propiedad es
@given(p=polinomioAleatorio())
def test_polinomioAdensa(p: Polinomio[int]) -> None:
    assert polinomioAdensa(p) == polinomioAdensa2(p)

# Propiedades de inversa
# ======================

# La primera propiedad es
@given(xs=densaAleatoria())
def test_polinomioAdensa_densaApolinomio(xs: list[int]) -> None:
    assert polinomioAdensa(densaApolinomio(xs)) == xs

# La segunda propiedad es
@given(p=polinomioAleatorio())
def test_densaApolinomio_polinomioAdensa(p: Polinomio[int]) -> None:
    assert densaApolinomio(polinomioAdensa(p)) == p

# La comprobación es
#    > poetry run pytest -v Pol_Transformaciones_polinomios_densas.py
#    test_densaApolinomio PASSED
#    test_polinomioAdensa PASSED
#    test_polinomioAdensa_densaApolinomio PASSED
#    test_densaApolinomio_polinomioAdensa PASSED
