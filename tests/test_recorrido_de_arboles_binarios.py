from src.recorrido_de_arboles_binarios import \
    H, N, preorden, postorden

def test_recorrido() -> None:
    assert preorden(N(9, N(3, H(2), H(4)), H(7))) == [9, 3, 2, 4, 7]
    assert postorden(N(9, N(3, H(2), H(4)), H(7))) == [2, 4, 3, 7, 9]
