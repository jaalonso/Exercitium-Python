# Pol_Integral_de_un_polinomio.py
# TAD de los polinomios: Integral de un polinomio.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    integral : (Polinomio[float]) -> Polinomio[float]
# tal que integral(p) es la integral del polinomio p cuyos coefientes
# son números decimales. Por ejemplo,
#    >>> ejPol = consPol(7, 2, consPol(4, 5, consPol(2, 5, polCero())))
#    >>> ejPol
#    2*x^7 + 5*x^4 + 5*x^2
#    >>> integral(ejPol)
#    0.25*x^8 + x^5 + 1.6666666666666667*x^3
# ---------------------------------------------------------------------

from src.TAD.Polinomio import (Polinomio, coefLider, consPol, esPolCero, grado,
                               polCero, restoPol)


def integral(p: Polinomio[float]) -> Polinomio[float]:
    if esPolCero(p):
        return  polCero()
    n = grado(p)
    b = coefLider(p)
    r = restoPol(p)
    return consPol(n + 1, b / (n + 1), integral(r))
