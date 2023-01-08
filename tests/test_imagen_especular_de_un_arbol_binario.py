from src.imagen_especular_de_un_arbol_binario import H, N, espejo


def test_espejo() -> None:
    assert espejo(N(9, N(3, H(2), H(4)), H(7))) == N(9, H(7), N(3, H(4), H(2)))
