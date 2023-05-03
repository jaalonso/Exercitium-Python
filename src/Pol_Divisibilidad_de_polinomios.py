# Pol_Divisibilidad_de_polinomios.py
# TAD de los polinomios: Divisibilidad de polinomios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 11-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    divisiblePol : (Polinomio[float], Polinomio[float]) -> bool
# tal que divisiblePol(p, q) se verifica si el polinomio p es divisible
# por el polinomio q. Por ejemplo,
#    >>> pol1 = consPol(2, 8, consPol(1, 14, consPol(0, 3, polCero())))
#    >>> pol1
#    8*x^2 + 14*x + 3
#    >>> pol2 = consPol(1, 2, consPol(0, 3, polCero()))
#    >>> pol2
#    2*x + 3
#    >>> pol3 = consPol(2, 6, consPol(1, 2, polCero()))
#    >>> pol3
#    6*x^2 + 2*x
#    >>> divisiblePol(pol1, pol2)
#    True
#    >>> divisiblePol(pol1, pol3)
#    False
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from src.Pol_Division_de_polinomios import resto
from src.TAD.Polinomio import Polinomio, consPol, esPolCero, polCero


def divisiblePol(p: Polinomio[float], q: Polinomio[float]) -> bool:
    return esPolCero(resto(p, q))
