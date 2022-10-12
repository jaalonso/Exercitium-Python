from src.limite_del_seno import \
    aproxLimSeno1, aproxLimSeno2, aproxLimSeno3, aproxLimSeno4, \
    aproxLimSeno5, aproxLimSeno6, errorLimSeno1, errorLimSeno2, \
    errorLimSeno3

def test_limite_seno() -> None:
    for aproxLimSeno in [aproxLimSeno1, aproxLimSeno2, aproxLimSeno3,
                         aproxLimSeno4, aproxLimSeno5, aproxLimSeno6]:
        assert aproxLimSeno(1) == [0.8414709848078965]
        assert aproxLimSeno(2) == [0.8414709848078965, 0.958851077208406]
    for errorLimSeno in [errorLimSeno1, errorLimSeno2, errorLimSeno3]:
        assert errorLimSeno(0.1) == 2
        assert errorLimSeno(0.01) == 5
        assert errorLimSeno(0.001) == 13
        assert errorLimSeno(0.0001) == 41
