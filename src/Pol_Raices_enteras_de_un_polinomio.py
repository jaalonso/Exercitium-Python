# Pol_Raices_enteras_de_un_polinomio.py
# TAD de los polinomios: Raíces enteras de un polinomio.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#     raicesRuffini : (Polinomio[int]) -> list[int]
# tal que raicesRuffini(p) es la lista de las raices enteras de p,
# calculadas usando el regla de Ruffini. Por ejemplo,
#    >>> ejPol1 = consPol(4, 3, consPol(2, -5, consPol(0, 3, polCero())))
#    >>> ejPol1
#    3*x^4 + -5*x^2 + 3
#    >>> raicesRuffini(ejPol1)
#    []
#    >>> ejPol2 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
#    >>> ejPol2
#    x^5 + 5*x^2 + 4*x
#    >>> raicesRuffini(ejPol2)
#    [0, -1]
#    >>> ejPol3 = consPol(4, 6, consPol(1, 2, polCero()))
#    >>> ejPol3
#    6*x^4 + 2*x
#    >>> raicesRuffini(ejPol3)
#    [0]
#    >>> ejPol4 = consPol(3, 1, consPol(2, 2, consPol(1, -1, consPol(0, -2, polCero()))))
#    >>> ejPol4
#    x^3 + 2*x^2 + -1*x + -2
#    >>> raicesRuffini(ejPol4)
#    [1, -1, -2]
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from src.Pol_Reconocimiento_de_raices_por_la_regla_de_Ruffini import \
    esRaizRuffini
from src.Pol_Regla_de_Ruffini import cocienteRuffini
from src.Pol_Termino_independiente_de_un_polinomio import terminoIndep
from src.TAD.Polinomio import Polinomio, consPol, esPolCero, polCero


# (divisores n) es la lista de todos los divisores enteros de n. Por
# ejemplo,
#    divisores(4)  == [1, 2, 4, -1, -2, -4]
#    divisores(-6) == [1, 2, 3, 6, -1, -2, -3, -6]
def divisores(n: int) -> list[int]:
    xs = [x for x in range(1, abs(n)+1) if n % x == 0]
    return xs + [-x for x in xs]

def raicesRuffini(p: Polinomio[int]) -> list[int]:
    if esPolCero(p):
        return []
    def aux(rs: list[int]) -> list[int]:
        if not rs:
            return []
        x, *xs = rs
        if esRaizRuffini(x, p):
            return [x] + raicesRuffini(cocienteRuffini(x, p))
        return aux(xs)

    return aux([0] + divisores(terminoIndep(p)))
