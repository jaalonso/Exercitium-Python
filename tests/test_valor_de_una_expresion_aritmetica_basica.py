from src.valor_de_una_expresion_aritmetica_basica import C, P, S, valor


def test_valor() -> None:
    assert valor(P(C(2), S(C(3), C(7)))) == 20
