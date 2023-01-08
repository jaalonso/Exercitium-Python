from src.arbol_de_profundidad_n_con_nodos_iguales import H, N, replicateArbol


def test_replicateArbol() -> None:
    assert replicateArbol(0, 5) == \
        H(5)
    assert replicateArbol(1, 5) == \
        N(5, H(5), H(5))
    assert replicateArbol(2, 5) == \
        N(5, N(5, H(5), H(5)), N(5, H(5), H(5)))
