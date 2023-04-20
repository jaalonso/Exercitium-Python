from src.Pol_Producto_polinomios import multPol
from src.TAD.Polinomio import consPol, polCero


def test_Pol_Producto_polinomios() -> None:
    ejPol1 = consPol(4, 3, consPol(2, -5, consPol(0, 3, polCero())))
    ejPol2 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    assert str(multPol(ejPol1, ejPol2)) ==\
        "3*x^9 + -5*x^7 + 15*x^6 + 15*x^5 + -25*x^4 + -20*x^3 + 15*x^2 + 12*x"
