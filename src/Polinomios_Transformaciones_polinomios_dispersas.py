# Polinomios_Transformaciones_polinomios_dispersas.py
# TAD de los polinomios: Transformaciones entre polinomios y listas dispersas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los polinomios]
# (https://bit.ly/3KwqXYu) definir las funciones
#    dispersaApolinomio : (list[tuple[int, A]]) -> Polinomio[A]
#    polinomioAdispersa : (Polinomio[A]) -> list[tuple[int, A]]
# tales que
# + dispersaApolinomio(ps) es el polinomiocuya representación dispersa
#   es ps. Por ejemplo,
#      >>> dispersaApolinomio([(6, 9), (3, 5), (1, 4), (0, 7)])
#      9*x^6 + 5*x^3 + 4*x + 7
# + polinomioAdispersa(p) es la representación dispersa del polinomio
#   p. Por ejemplo,
#      >>> ejPol1 = consPol(3, 5, consPol(1, 4, consPol(0, 7, polCero())))
#      >>> ejPol = consPol(6, 9, ejPol1)
#      >>> ejPol
#      9*x^6 + 5*x^3 + 4*x + 7
#      >>> polinomioAdispersa(ejPol)
#      [(6, 9), (3, 5), (1, 4), (0, 7)]
#
# Comprobar con Hypothesis que ambas funciones son inversas.
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given

from src.Polinomios_Transformaciones_dispersa_y_densa import dispersaAleatoria
from src.TAD.Polinomio import (Polinomio, coefLider, consPol, esPolCero, grado,
                               polCero, polinomioAleatorio, restoPol)

A = TypeVar('A', int, float, complex)


# 1ª definición de dispersaApolinomio
# ===================================

def dispersaApolinomio(ps: list[tuple[int, A]]) -> Polinomio[A]:
    if not ps:
        return polCero()
    (n, a) = ps[0]
    return consPol(n, a, dispersaApolinomio(ps[1:]))

# 2ª definición de dispersaApolinomio
# ===================================

def dispersaApolinomio2(ps: list[tuple[int, A]]) -> Polinomio[A]:
    r: Polinomio[A] = polCero()
    for (n, a) in reversed(ps):
        r = consPol(n, a, r)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(ps=dispersaAleatoria())
def test_dispersaApolinomio(ps: list[tuple[int, int]]) -> None:
    assert dispersaApolinomio(ps) == dispersaApolinomio2(ps)

# El generador dispersaAleatoria está definido en el ejercicio
# "Transformaciones entre las representaciones dispersa y densa" que se
# encuentra en https://bit.ly/402UpuT

# Definición de polinomioAdispersa
# ================================

def polinomioAdispersa(p: Polinomio[A]) -> list[tuple[int, A]]:
    if esPolCero(p):
        return []
    return [(grado(p), coefLider(p))] + polinomioAdispersa(restoPol(p))

# Propiedad de ser inversas
# =========================

# La primera propiedad es
@given(ps=dispersaAleatoria())
def test_polinomioAdispersa_dispersaApolinomio(ps: list[tuple[int,
                                                              int]]) -> None:
    assert polinomioAdispersa(dispersaApolinomio(ps)) == ps

# La segunda propiedad es
@given(p=polinomioAleatorio())
def test_dispersaApolinomio_polinomioAdispersa(p: Polinomio[int]) -> None:
    assert dispersaApolinomio(polinomioAdispersa(p)) == p

# La comprobación es
#    > poetry run pytest -v Polinomios_Transformaciones_polinomios_dispersas.py
#    test_dispersaApolinomio PASSED
#    test_polinomioAdispersa_dispersaApolinomio PASSED
#    test_dispersaApolinomio_polinomioAdispersa PASSED
