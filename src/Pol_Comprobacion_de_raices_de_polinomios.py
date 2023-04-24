# Pol_Comprobacion_de_raices_de_polinomios.py
# TAD de los polinomios: Comprobación de raíces de polinomios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    esRaiz(A, Polinomio[A]) -> bool
# tal que esRaiz(c, p) se verifica si c es una raiz del polinomio p. Por
# ejemplo,
#    >>> ejPol = consPol(4, 6, consPol(1, 2, polCero()))
#    >>> ejPol
#    6*x^4 + 2*x
#    >>> esRaiz(0, ejPol)
#    True
#    >>> esRaiz(1, ejPol)
#    False
# ---------------------------------------------------------------------

from typing import TypeVar

from src.Pol_Valor_de_un_polinomio_en_un_punto import valor
from src.TAD.Polinomio import Polinomio, consPol, polCero

A = TypeVar('A', int, float, complex)

def esRaiz(c: A, p: Polinomio[A]) -> bool:
    return valor(p, c) == 0
