# Pol_Integral_definida_de_un_polinomio.py
# TAD de los polinomios: Integral definida de un polinomio.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 8-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de datos de los polinomios](https://bit.ly/3KwqXYu)
# definir la función
#    integralDef : (Polinomio[float], float, float) -> float
# tal que integralDef(p, a, b) es la integral definida del polinomio p
# cuyos coefientes son números racionales. Por ejemplo,
#    >>> ejPol = consPol(7, 2, consPol(4, 5, consPol(2, 5, polCero())))
#    >>> ejPol
#    2*x^7 + 5*x^4 + 5*x^2
#    >>> integralDef(ejPol, 0, 1)
#    2.916666666666667
# ---------------------------------------------------------------------

from src.Pol_Integral_de_un_polinomio import integral
from src.Pol_Valor_de_un_polinomio_en_un_punto import valor
from src.TAD.Polinomio import Polinomio, consPol, polCero


def integralDef(p: Polinomio[float], a: float, b: float) -> float:
    q = integral(p)
    return valor(q, b) - valor(q, a)
