from src.Pol_Valor_de_un_polinomio_en_un_punto import valor
from src.TAD.Polinomio import consPol, polCero


def test_valor() -> None:
    ejPol = consPol(4, 3, consPol(2, -5, consPol(0, 3, polCero())))
    assert valor(ejPol, 0) == 3
    assert valor(ejPol, 1) == 1
    assert valor(ejPol, -2) == 31
