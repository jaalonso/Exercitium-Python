from src.rango_de_una_lista import rango


def test_rango():
    assert rango([3, 2, 7, 5]) == [2, 7]
