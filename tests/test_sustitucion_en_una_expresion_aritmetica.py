from src.sustitucion_en_una_expresion_aritmetica import C, P, S, V, sustitucion


def test_sustitucion() -> None:
    assert sustitucion(P(V('z'), S(C(3), V('x'))),
                       [('x', 7), ('z', 9)]) == \
        P(C(9), S(C(3), C(7)))
    assert sustitucion(P(V('z'), S(C(3), V('y'))),
                       [('x', 7), ('z', 9)]) == \
        P(C(9), S(C(3), V('y')))
