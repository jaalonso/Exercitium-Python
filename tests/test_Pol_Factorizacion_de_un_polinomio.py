from src.Pol_Factorizacion_de_un_polinomio import factorizacion
from src.TAD.Polinomio import consPol, polCero


def test_factorizacion() -> None:
    ejPol1 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
    assert list(map(str, factorizacion(ejPol1))) \
        == ["1*x", "1*x + 1", "x^3 + -1*x^2 + 1*x + 4"]
    ejPol2 = consPol(3, 1, consPol(2, 2, consPol(1, -1, consPol(0, -2, polCero()))))
    assert list(map(str, factorizacion(ejPol2))) \
        == ["1*x + -1", "1*x + 1", "1*x + 2", "1"]
