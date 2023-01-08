from src.suma_de_divisores import (sumaDivisores1, sumaDivisores2,
                                   sumaDivisores3, sumaDivisores4,
                                   sumaDivisores5, sumaDivisores6)


def test_sumaDivisores():
    assert sumaDivisores1(12) == 28
    assert sumaDivisores1(25) == 31
    assert sumaDivisores2(12) == 28
    assert sumaDivisores2(25) == 31
    assert sumaDivisores3(12) == 28
    assert sumaDivisores3(25) == 31
    assert sumaDivisores4(12) == 28
    assert sumaDivisores4(25) == 31
    assert sumaDivisores5(12) == 28
    assert sumaDivisores5(25) == 31
    assert sumaDivisores6(12) == 28
    assert sumaDivisores6(25) == 31
