from src.puntos_dentro_del_circulo import circulo1, circulo2

def test_circulo() -> None:
    for circulo in [circulo1, circulo2]:
        assert circulo(3) == 9
        assert circulo(4) == 15
        assert circulo(5) == 22
        assert circulo(100) == 7949
