# Pol_Division_de_polinomios.py
# TAD de los polinomios: División de polinomios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir las funciones
#    cociente : (Polinomio[float], Polinomio[float]) -> Polinomio[float]
#    resto    : (Polinomio[float], Polinomio[float]) -> Polinomio[float]
# tales que
# + cociente(p, q) es el cociente de la división de p entre q. Por
#   ejemplo,
#      >>> pol1 = consPol(3, 2, consPol(2, 9, consPol(1, 10, consPol(0, 4, polCero()))))
#      >>> pol1
#      2*x^3 + 9*x^2 + 10*x + 4
#      >>> pol2 = consPol(2, 1, consPol(1, 3, polCero()))
#      >>> pol2
#      x^2 + 3*x
#      >>> cociente(pol1, pol2)
#      2.0*x + 3.0
# + resto(p, q) es el resto de la división de p entre q. Por ejemplo,
#      >>> resto(pol1, pol2)
#      1.0*x + 4
# ---------------------------------------------------------------------

from src.Pol_Crea_termino import creaTermino
from src.Pol_Multiplicacion_de_un_polinomio_por_un_numero import multEscalar
from src.Pol_Producto_polinomios import multPol, multPorTerm
from src.Pol_Resta_de_polinomios import restaPol
from src.TAD.Polinomio import Polinomio, coefLider, consPol, grado, polCero


def cociente(p: Polinomio[float], q: Polinomio[float]) -> Polinomio[float]:
    n1 = grado(p)
    a1 = coefLider(p)
    n2 = grado(q)
    a2 = coefLider(q)
    n3 = n1 - n2
    a3 = a1 / a2
    p3 = restaPol(p, multPorTerm(creaTermino(n3, a3), q))
    if n2 == 0:
        return multEscalar(1 / a2, p)
    if n1 < n2:
        return polCero()
    return consPol(n3, a3, cociente(p3, q))

def resto(p: Polinomio[float], q: Polinomio[float]) -> Polinomio[float]:
    return restaPol(p, multPol(cociente(p, q), q))
