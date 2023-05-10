from src.Pol_Reconocimiento_de_raices_por_la_regla_de_Ruffini import \
    esRaizRuffini
from src.TAD.Polinomio import consPol, polCero


def test_esRaizRuffini() -> None:
    ejPol = consPol(4, 6, consPol(1, 2, polCero()))
    assert esRaizRuffini(0, ejPol)
    assert not esRaizRuffini(1, ejPol)
