# Pol_Factorizacion_de_un_polinomio.py
# TAD de los polinomios: Factorización de un polinomio.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    factorizacion : (Polinomio[int]) -> list[Polinomio[int]]
# tal que factorizacion(p) es la lista de la descomposición del
# polinomio p en factores obtenida mediante el regla de Ruffini. Por
# ejemplo,
#    >>> ejPol1 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
#    >>> ejPol1
#    x^5 + 5*x^2 + 4*x
#    >>> factorizacion(ejPol1)
#    [1*x, 1*x + 1, x^3 + -1*x^2 + 1*x + 4]
#    >>> ejPol2 = consPol(3, 1, consPol(2, 2, consPol(1, -1, consPol(0, -2, polCero()))))
#    >>> ejPol2
#    x^3 + 2*x^2 + -1*x + -2
#    >>> factorizacion(ejPol2)
#    [1*x + -1, 1*x + 1, 1*x + 2, 1]
# ---------------------------------------------------------------------

from src.Pol_Raices_enteras_de_un_polinomio import divisores
from src.Pol_Reconocimiento_de_raices_por_la_regla_de_Ruffini import \
    esRaizRuffini
from src.Pol_Regla_de_Ruffini import cocienteRuffini
from src.Pol_Termino_independiente_de_un_polinomio import terminoIndep
from src.Pol_Transformaciones_polinomios_densas import densaApolinomio
from src.TAD.Polinomio import Polinomio, consPol, esPolCero, polCero


def factorizacion(p: Polinomio[int]) -> list[Polinomio[int]]:
    def aux(xs: list[int]) -> list[Polinomio[int]]:
        if not xs:
            return [p]
        r, *rs = xs
        if esRaizRuffini(r, p):
            return [densaApolinomio([1, -r])] + factorizacion(cocienteRuffini(r, p))
        return aux(rs)

    if esPolCero(p):
        return [p]
    return aux([0] + divisores(terminoIndep(p)))
