from src.calculo_de_pi_mediante_la_formula_de_Leibniz import \
    calculaPi1, calculaPi2, calculaPi3, \
    errorPi1, errorPi2

def test_pi() -> None:
    for calculaPi in [calculaPi1, calculaPi2, calculaPi3]:
        assert calculaPi(3) == 2.8952380952380956
        assert calculaPi(300) == 3.1449149035588526
    for errorPi in [errorPi1, errorPi2]:
        assert errorPi(0.1) == 9
        assert errorPi(0.01) == 99
        assert errorPi(0.001) == 999
