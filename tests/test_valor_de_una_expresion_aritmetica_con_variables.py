from src.valor_de_una_expresion_aritmetica_con_variables import \
    C, V, S, P, valor

def test_valor() -> None:
    assert valor(P(C(2), S(V('a'), V('b'))),
                 [('a', 2), ('b', 5)]) == 14
