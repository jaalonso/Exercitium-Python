# Pol_Valor_de_un_polinomio_en_un_punto.py
# TAD de los polinomios: Valor de un polinomio en un punto.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 28-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    valor : (Polinomio[A], A) -> A
# tal que valor(p, c) es el valor del polinomio p al sustituir su
# variable por c. Por ejemplo,
#    >>> ejPol = consPol(4, 3, consPol(2, -5, consPol(0, 3, polCero())))
#    >>> ejPol
#    3*x^4 + -5*x^2 + 3
#    >>> valor(ejPol, 0)
#    3
#    >>> valor(ejPol, 1)
#    1
#    >>> valor(ejPol, -2)
#    31
# --------------------------------------------------------------------

# pylint: disable=unused-import

from typing import TypeVar

from src.TAD.Polinomio import (Polinomio, coefLider, consPol, esPolCero, grado,
                               polCero, restoPol)

A = TypeVar('A', int, float, complex)

def valor(p: Polinomio[A], c: A) -> A:
    if esPolCero(p):
        return 0
    n = grado(p)
    b = coefLider(p)
    r = restoPol(p)
    return b*c**n + valor(r, c)
