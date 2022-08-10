from src.tres_iguales import tresIguales1, tresIguales2


def test_tresIguales():
    assert tresIguales1(4, 4, 4) is True
    assert tresIguales1(4, 3, 4) is False
    assert tresIguales2(4, 4, 4) is True
    assert tresIguales2(4, 3, 4) is False
