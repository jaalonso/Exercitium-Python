from src.valor_de_una_expresion_aritmetica import \
    Lit, Suma, Op, SiCero, valor

def test_valor() -> None:
    assert valor(Op(Suma(Lit(3), Lit(5)))) == -8
    assert valor(SiCero(Lit(0), Lit(4), Lit(5))) == 4
    assert valor(SiCero(Lit(1), Lit(4), Lit(5))) == 5
