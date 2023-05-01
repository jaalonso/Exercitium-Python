# Pol_Multiplicacion_de_un_polinomio_por_un_numero.py
# TAD de los polinomios: Multiplicación de un polinomio por un número.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    multEscalar : (A, Polinomio[A]) -> Polinomio[A]
# tal que multEscalar(c, p) es el polinomio obtenido multiplicando el
# número c por el polinomio p. Por ejemplo,
#    >>> ejPol = consPol(1, 2, consPol(0, 3, polCero()))
#    >>> ejPol
#    2*x + 3
#    >>> multEscalar(4, ejPol)
#    8*x + 12
#    >>> from fractions import Fraction
#    >>> multEscalar(Fraction('1/4'), ejPol)
#    1/2*x + 3/4
# ---------------------------------------------------------------------

from typing import TypeVar

from src.TAD.Polinomio import (Polinomio, coefLider, consPol, esPolCero, grado,
                               polCero, restoPol)

A = TypeVar('A', int, float, complex)

def multEscalar(c: A, p: Polinomio[A]) -> Polinomio[A]:
    if esPolCero(p):
        return polCero()
    n = grado(p)
    b = coefLider(p)
    r = restoPol(p)
    return consPol(n, c * b, multEscalar(c, r))
