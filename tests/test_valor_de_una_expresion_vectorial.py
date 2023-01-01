from src.valor_de_una_expresion_vectorial import \
    Vec, Sum, Mul, valorEV1, valorEV2

def test_valoeEV() -> None:
    for valorEV in [valorEV1, valorEV2]:
        assert valorEV(Vec(1, 2)) == (1, 2)
        assert valorEV(Sum(Vec(1, 2), Vec(3, 4))) == (4, 6)
        assert valorEV(Mul(2, Vec(3, 4))) == (6, 8)
        assert valorEV(Mul(2, Sum(Vec(1, 2), Vec(3, 4)))) == (8, 12)
        assert valorEV(Sum(Mul(2, Vec(1, 2)), Mul(2, Vec(3, 4)))) == (8, 12)
