from src.Pol_Raices_enteras_de_un_polinomio import raicesRuffini
from src.TAD.Polinomio import consPol, polCero


def test_raicesRuffini() -> None:
    ejPol1 = consPol(4, 3, consPol(2, -5, consPol(0, 3, polCero())))
    assert raicesRuffini(ejPol1) == []
    ejPol2 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    assert raicesRuffini(ejPol2) == [0, -1]
    ejPol3 = consPol(4, 6, consPol(1, 2, polCero()))
    assert raicesRuffini(ejPol3) == [0]
    ejPol4 = consPol(3, 1, consPol(2, 2, consPol(1, -1, consPol(0, -2, polCero()))))
    assert raicesRuffini(ejPol4) == [1, -1, -2]
