from src.segmento_de_una_lista import segmento


def test_segmento():
    assert segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
    assert segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
    assert segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
