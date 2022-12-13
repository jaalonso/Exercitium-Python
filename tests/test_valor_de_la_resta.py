from src.valor_de_la_resta import \
    Lit, Suma, Op, resta

def test_valor() -> None:
    assert resta(Lit(42), Lit(2)) == Suma(Lit(42), Op(Lit(2)))
