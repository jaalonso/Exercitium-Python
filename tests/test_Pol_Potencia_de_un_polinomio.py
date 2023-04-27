from src.Pol_Potencia_de_un_polinomio import potencia, potencia2, potencia3
from src.TAD.Polinomio import consPol, polCero


def test_potencia() -> None:
    ejPol = consPol(1, 2, consPol(0, 3, polCero()))
    for potencia_ in [potencia, potencia2, potencia3]:
        assert str(potencia_(ejPol, 2)) == "4*x^2 + 12*x + 9"
        assert str(potencia_(ejPol, 3)) == "8*x^3 + 36*x^2 + 54*x + 27"
