from src.Pol_Multiplicacion_de_un_polinomio_por_un_numero import multEscalar
from src.TAD.Polinomio import consPol, polCero


def test_multEscalar() -> None:
    ejPol = consPol(1, 2, consPol(0, 3, polCero()))
    assert str(multEscalar(4, ejPol)) == "8*x + 12"
