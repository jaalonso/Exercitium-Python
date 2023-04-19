from src.Pol_Suma_de_polinomios import sumaPol, sumaPol2
from src.TAD.Polinomio import consPol, polCero


def test_Pol_Suma_de_polinomios() -> None:
    ejPol1 = consPol(4, 3, consPol(2, -5, consPol(0, 3, polCero())))
    ejPol2 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    assert str(sumaPol(ejPol1, ejPol2)) == "x^5 + 3*x^4 + 4*x + 3"
    assert str(sumaPol2(ejPol1, ejPol2)) == "x^5 + 3*x^4 + 4*x + 3"
