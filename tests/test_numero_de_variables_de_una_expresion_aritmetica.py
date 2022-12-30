from src.numero_de_variables_de_una_expresion_aritmetica import \
    X, C, S, P, numVars

def test_numVars() -> None:
    assert numVars(C(3)) == 0
    assert numVars(X()) == 1
    assert numVars(P(X(), S(C(13), X()))) == 2
