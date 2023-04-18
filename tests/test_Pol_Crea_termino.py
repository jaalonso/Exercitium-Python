from src.Pol_Crea_termino import creaTermino, creaTermino2


def test_Pol_Crea_termino() -> None:
    assert str(creaTermino(2, 5)) == "5*x^2"
    assert str(creaTermino2(2, 5)) == "5*x^2"
