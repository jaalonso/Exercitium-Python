from src.movimientos_en_el_plano import (Direccion, movimiento1, movimiento2,
                                         movimientos1, movimientos2, opuesta1,
                                         opuesta2)


def test_movimientos() -> None:
    assert opuesta1(Direccion.Izquierda) == Direccion.Derecha
    assert movimiento1((2, 5), Direccion.Arriba) == (2, 6)
    assert movimiento1((2, 5), opuesta1(Direccion.Abajo)) == (2, 6)
    assert movimientos1((2, 5), [Direccion.Arriba, Direccion.Izquierda])\
        == (1, 6)
    assert opuesta2(Direccion.Izquierda) == Direccion.Derecha
    assert movimiento2((2, 5), Direccion.Arriba) == (2, 6)
    assert movimiento2((2, 5), opuesta1(Direccion.Abajo)) == (2, 6)
    assert movimientos2((2, 5), [Direccion.Arriba, Direccion.Izquierda])\
        == (1, 6)
