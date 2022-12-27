from src.elementos_del_nivel_k_de_un_arbol import \
    H, N, nivel

def test_nivel() -> None:
    assert nivel(0, N(7, N(2, H(5), H(4)), H(9))) == [7]
    assert nivel(1, N(7, N(2, H(5), H(4)), H(9))) == [2, 9]
    assert nivel(2, N(7, N(2, H(5), H(4)), H(9))) == [5, 4]
    assert nivel(3, N(7, N(2, H(5), H(4)), H(9))) == []
