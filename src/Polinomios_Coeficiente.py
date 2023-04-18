# Polinomios_Coeficiente.py
# TAD de los polinomios: Coeficiente del término de grado k.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 20-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los polinomios]
# (https://bit.ly/3KwqXYu) definir la función
#    coeficiente : (int, Polinomio[A]) -> A
# tal que coeficiente(k, p) es el coeficiente del término de grado k
# del polinomio p. Por ejemplo,
#    >>> ejPol = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
#    >>> ejPol
#    x^5 + 5*x^2 + 4*x
#    >>> coeficiente(2, ejPol)
#    5
#    >>> coeficiente(3, ejPol)
#    0
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from typing import TypeVar

from src.TAD.Polinomio import (Polinomio, coefLider, consPol, grado, polCero,
                               restoPol)

A = TypeVar('A', int, float, complex)

def coeficiente(k: int, p: Polinomio[A]) -> A:
    if k == grado(p):
        return coefLider(p)
    if k > grado(restoPol(p)):
        return 0
    return coeficiente(k, restoPol(p))
