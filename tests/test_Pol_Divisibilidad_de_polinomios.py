from src.Pol_Divisibilidad_de_polinomios import divisiblePol
from src.TAD.Polinomio import Polinomio, consPol, polCero


def test_divisiblePol() -> None:
    pol1: Polinomio[float] = consPol(2, 8, consPol(1, 14, consPol(0, 3, polCero())))
    pol2: Polinomio[float] = consPol(1, 2, consPol(0, 3, polCero()))
    pol3: Polinomio[float] = consPol(2, 6, consPol(1, 2, polCero()))
    assert divisiblePol(pol1, pol2)
    assert not divisiblePol(pol1, pol3)
