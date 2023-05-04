from src.Pol_Metodo_de_Horner_del_valor_de_un_polinomio import horner, horner2
from src.TAD.Polinomio import Polinomio, consPol, polCero


def test_horner() -> None:
    pol1: Polinomio[float] = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    for horner_ in [horner, horner2]:
        assert horner_(pol1, 0) == 0
        assert horner_(pol1, 1) == 10
        assert horner_(pol1, 1.5) == 24.84375
