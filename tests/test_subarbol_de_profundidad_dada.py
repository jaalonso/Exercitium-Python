from src.subarbol_de_profundidad_dada import H, N, takeArbol


def test_takeArbol() -> None:
    assert takeArbol(0, N(9, N(3, H(2), H(4)), H(7))) == \
        H(9)
    assert takeArbol(1, N(9, N(3, H(2), H(4)), H(7))) == \
        N(9, H(3), H(7))
    assert takeArbol(2, N(9, N(3, H(2), H(4)), H(7))) == \
        N(9, N(3, H(2), H(4)), H(7))
    assert takeArbol(3, N(9, N(3, H(2), H(4)), H(7))) == \
        N(9, N(3, H(2), H(4)), H(7))
