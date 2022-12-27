from src.existencia_de_elemento_del_arbol_con_propiedad import \
    H, N, algunoArbol

def test_algunoArbol() -> None:
    assert algunoArbol(N(5, N(3, H(1), H(4)), H(2)), lambda x: x > 4)
    assert not algunoArbol(N(5, N(3, H(1), H(4)), H(2)), lambda x: x > 7)
