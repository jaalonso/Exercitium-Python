from src.rama_izquierda_de_un_arbol_binario import H, N, ramaIzquierda


def test_ramaIzquierda() -> None:
    assert ramaIzquierda(N(2,
                           N(5, N(3, H(), H()), N(7, H(), H())),
                           N(4, H(), H()))) == \
        [2, 5, 3]
