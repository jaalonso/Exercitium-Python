from src.expresiones_aritmeticas_reducibles import C, P, S, V, reducible


def test_reducible() -> None:
    assert reducible(S(C(3), C(4))) is True
    assert reducible(S(C(3), V('x'))) is False
    assert reducible(S(C(3), P(C(4), C(5)))) is True
    assert reducible(S(V('x'), P(C(4), C(5)))) is True
    assert reducible(S(C(3), P(V('x'), C(5)))) is False
    assert reducible(C(3)) is False
    assert reducible(V('x')) is False
