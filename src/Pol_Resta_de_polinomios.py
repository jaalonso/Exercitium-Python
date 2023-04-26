# Pol_Resta_de_polinomios.py
# TAD de los polinomios: Resta de polinomios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    restaPol : (Polinomio[A], Polinomio[A]) -> Polinomio[A]
# tal que restaPol(p, q) es la el polinomio obtenido restándole a p el q. Por
# ejemplo,
#    >>> ejPol1 = consPol(5,1,consPol(4,5,consPol(2,5,consPol(0,9,polCero()))))
#    >>> ejPol2 = consPol(4,3,consPol(2,5,consPol(0,3,polCero())))
#    >>> ejPol1
#    x^5 + 5*x^4 + 5*x^2 + 9
#    >>> ejPol2
#    3*x^4 + 5*x^2 + 3
#    >>> restaPol(ejPol1, ejPol2)
#    x^5 + 2*x^4 + 6
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from typing import TypeVar

from src.Pol_Crea_termino import creaTermino
from src.Pol_Producto_polinomios import multPorTerm
from src.Pol_Suma_de_polinomios import sumaPol
from src.TAD.Polinomio import Polinomio, consPol, polCero

A = TypeVar('A', int, float, complex)

def restaPol(p: Polinomio[A], q: Polinomio[A]) -> Polinomio[A]:
    return sumaPol(p, multPorTerm(creaTermino(0, -1), q))
