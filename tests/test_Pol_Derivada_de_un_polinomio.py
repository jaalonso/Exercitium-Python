from src.Pol_Derivada_de_un_polinomio import derivada
from src.TAD.Polinomio import consPol, polCero


def test_derivada() -> None:
    ejPol = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    assert str(derivada(ejPol)) == "5*x^4 + 10*x + 4"
