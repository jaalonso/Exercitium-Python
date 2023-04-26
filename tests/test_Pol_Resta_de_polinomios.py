from src.Pol_Resta_de_polinomios import restaPol
from src.TAD.Polinomio import consPol, polCero


def test_restPol() -> None:
    ejPol1 = consPol(5,1,consPol(4,5,consPol(2,5,consPol(0,9,polCero()))))
    ejPol2 = consPol(4,3,consPol(2,5,consPol(0,3,polCero())))
    assert str(restaPol(ejPol1, ejPol2)) == "x^5 + 2*x^4 + 6"
