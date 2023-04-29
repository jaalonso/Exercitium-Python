from src.Pol_Integral_de_un_polinomio import integral
from src.TAD.Polinomio import Polinomio, consPol, polCero


def test_integral() -> None:
    ejPol: Polinomio[float] = consPol(7, 2, consPol(4, 5, consPol(2, 5, polCero())))
    assert str(integral(ejPol)) == "0.25*x^8 + x^5 + 1.6666666666666667*x^3"
