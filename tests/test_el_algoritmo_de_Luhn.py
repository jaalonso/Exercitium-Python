from src.el_algoritmo_de_Luhn import luhn


def test_luhn() -> None:
    assert luhn(5594589764218858) is True
    assert luhn(1234567898765432) is False
