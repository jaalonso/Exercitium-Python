from src.arbol_de_factorizacion import \
    H, N, arbolFactorizacion1, arbolFactorizacion2

def test_arbolFactorizacion() -> None:
    for arbolFactorizacion in [arbolFactorizacion1,
                               arbolFactorizacion2]:
        assert arbolFactorizacion(60) == N(60,
                                           N(6, H(2), H(3)),
                                           N(10, H(2), H(5)))
        assert arbolFactorizacion(45) == N(45, H(5), N(9, H(3), H(3)))
        assert arbolFactorizacion(7) == H(7)
        assert arbolFactorizacion(9) == N(9, H(3), H(3))
        assert arbolFactorizacion(14) == N(14, H(2), H(7))
        assert arbolFactorizacion(28) == N(28, N(4, H(2), H(2)), H(7))
        assert arbolFactorizacion(84) == N(84,
                                           H(7),
                                           N(12, H(3), N(4, H(2), H(2))))
