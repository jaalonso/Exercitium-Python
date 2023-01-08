from src.arboles_balanceados import H, N, balanceado


def test_balanceado() -> None:
    assert balanceado (N(5, H(), N(3, H(), H()))) is True
    assert balanceado(N(4,
                        N(3, N(2, H(), H()), H()),
                        N(5, H(), N(6, H(), N(7, H(), H()))))) is False
