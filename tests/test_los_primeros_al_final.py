from src.los_primeros_al_final import rota


def test_rota():
    assert rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3]
    assert rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2]
    assert rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]
