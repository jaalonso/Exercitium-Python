from src.Pol_Regla_de_Ruffini import cocienteRuffini, restoRuffini
from src.TAD.Polinomio import consPol, polCero


def test_Ruffini() -> None:
    ejPol = consPol(3, 1, consPol(2, 2, consPol(1, -1, consPol(0, -2, polCero()))))
    assert str(cocienteRuffini(2, ejPol)) == "x^2 + 4*x + 7"
    assert str(cocienteRuffini(-2, ejPol)) == "x^2 + -1"
    assert str(cocienteRuffini(3, ejPol)) == "x^2 + 5*x + 14"
    assert restoRuffini(2, ejPol) == 12
    assert restoRuffini(-2, ejPol) == 0
    assert restoRuffini(3, ejPol) == 40
