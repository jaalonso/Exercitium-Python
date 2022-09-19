from src.divisores_de_un_numero import \
    divisores1, \
    divisores2, \
    divisores3, \
    divisores4, \
    divisores5, \
    divisores6, \
    divisores7, \
    divisores8

def test_divisores():
    assert divisores1(30) == [1, 2, 3, 5, 6, 10, 15, 30]
    assert divisores2(30) == [1, 2, 3, 5, 6, 10, 15, 30]
    assert divisores3(30) == [1, 2, 3, 5, 6, 10, 15, 30]
    assert divisores4(30) == [1, 2, 3, 5, 6, 10, 15, 30]
    assert divisores5(30) == [1, 2, 3, 5, 6, 10, 15, 30]
    assert divisores6(30) == [1, 2, 3, 5, 6, 10, 15, 30]
    assert divisores7(30) == [1, 2, 3, 5, 6, 10, 15, 30]
    assert divisores8(30) == [1, 2, 3, 5, 6, 10, 15, 30]
