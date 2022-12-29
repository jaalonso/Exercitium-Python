from src.valor_de_una_expresion_aritmetica_con_una_variable import \
    X, C, S, P, valor

def test_valor() -> None:
    assert valor(P(X(), S(C(13), X())), 2) == 30
