from src.segmento_de_una_lista import segmento1, segmento2


def test_segmento():
    assert segmento1(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
    assert segmento1(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
    assert segmento1(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
    assert segmento2(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
    assert segmento2(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
    assert segmento2(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
