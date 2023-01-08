from src.algoritmo_de_Euclides_del_mcd import mcd


def test_mcd() -> None:
    assert mcd(30, 45) == 15
    assert mcd(45, 30) == 15
