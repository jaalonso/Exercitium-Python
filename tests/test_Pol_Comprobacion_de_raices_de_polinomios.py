from src.Pol_Comprobacion_de_raices_de_polinomios import esRaiz
from src.TAD.Polinomio import consPol, polCero


def test_esRaioz() -> None:
    ejPol = consPol(4, 6, consPol(1, 2, polCero()))
    assert esRaiz(0, ejPol)
    assert not esRaiz(1, ejPol)
