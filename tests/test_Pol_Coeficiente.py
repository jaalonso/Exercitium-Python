from src.Pol_Coeficiente import coeficiente
from src.TAD.Polinomio import consPol, polCero


def test_coeficiente() -> None:
    ejPol = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    assert coeficiente(2, ejPol) == 5
    assert coeficiente(3, ejPol) == 0
