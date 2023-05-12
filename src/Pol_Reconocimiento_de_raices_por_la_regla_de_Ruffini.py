# Pol_Reconocimiento_de_raices_por_la_regla_de_Ruffini.py
# TAD de los polinomios: Reconocimiento de raíces por la regla de Ruffini.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 18-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    esRaizRuffini : (int, Polinomio[int]) -> bool
# tal que esRaizRuffini(r, p) se verifica si r es una raiz de p, usando
# para ello el regla de Ruffini. Por ejemplo,
#    >>> ejPol = consPol(4, 6, consPol(1, 2, polCero()))
#    >>> ejPol
#    6*x^4 + 2*x
#    >>> esRaizRuffini(0, ejPol)
#    True
#    >>> esRaizRuffini(1, ejPol)
#    False
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from src.Pol_Regla_de_Ruffini import restoRuffini
from src.TAD.Polinomio import Polinomio, consPol, polCero


def esRaizRuffini(r: int, p: Polinomio[int]) -> bool:
    return restoRuffini(r, p) == 0
