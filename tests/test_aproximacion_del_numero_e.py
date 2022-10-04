from src.aproximacion_del_numero_e import \
    aproxE1, \
    aproxE2, \
    aproxE3, \
    aproxE4, \
    aproxE5, \
    aproxE6, \
    errorAproxE1, \
    errorAproxE2, \
    errorAproxE3

def test_aproxE() -> None:
    for aproxE in [aproxE1, aproxE2, aproxE3, aproxE4, aproxE5,
                   aproxE6]:
        assert aproxE(4) == [2.0, 2.25, 2.37037037037037, 2.44140625]
    for errorAproxE in [errorAproxE1, errorAproxE2, errorAproxE3]:
        assert errorAproxE(0.1) == 13
        assert errorAproxE(0.01) == 135
        assert errorAproxE(0.001) == 1359
