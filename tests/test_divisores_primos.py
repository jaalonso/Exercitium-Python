from src.divisores_primos import \
    divisoresPrimos1, \
    divisoresPrimos2, \
    divisoresPrimos3, \
    divisoresPrimos4


def test_divisoresPrimos():
    assert divisoresPrimos1(40) == [2, 5]
    assert divisoresPrimos1(70) == [2, 5, 7]
    assert divisoresPrimos2(40) == [2, 5]
    assert divisoresPrimos3(70) == [2, 5, 7]
    assert divisoresPrimos3(40) == [2, 5]
    assert divisoresPrimos3(70) == [2, 5, 7]
    assert divisoresPrimos4(40) == [2, 5]
    assert divisoresPrimos4(70) == [2, 5, 7]
