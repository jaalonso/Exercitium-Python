from src.Pol_Termino_lider import termLider, termLider2
from src.TAD.Polinomio import consPol, polCero


def test_termLider() -> None:
    ejPol = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    assert str(termLider(ejPol)) == "x^5"
    assert str(termLider2(ejPol)) == "x^5"
