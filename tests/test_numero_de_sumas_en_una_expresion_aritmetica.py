from src.numero_de_sumas_en_una_expresion_aritmetica import C, P, S, V, sumas


def test_sumas() -> None:
    assert sumas(P(V('z'), S(C(3), V('x')))) == 1
    assert sumas(S(V('z'), S(C(3), V('x')))) == 2
    assert sumas(P(V('z'), P(C(3), V('x')))) == 0
