from src.valor_de_una_expresion_aritmetica_con_una_variable import (C, P, S, X,
                                                                    valor)


def test_valor() -> None:
    assert valor(P(X(), S(C(13), X())), 2) == 30
