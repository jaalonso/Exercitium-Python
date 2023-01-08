from src.valor_de_expresiones_aritmeticas_generales import A, C, Op, valor


def test_valor() -> None:
    assert valor(A(Op.S, A(Op.R, C(7), C(3)), A(Op.M, C(2), C(5)))) == 14
    assert valor(A(Op.M, A(Op.R, C(7), C(3)), A(Op.S, C(2), C(5)))) == 28
