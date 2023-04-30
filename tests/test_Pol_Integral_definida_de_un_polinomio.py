from src.Pol_Integral_definida_de_un_polinomio import integralDef
from src.TAD.Polinomio import Polinomio, consPol, polCero


def test_integralDef () -> None:
    ejPol: Polinomio[float] = consPol(7, 2, consPol(4, 5, consPol(2, 5, polCero())))
    assert integralDef(ejPol, 0, 1) == 2.916666666666667
