from src.mayor_numero_con_dos_digitos_dados import numeroMayor1, numeroMayor2


def test_numeroMayor():
    assert numeroMayor1(2, 5) == 52
    assert numeroMayor1(5, 2) == 52
    assert numeroMayor2(2, 5) == 52
    assert numeroMayor2(5, 2) == 52
