from src.primeros_y_ultimos_elementos import extremos


def test_extremos():
    assert extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]
