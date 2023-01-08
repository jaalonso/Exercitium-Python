from src.suma_de_un_arbol import H, N, sumaArbol


def test_sumaArbol() -> None:
    assert sumaArbol(N(2,
                       N(5, N(3, H(), H()), N(7, H(), H())),
                       N(4, H(), H()))) == \
        21
