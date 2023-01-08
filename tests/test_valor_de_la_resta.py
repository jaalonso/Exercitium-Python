from src.valor_de_la_resta import Lit, Op, Suma, resta


def test_valor() -> None:
    assert resta(Lit(42), Lit(2)) == Suma(Lit(42), Op(Lit(2)))
