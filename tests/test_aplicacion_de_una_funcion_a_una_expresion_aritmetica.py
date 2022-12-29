from src.aplicacion_de_una_funcion_a_una_expresion_aritmetica import \
    C, S, P, aplica

def test_aplica() -> None:
    assert aplica(lambda x: 2 + x, S(P(C(3), C(5)), P(C(6), C(7)))) == \
        S(P(C(5), C(7)), P(C(8), C(9)))
    assert aplica(lambda x: 2 * x, S(P(C(3), C(5)), P(C(6), C(7)))) == \
        S(P(C(6), C(10)), P(C(12), C(14)))
