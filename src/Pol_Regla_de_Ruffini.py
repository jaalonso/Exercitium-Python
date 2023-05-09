# Pol_Regla_de_Ruffini.py
# TAD de los polinomios: Regla de Ruffini.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 17-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir las funciones
#    cocienteRuffini : (int, Polinomio[int]) -> Polinomio[int]
#    restoRuffini    : (int, Polinomio[int]) -> int
# tales que
# + cocienteRuffini(r, p) es el cociente de dividir el polinomio p por
#   el polinomio x-r. Por ejemplo:
#      λ> ejPol = consPol(3, 1, consPol(2, 2, consPol(1, -1, consPol(0, -2, polCero()))))
#      λ> ejPol
#      x^3 + 2*x^2 + -1*x + -2
#      λ> cocienteRuffini(2, ejPol)
#      x^2 + 4*x + 7
#      λ> cocienteRuffini(-2, ejPol)
#      x^2 + -1
#      λ> cocienteRuffini(3, ejPol)
#      x^2 + 5*x + 14
# + restoRuffini(r, p) es el resto de dividir el polinomio p por el
#   polinomio x-r. Por ejemplo,
#      λ> restoRuffini(2, ejPol)
#      12
#      λ> restoRuffini(-2, ejPol)
#      0
#      λ> restoRuffini(3, ejPol)
#      40
#
# Comprobar con Hypothesis que, dado un polinomio p y un número entero
# r, las funciones anteriores verifican la propiedad de la división
# euclídea.
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from hypothesis import given
from hypothesis import strategies as st

from src.Pol_Crea_termino import creaTermino
from src.Pol_Division_de_Ruffini_con_representacion_densa import ruffiniDensa
from src.Pol_Producto_polinomios import multPol
from src.Pol_Suma_de_polinomios import sumaPol
from src.Pol_Transformaciones_polinomios_densas import (densaApolinomio,
                                                        polinomioAdensa)
from src.TAD.Polinomio import (Polinomio, consPol, esPolCero, polCero,
                               polinomioAleatorio)


def cocienteRuffini(r: int, p: Polinomio[int]) -> Polinomio[int]:
    if esPolCero(p):
        return polCero()
    return densaApolinomio(ruffiniDensa(r, polinomioAdensa(p))[:-1])

def restoRuffini(r: int, p: Polinomio[int]) -> int:
    if esPolCero(p):
        return 0
    return ruffiniDensa(r, polinomioAdensa(p))[-1]

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(r=st.integers(), p=polinomioAleatorio())
def test_diviEuclidea (r: int, p: Polinomio[int]) -> None:
    coci = cocienteRuffini(r, p)
    divi = densaApolinomio([1, -r])
    rest = creaTermino(0, restoRuffini(r, p))
    assert p == sumaPol(multPol(coci, divi), rest)

# La comprobación es
#    src> poetry run pytest -q Pol_Regla_de_Ruffini.py
#    1 passed in 0.32s
