from src.numero_de_operaciones_en_una_expresion import Lit, Op, Suma, numeroOps


def test_numeroOps() -> None:
    assert numeroOps(Lit(3)) == 0
    assert numeroOps(Suma(Lit(7), Op(Lit(5)))) == 2
