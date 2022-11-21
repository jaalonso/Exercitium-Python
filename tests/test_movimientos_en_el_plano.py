from src.movimientos_en_el_plano import \
    opuesta1, opuesta2, \
    movimiento1, movimiento2, \
    movimientos1, movimientos2

def test_movimientos() -> None:
    assert opuesta1('Izquierda') == 'Derecha'
    assert movimiento1((2 , 5), 'Arriba') == (2, 6)
    assert movimiento1((2, 5), opuesta1('Abajo')) == (2, 6)
    assert movimientos1((2, 5),  ['Arriba', 'Izquierda']) == (1, 6)
    assert opuesta2('Izquierda') == 'Derecha'
    assert movimiento2((2 , 5), 'Arriba') == (2, 6)
    assert movimiento2((2, 5), opuesta1('Abajo')) == (2, 6)
    assert movimientos2((2, 5),  ['Arriba', 'Izquierda']) == (1, 6)
