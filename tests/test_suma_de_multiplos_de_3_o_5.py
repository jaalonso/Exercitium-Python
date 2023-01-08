from src.suma_de_multiplos_de_3_o_5 import (euler1a, euler1b, euler1c, euler1d,
                                            euler1e, euler1f)


def test_euler() -> None:
    assert euler1a(10) == 23
    assert euler1a(10**2) == 2318
    assert euler1b(10) == 23
    assert euler1b(10**2) == 2318
    assert euler1c(10) == 23
    assert euler1c(10**2) == 2318
    assert euler1d(10) == 23
    assert euler1d(10**2) == 2318
    assert euler1e(10) == 23
    assert euler1e(10**2) == 2318
    assert euler1f(10) == 23
    assert euler1f(10**2) == 2318
