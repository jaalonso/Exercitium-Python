from src.profundidad_de_un_arbol_binario import H, N, profundidad


def test_profundidad() -> None:
    assert profundidad(N(9, N(3, H(2), H(4)), H(7))) == 2
    assert profundidad(N(9, N(3, H(2), N(1, H(4), H(5))), H(7))) == 3
    assert profundidad(N(4, N(5, H(4), H(2)), N(3, H(7), H(4)))) == 2
