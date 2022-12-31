from src.maximos_valores_de_una_expresion_aritmetica import \
    C, X, S, R, P, E, maximo

def test_maximo() -> None:
    assert maximo(E(S(C(10), P(R(C(1), X()), X())), 2),
                  list(range(-3, 4))) == (100, [0, 1])
