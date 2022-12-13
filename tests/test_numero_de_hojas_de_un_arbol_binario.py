from src.numero_de_hojas_de_un_arbol_binario import \
    H, N, nHojas, nNodos

def test_nHojas() -> None:
    assert nHojas(N(9, N(3, H(2), H(4)), H(7))) == 3
    assert nNodos(N(9, N(3, H(2), H(4)), H(7))) == 2
