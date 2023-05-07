from src.Pol_Termino_independiente_de_un_polinomio import terminoIndep
from src.TAD.Polinomio import consPol, polCero


def test_terminoIndep() -> None:
    ejPol1 = consPol(4, 3, consPol(2, 5, consPol(0, 3, polCero())))
    ejPol2 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    assert terminoIndep(ejPol1) == 3
    assert terminoIndep(ejPol2) == 0
