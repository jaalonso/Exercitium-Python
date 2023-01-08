from src.puntos_dentro_del_circulo import (circulo1, circulo2, circulo3,
                                           circulo4)


def test_circulo() -> None:
    for circulo in [circulo1, circulo2, circulo3, circulo4]:
        assert circulo(1)    ==  3
        assert circulo(2)    ==  6
        assert circulo(3)    ==  11
        assert circulo(4)    ==  17
        assert circulo(100)  ==  7955
