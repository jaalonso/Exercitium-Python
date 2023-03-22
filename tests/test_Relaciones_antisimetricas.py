from src.Relaciones_antisimetricas import (antisimetrica, antisimetrica2,
                                           antisimetrica3, antisimetrica4,
                                           antisimetrica5)


def test_antisimetrica_() -> None:
    for antisimetrica_ in [antisimetrica, antisimetrica2, antisimetrica3,
                           antisimetrica4, antisimetrica5]:
        assert antisimetrica_(([1,2],[(1,2)]))
        assert not antisimetrica_(([1,2],[(1,2),(2,1)]))
        assert antisimetrica_(([1,2],[(1,1),(2,1)]))
