from src.Pol_Division_de_polinomios import cociente, resto
from src.TAD.Polinomio import Polinomio, consPol, polCero


def test_division() -> None:
    pol1: Polinomio[float] = consPol(3, 2, consPol(2, 9, consPol(1, 10, consPol(0, 4, polCero()))))
    pol2: Polinomio[float] = consPol(2, 1, consPol(1, 3, polCero()))
    assert str(cociente(pol1, pol2)) == "2.0*x + 3.0"
    assert str(resto(pol1, pol2)) == "1.0*x + 4"
