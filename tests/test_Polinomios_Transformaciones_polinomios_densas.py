from src.Polinomios_Transformaciones_polinomios_densas import (
    densaApolinomio, densaApolinomio2, polinomioAdensa, polinomioAdensa2)
from src.TAD.Polinomio import consPol, polCero


def test_Polinomios_Transformaciones_polinomios_densas() -> None:
    assert str(densaApolinomio([9, 0, 0, 5, 0, 4, 7]))\
        == "9*x^6 + 5*x^3 + 4*x + 7"
    assert str(densaApolinomio2([9, 0, 0, 5, 0, 4, 7]))\
        == "9*x^6 + 5*x^3 + 4*x + 7"
    ejPol = consPol(6, 9, consPol(3, 5, consPol(1, 4, consPol(0, 7, polCero()))))
    assert polinomioAdensa(ejPol) == [9, 0, 0, 5, 0, 4, 7]
    assert polinomioAdensa2(ejPol) == [9, 0, 0, 5, 0, 4, 7]
