# Pol_Termino_independiente_de_un_polinomio.py
# TAD de los polinomios: Término independiente de un polinomio.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu)
# definir la función
#    terminoIndep : (Polinomio[A]) -> A
# tal que terminoIndep(p) es el término independiente del polinomio
# p. Por ejemplo,
#    >>> ejPol1 = consPol(4, 3, consPol(2, 5, consPol(0, 3, polCero())))
#    >>> ejPol1
#    3*x^4 + 5*x^2 + 3
#    >>> terminoIndep(ejPol1)
#    3
#    >>> ejPol2 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
#    >>> ejPol2
#    x^5 + 5*x^2 + 4*x
#    >>> terminoIndep(ejPol2)
#    0
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from typing import TypeVar

from src.Pol_Coeficiente import coeficiente
from src.TAD.Polinomio import Polinomio, consPol, polCero

A = TypeVar('A', int, float, complex)

def terminoIndep(p: Polinomio[A]) -> A:
    return coeficiente(0, p)
